import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helper.config import web_url
from helper.test_management_integration import *


def pytest_html_report_title(report):
    report.title = "Report Selenium Python"


@pytest.fixture()
def open_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--window-size=1920, 1080")
    options.add_argument("--disable-web-security")
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


@pytest.fixture(scope='function', autouse=True)
def hook(request, open_driver):
    open_driver.get(web_url)
    get_error = request.session.testsfailed
    yield
    test_result = request.session.testsfailed - get_error
    marker = request.node.get_closest_marker("TestManagement")
    case_id = marker.args[0]

    if test_result == 0:
        push_result(case_id, "passed")
    else:
        push_result(case_id, "failed")

    open_driver.quit()


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    print("BEFORE SUITE")
    yield
    print("AFTER SUITE")
