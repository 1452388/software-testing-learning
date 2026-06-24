# ============================================
# UI 自动化测试 - conftest.py
# 使用 Selenium + Pytest + Allure
# ============================================

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    """初始化浏览器驱动"""
    options = Options()
    options.add_argument("--headless")          # 无头模式
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """被测网站URL"""
    return "https://example.com"


# ========== 自定义断言 ==========

def assert_element_text(element, expected_text):
    """断言元素文本内容"""
    actual = element.text
    assert expected_text in actual, f"期望: {expected_text}, 实际: {actual}"


def assert_page_title(driver, expected_title):
    """断言页面标题"""
    assert expected_title in driver.title, f"期望: {expected_title}, 实际: {driver.title}"
