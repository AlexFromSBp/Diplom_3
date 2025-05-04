import allure

from data.user_data import email, password
from locators import ProfilePageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.title("Проверяем переход на страницу профиля")
    def click_lk(self):
        self.click_element(ProfilePageLocators.LK_BUTTON)

    @allure.title("Вводим логин")
    def set_login(self, email):
        self.send_keys_to_input(ProfilePageLocators.MAIL_INPUT, "email")

    @allure.title("Вводим пароль")
    def set_password(self, password):
        self.send_keys_to_input(ProfilePageLocators.PASSWORD_INPUT, "password")

    @allure.title("Клик по кнопке 'Войти'")
    def click_enter_button(self):
        self.click_element(ProfilePageLocators.BUTTON_ENTER)

    @allure.title("Ожидаем загрузку страницы профиля")
    def wait_account_page(self):
        self.wait_to_clickable(ProfilePageLocators.BUTTON_PROFILE)

    @allure.title("Тап по кнопке 'История заказов'")
    def click_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY)

    @allure.title("Тап по кнопке 'Выход'")
    def click_exit_button(self):
        self.click_element(ProfilePageLocators.EXIT_BUTTON)

    @allure.title("Ожидание загрузки страницы при выходе")
    def wait_logout_page(self):
        self.wait_to_clickable(ProfilePageLocators.BUTTON_ENTER)

    @allure.step("Получаем текущую страницу")
    def get_current_url(self):
        return self.driver.current_url
