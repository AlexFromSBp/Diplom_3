import allure
from data.user_data import email, password
from locators import ResetPageLocators
from pages.base_page import BasePage


class PasswordPage(BasePage):

    @allure.step("Тап по кнопке 'Личный кабинет'")
    def lk_click(self):
        self.click_element(ResetPageLocators.LK_BUTTON)

    @allure.step("Тап по кнопке 'Восстановить пароль'")
    def recovery_password_click(self):
        self.click_element(ResetPageLocators.RECOVERY_PASSWORD)

    @allure.step("Вводим email")
    def email_input(self):
        self.send_keys_to_input(ResetPageLocators.MAIL_INPUT, email)

    @allure.step("Тап по кнопке 'Восстановить'")
    def click_recovery_button(self):
        self.click_element(ResetPageLocators.RESTORE_BUTTON)

    @allure.step("Ожидаем активацию кнопки 'Сохранить'")
    def wait_save_button(self):
        self.wait_to_visibility(ResetPageLocators.SAVE_PWD_BUTTON)

    @allure.step("Вводим новый пароль")
    def set_new_password(self):
        self.send_keys_to_input(ResetPageLocators.INPUT_NEW_PASSWORD, password)

    @allure.step("Тап на кнопку Показать/скрыть пароль")
    def click_visibility_icon(self) -> bool:
        self.click_element(ResetPageLocators.BUTTON_VISIBILITY_PASSWORD)
        return "visibility_off" in self.get_element_text(ResetPageLocators.BUTTON_VISIBILITY_PASSWORD)

    @allure.step("Проверка активности скрытия элемента")
    def check_visibility(self):
        self.wait_to_visibility(ResetPageLocators.SEARCH_ELEMENT)

    @allure.step("Получаем текущую страницу")
    def get_current_url(self):
        return self.driver.current_url
