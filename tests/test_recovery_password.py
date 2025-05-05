import allure

from pages.password_page import PasswordPage
from data.urls import Urls


class TestRecoveryPassword:

    @allure.title("Переход по кнопке 'Восстановить пароль'")
    def test_button_password_recovery(self, driver):
        test = PasswordPage(driver)
        test.lk_click()
        test.recovery_password_click()
        assert test.current_url() == Urls.FORGOT_PAGE

    @allure.title("Переход на страницу обновления пароля")
    def test_enter_mail_click_restore_button(self, driver):
        test = PasswordPage(driver)
        test.lk_click()
        test.recovery_password_click()
        test.email_input()
        test.click_recovery_button()
        test.wait_save_button()
        assert test.current_url() == Urls.RESET_PAGE

    @allure.title("Клик по кнопке Показать/скрыть пароль активирует поле")
    def test_click_button_invisibility_button(self, driver):
        password_page = PasswordPage(driver)
        password_page.lk_click()
        password_page.recovery_password_click()
        password_page.email_input()
        password_page.click_recovery_button()
        password_page.wait_save_button()
        password_page.set_new_password()
        password_page.click_visibility_icon()

        assert password_page.check_visibility()