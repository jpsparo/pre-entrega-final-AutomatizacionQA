from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.LoginPage import LoginPage


def iniciar_sesion(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    login.hacer_login(
        "standard_user",
        "secret_sauce"
    )

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )