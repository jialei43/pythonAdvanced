#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dewu（得物）鞋子规格&价格一键抓取
运行：python dewu_shoes.py
同级目录会生成 dewu_shoes.csv 与日志文件
"""
# --------------------  1.  导入区  --------------------
import csv                 # 用于把结果写入 CSV
import json                # 解析/序列化 JSON 数据
import logging             # 记录日志，方便排查
import os                  # 判断文件是否存在等系统操作
import random              # 随机延时，降低被封概率
import time                # sleep 控制抓取速度
from datetime import datetime  # 记录每条数据的抓取时间

import requests            # 发起 HTTP 请求
from tqdm import tqdm      # 进度条，让等待不再焦虑

# --------------------  2.  配置区  --------------------
KEY_WORD = "鞋子"          # 搜索关键词，可换成“AJ1”“Yeezy”等
SAVE_CSV = "dewu_shoes.csv"   # 结果保存路径
MAX_PAGE = 10              # 抓多少页（每页 40 条），想多抓就调大
TIMEOUT = 8                # 单次请求最长等待秒数
# 请求头，伪装成安卓手机浏览器
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; SM-G9730) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "Referer": "https://m.dewu.com/",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
# -----------------------------------------------------

# 2.1 配置日志：同时输出到控制台和 run.log 文件
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[logging.FileHandler("run.log", encoding="utf-8"), logging.StreamHandler()]
)

# 2.2 复用 Session，自动保持 cookie、连接池，提高性能
session = requests.Session()
session.headers.update(HEADERS)


# --------------------  3.  工具函数  --------------------
def random_sleep(a=1, b=3):
    """在 a 到 b 秒之间随机 sleep，降低被封概率"""
    time.sleep(random.uniform(a, b))


def save_csv(rows):
    """
    将 rows 追加写入 SAVE_CSV。
    首次写入会自动写表头；以后每次追加，实现断点续跑。
    """
    first = not os.path.exists(SAVE_CSV)      # 文件不存在说明第一次写
    with open(SAVE_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if first:                             # 写表头
            writer.writerow(["spuId", "标题", "尺码", "价格", "规格JSON", "抓取时间"])
        writer.writerows(rows)                # 写数据


# --------------------  4.  搜索接口 --------------------
def search_shoes(page: int):
    """
    调用得物搜索接口，返回当前页 40 条简略商品列表
    page: 页码，从 1 开始
    """
    url = "https://m.dewu.com/router/search/search"   # 搜索接口
    params = {
        "keyword": KEY_WORD,   # 搜索关键词
        "page": page,          # 第几页
        "limit": 40,           # 每页条数
        "sortType": 0,         # 0=综合排序，可改成 1=价格升序等
        "showHot": 1
    }
    resp = session.get(url, params=params, timeout=TIMEOUT)  # 发 GET
    resp.raise_for_status()                                  # 如果状态码非 200 会抛异常
    data = resp.json()                                       # 转 JSON
    if data.get("code") != 200:                              # 得物自定义错误码
        raise RuntimeError(f"搜索接口异常：{data}")
    return data["data"]["list"]                              # 返回商品列表


# --------------------  5.  详情接口 --------------------
def parse_detail(spu_id: str):
    """
    根据 spuId 拉取详情页，解析出所有尺码及其对应价格
    返回 List[dict]，每条 dict 含 size/price 等信息
    """
    url = "https://m.dewu.com/router/product/detail"   # 详情接口
    params = {"spuId": spu_id}                         # 唯一商品 ID
    resp = session.get(url, params=params, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 200:
        logging.warning(f"详情拉取失败 spuId={spu_id}, msg={data.get('msg')}")
        return []                                      # 空列表表示没抓到

    d = data["data"]           # 真正的详情数据
    title = d["title"]         # 商品标题
    sku_list = d["skuList"]    # 各尺码对应价格、库存等
    rows = []
    for sku in sku_list:       # 遍历所有尺码
        rows.append({
            "spuId": spu_id,
            "标题": title,
            "尺码": sku["size"],
            "价格": sku["price"],
            "规格JSON": json.dumps(sku, ensure_ascii=False)  # 整段原始规格备用
        })
    return rows


# --------------------  6.  主流程 --------------------
def main():
    logging.info("开始抓取得物鞋子数据...")
    all_spu = set()                       # 用来去重，防止重复抓

    # 如果本地已有 CSV，先读入已抓过的 spuId，实现断点续跑
    if os.path.exists(SAVE_CSV):
        with open(SAVE_CSV, encoding="utf-8") as f:
            # 跳过表头，把第一列 spuId 加入集合
            all_spu = {r[0] for r in csv.reader(f) if r and r[0] != "spuId"}

    # 逐页抓取
    for page in range(1, MAX_PAGE + 1):
        try:
            items = search_shoes(page)        # 拿到当前页 40 条
            if not items:                     # 没数据就提前结束
                break
            # tqdm 进度条，直观看到当前页进度
            for item in tqdm(items, desc=f"第{page}页"):
                spu_id = str(item["spuId"])   # 唯一商品编号
                if spu_id in all_spu:         # 已抓过就跳过
                    continue
                random_sleep()                # 随机睡 1~3 秒，别太快
                detail_rows = parse_detail(spu_id)  # 调详情接口
                if detail_rows:               # 抓到有效 SKU 才写文件
                    save_csv([
                        [r["spuId"], r["标题"], r["尺码"], r["价格"], r["规格JSON"], datetime.now()]
                        for r in detail_rows
                    ])
                    all_spu.add(spu_id)       # 记录已抓
                else:
                    logging.info(f"spuId={spu_id} 无有效 SKU，已跳过")
        except Exception as e:
            # 当前页出错时记录异常，稍等几秒继续下一页，防止整个脚本崩溃
            logging.exception(f"第{page}页出错：{e}")
            random_sleep(5, 10)
            continue

    # 全部完成后打印汇总
    logging.info(f"全部完成！已抓 {len(all_spu)} 双鞋，见 {SAVE_CSV}")


# --------------------  7.  入口 --------------------
if __name__ == "__main__":
    main()        # 只有当脚本被直接运行时才会执行 main()