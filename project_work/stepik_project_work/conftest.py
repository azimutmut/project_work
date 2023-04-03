# import pytest
# from selenium import webdriver
#
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default=None,
#                      help="Choose browser: chrome or firefox")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#


#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.mark.parametrize('language', [ "en"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")





# import pytest
# from selenium import webdriver
#
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default=None,
#                      help="Choose browser: chrome or firefox")
#     parser.addoption('--language', action='store', default='en', help='Language')
#
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     user_language= request.config.getoption("language")
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         options = Option()
#         options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#         browser = webdriver.Chrome(options=options)
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         fp= webdriver.FirefoxProfile()
#         fp.set_preference('intl.accept_languages', user_language)
#         browser= webdriver.Firefox(firefox_profile=fp)
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()




# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def pytest_addoption(parser):
#     parser.addoption('--language', action= 'store', default='en')
#
# @pytest.fixture(scope="function")
# def browser(request):
#     print("\nstart browser for test..")
#     user_language= request.config.getoption("language")
#     options = Option()
#     options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#     browser = webdriver.Chrome(options=options)
#     yield [user_language,browser]
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.mark.parametrize('language', [ "en"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")

