import time

from logger import logger
from pages.LoginPage import LoginPageHelper
from settings import USER_MAIL, USER_PASS

log = logger.setup_applevel_logger(file_name='app_debug.log')


def test_login(browser):
    log.info("start collector")
    login_page = LoginPageHelper(browser)
    login_page.go_to_site()
    login_page.setLogin(USER_MAIL)
    login_page.setPass(USER_PASS)
    login_page.setTerms()
    login_page.loginClick()

    log.info("finish collector")


# def test_login2(browser):
#     log.info("start collector")
#     login_page = LoginPageHelper(browser)
#     login_page.go_to_site()
#     time.sleep(15)
#     log.info("finish collector")
