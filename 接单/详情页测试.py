from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# 设置 Selenium 模式为无头模式（不打开浏览器窗口）
chrome_options = Options()
chrome_options.add_argument("--headless")  # 开启无头模式
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("start-maximized")

# 设置 Chrome 驱动路径
driver_path = r'D:\chromedriver-win64\chromedriver-win64\chromedriver.exe' # 请替换为你本地的 chromedriver 路径

# 使用 Service 来指定驱动路径
service = Service(executable_path=driver_path)

# 初始化 WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# 访问商品详情页
product_url = 'https://www.dewu.com/product-detail.html?sourceName=pc&spuId=18001883&propertyValueId=0&skuId=872081327'

driver.get(product_url)

# 显式等待，确保页面加载完成，等待商品标题加载
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'product-title'))  # 等待商品标题元素加载
    )
except:
    print("页面加载超时，商品标题未加载完成")

# 获取页面 HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 尝试获取商品名称，验证元素是否存在
name_element = soup.find('h1', class_='product-title')
if name_element:
    name = name_element.get_text(strip=True)  # 商品名称
    print(f"商品名称: {name}")
else:
    print("未找到商品名称")

# 尝试获取商品价格
price_element = soup.find('span', class_='product-price')
if price_element:
    price = price_element.get_text(strip=True)  # 商品价格
    print(f"商品价格: {price}")
else:
    print("未找到商品价格")

# 尝试获取商品规格
specs_element = soup.find('div', class_='product-specs')
if specs_element:
    specs = specs_element.get_text(strip=True)  # 商品规格
    print(f"商品规格: {specs}")
else:
    print("未找到商品规格")

# 截图，查看页面加载情况
driver.save_screenshot("screenshot.png")

# 关闭浏览器
driver.quit()