import requests
import time
import random
import json
import re
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging
from urllib.parse import urlencode, urljoin

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DeWuShoeSpider:
    def __init__(self):
        # 初始化session，维持会话状态
        self.session = self._create_session()
        # 初始化UserAgent池
        self.ua = UserAgent()
        # 基础请求头，模拟真实浏览器
        self.base_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://www.dewu.com/',  # 添加来源页，模拟从首页跳转
        }
        # 随机延迟范围（模拟用户浏览时间）
        self.min_delay = 3
        self.max_delay = 8
        # 已爬取的URL集合，用于去重
        self.crawled_urls = set()
        # 先访问首页初始化会话
        self._init_session()

    def _create_session(self):
        """创建带重试机制的session"""
        session = requests.Session()

        # 设置重试策略
        retry_strategy = Retry(
            total=3,
            backoff_factor=2,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"]
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        # 设置超时时间
        session.timeout = 20

        return session

    def _init_session(self):
        """先访问首页，获取有效cookie和会话状态"""
        try:
            logger.info("初始化会话，访问得物首页")
            self._simulate_user_behavior()

            response = self.session.get(
                url='https://www.dewu.com/',
                headers=self._get_random_headers(),
                verify=False,
                allow_redirects=True
            )
            response.raise_for_status()
            logger.info("会话初始化成功")

        except Exception as e:
            logger.error(f"会话初始化失败: {str(e)}")

    def _get_random_headers(self):
        """生成随机请求头，模拟不同浏览器"""
        headers = self.base_headers.copy()
        headers['User-Agent'] = self.ua.random
        return headers

    def _simulate_user_behavior(self):
        """模拟用户浏览行为，添加随机延迟"""
        delay = random.uniform(self.min_delay, self.max_delay)
        logger.info(f"模拟用户浏览，延迟 {delay:.2f} 秒")
        time.sleep(delay)

    def get_shoe_list_urls(self, keyword="运动鞋", max_pages=3, proxy=None):
        """
        通过搜索接口获取运动鞋商品详情页URL（替代直接访问分类页）
        :param keyword: 搜索关键词
        :param max_pages: 要爬取的最大页数
        :param proxy: 代理IP
        :return: 商品详情页URL列表
        """
        all_detail_urls = []
        # 得物的搜索接口（核心修正点）
        search_api = "https://www.dewu.com/api/v2/search/products"

        for page in range(1, max_pages + 1):
            try:
                # 1. 模拟用户行为
                self._simulate_user_behavior()

                # 2. 构造搜索参数
                params = {
                    'keyword': keyword,
                    'page': page,
                    'limit': 30,  # 每页30条
                    'sort': 'sales',  # 按销量排序
                    'categoryId': 58390,  # 运动鞋分类ID
                    'currency': 'CNY'
                }

                logger.info(f"请求搜索接口第 {page} 页，关键词: {keyword}")

                # 3. 准备代理
                proxies = None
                if proxy:
                    proxies = {
                        'http': proxy,
                        'https': proxy
                    }

                # 4. 发送AJAX请求（模拟前端真实请求）
                response = self.session.get(
                    url=search_api,
                    params=params,
                    headers=self._get_random_headers(),
                    proxies=proxies,
                    verify=False
                )
                response.raise_for_status()

                # 5. 解析JSON响应
                data = response.json()

                # 6. 提取商品详情URL
                if data.get('code') == 200 and data.get('data'):
                    products = data['data'].get('products', [])
                    for product in products:
                        spu_id = product.get('spuId')
                        if spu_id:
                            # 构造详情页URL
                            detail_url = f"https://www.dewu.com/item/detail?spuId={spu_id}"

                            # 去重
                            if detail_url not in self.crawled_urls and detail_url not in all_detail_urls:
                                all_detail_urls.append(detail_url)
                                self.crawled_urls.add(detail_url)

                logger.info(f"第 {page} 页提取到 {len(products)} 个商品，去重后累计 {len(all_detail_urls)} 个")

                # 7. 分页间隔增加更长延迟
                if page < max_pages:
                    batch_delay = random.uniform(10, 20)
                    logger.info(f"分页间隔延迟 {batch_delay:.2f} 秒")
                    time.sleep(batch_delay)

            except Exception as e:
                logger.error(f"请求搜索接口第 {page} 页失败: {str(e)}")
                continue

        return all_detail_urls

    def get_shoe_detail(self, url, proxy=None):
        """
        获取鞋子详情页数据
        :param url: 商品详情页URL
        :param proxy: 代理IP
        :return: 商品详情字典
        """
        try:
            # 1. 模拟用户行为 - 随机延迟
            self._simulate_user_behavior()

            # 2. 准备请求参数
            proxies = None
            if proxy:
                proxies = {
                    'http': proxy,
                    'https': proxy
                }

            # 3. 发送请求
            logger.info(f"开始爬取详情页: {url}")
            response = self.session.get(
                url=url,
                headers=self._get_random_headers(),
                proxies=proxies,
                verify=False
            )

            # 4. 状态码检查
            response.raise_for_status()

            # 5. 解析响应
            html = response.text
            start_marker = 'window.__INITIAL_STATE__='
            end_marker = ';</script>'

            if start_marker in html:
                # 提取JSON数据
                start_idx = html.index(start_marker) + len(start_marker)
                end_idx = html.index(end_marker, start_idx)
                json_str = html[start_idx:end_idx]

                # 解析JSON
                data = json.loads(json_str)

                # 提取核心商品信息
                shoe_info = self._extract_core_info(data)
                # 添加商品URL
                shoe_info["商品URL"] = url
                return shoe_info
            else:
                logger.error(f"{url} - 未找到商品数据，可能反爬机制触发")
                return None

        except requests.exceptions.RequestException as e:
            logger.error(f"{url} - 请求失败: {str(e)}")
            return None
        except json.JSONDecodeError as e:
            logger.error(f"{url} - JSON解析失败: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"{url} - 爬取异常: {str(e)}")
            return None

    def _extract_core_info(self, data):
        """提取核心商品信息"""
        try:
            product_data = None

            # 尝试不同的数据路径（兼容得物不同页面结构）
            paths = [
                ['goods', 'detail', 'product'],
                ['product', 'info'],
                ['detail', 'product'],
                ['pageData', 'product']
            ]

            for path in paths:
                temp = data
                try:
                    for key in path:
                        temp = temp[key]
                    product_data = temp
                    break
                except KeyError:
                    continue

            if not product_data:
                return {"error": "未找到商品核心数据"}

            # 提取关键信息
            core_info = {
                "商品ID": product_data.get('id', ''),
                "商品名称": product_data.get('name', ''),
                "商品标题": product_data.get('title', ''),
                "品牌": product_data.get('brand', {}).get('name', ''),
                "售价": product_data.get('price', {}).get('salePrice', ''),
                "原价": product_data.get('price', {}).get('originalPrice', ''),
                "商品分类": product_data.get('category', {}).get('name', ''),
                "评分": product_data.get('evaluate', {}).get('score', ''),
                "销量": product_data.get('sales', {}).get('salesCount', ''),
                "产地": product_data.get('productionPlace', ''),
                "上市时间": product_data.get('marketTime', ''),
                "商品材质": product_data.get('material', ''),
                "货号": product_data.get('sku', ''),
                "款式": product_data.get('style', '')
            }

            return core_info

        except Exception as e:
            logger.error(f"提取数据失败: {str(e)}")
            return {"error": f"提取数据失败: {str(e)}"}

    def batch_crawl(self, url_list, proxy=None, save_to_file=True):
        """
        批量爬取多个商品详情页
        :param url_list: 商品详情页URL列表
        :param proxy: 代理IP
        :param save_to_file: 是否保存到JSON文件
        :return: 结果列表
        """
        results = []
        success_count = 0
        fail_count = 0

        logger.info(f"开始批量爬取，共 {len(url_list)} 个商品")

        for i, url in enumerate(url_list):
            logger.info(f"正在爬取第 {i + 1}/{len(url_list)} 个商品")
            result = self.get_shoe_detail(url, proxy)

            if result and "error" not in result:
                results.append(result)
                success_count += 1
            else:
                fail_count += 1

            # 批量爬取间隔延迟
            if i < len(url_list) - 1:
                batch_delay = random.uniform(8, 15)
                logger.info(f"批量爬取间隔，延迟 {batch_delay:.2f} 秒")
                time.sleep(batch_delay)

        logger.info(f"批量爬取完成 - 成功: {success_count}, 失败: {fail_count}")

        # 保存到文件
        if save_to_file and results:
            filename = f"dewu_shoes_{int(time.time())}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            logger.info(f"爬取结果已保存到: {filename}")

        return results


# ------------------- 修正后的使用示例 -------------------
if __name__ == "__main__":
    # 创建爬虫实例
    spider = DeWuShoeSpider()

    # 1. 通过搜索接口获取运动鞋商品详情URL（核心修正）
    # 关键词可以替换为"篮球鞋"、"跑步鞋"等
    detail_urls = spider.get_shoe_list_urls(keyword="运动鞋", max_pages=2)
    logger.info(f"共获取到 {len(detail_urls)} 个商品详情页URL")

    # 打印获取到的URL示例
    if detail_urls:
        logger.info(f"URL示例: {detail_urls[:3]}")

    # 2. 批量爬取详情页数据并保存到JSON文件
    if detail_urls:
        results = spider.batch_crawl(detail_urls)

        # 打印爬取结果示例
        if results:
            print("\n爬取结果示例：")
            print(json.dumps(results[0], ensure_ascii=False, indent=2))
    else:
        logger.warning("未获取到任何商品详情页URL")