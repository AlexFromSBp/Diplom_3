import allure

from pages.profile_page import ProfilePage
from data.urls import Urls
from data.user_data import email, password

class TestProfileAccount:

    @allure.title("Тап по кнопке 'Личный кабинет'")
    def test_switch_lk_button(self, driver):
        test = ProfilePage(driver)
        test.click_lk()
        test.set_login()
        test.set_password()
        test.click_enter_button()
        test.click_lk()
        test.wait_account_page()
        assert test.current_url() == Urls. PROFILE_PAGE

    @allure.title("Переход на вкладку 'История заказов'")
    def test_switch_order_history(self, driver):
        test = ProfilePage(driver)
        (test.click_lk()
         .set_login(login="test_practicum@ya.ru")
         .set_password("qwerty")
         .click_enter_button()
         .click_lk()
         .click_order_history())

        assert test.current_url() == Urls.HISTORY_PAGE

    @allure.title("Проверка выхода из аккаунта")
    def test_logout(self, driver):
        test = ProfilePage(driver)
        (test.click_lk()
         .set_login(email=email)
         .set_password(password=password)
         .click_enter_button()
         .click_lk()
         .click_exit_button()
         .wait_logout_page())
        assert test.current_url() == Urls.LOGIN_PAGE
