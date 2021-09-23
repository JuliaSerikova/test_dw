import time

from logger import logger
from pages.LoginPage import LoginPageHelper
from settings import USER_MAIL, USER_PASS, ITERS_BY_THREAD

log = logger.setup_applevel_logger(file_name='app_debug.log')


def step_login(browser, i):
    log.info("start one user. iteration " + str(i))
    login_page = LoginPageHelper(browser)
    browser.delete_all_cookies()
    login_page.go_to_site()
    log.info("go to url is ok. iteration " + str(i))
    login_page.setLogin(USER_MAIL)
    login_page.setPass(USER_PASS)
    login_page.setTerms()
    login_page.loginClick()
    log.info("login is ok. iteration " + str(i))
    login_page.jupiterClick() #для след кнопки //div/div/a

    log.info("click btn jupiter is ok. iteration " + str(i))
    log.info("finish one user. iteration " + str(i))


def test_thread1(browser):
    for i in range(ITERS_BY_THREAD):
        step_login(browser, i)


def test_thread2(browser):
    for i in range(ITERS_BY_THREAD):
        step_login(browser, i)


def test_thread3(browser):
    for i in range(ITERS_BY_THREAD):
        step_login(browser, i)


def test_thread4(browser):
    for i in range(ITERS_BY_THREAD):
        step_login(browser, i)


def test_thread5(browser):
    for i in range(ITERS_BY_THREAD):
        step_login(browser, i)
