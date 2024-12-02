import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Type of browser. Default is chrome."
    )

@pytest.fixture(scope="class")
def browser(request):
    browser_type = request.config.getoption("--browser")
    if browser_type == "chrome":
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")
    
    request.cls.driver = driver  # Attach driver to the test class instance
    yield
    driver.quit()
