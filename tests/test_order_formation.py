import allure
from data.urls import Urls
from pages.constructor_page import ConstructorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestConstructor:

    @allure.title("Успешное открытие страницы 'Конструктор' тапом по странице")
    def test_click_on_constructor(self, driver):
        test = ConstructorPage(driver)
        test.click_auth_button()
        WebDriverWait(driver, 10).until(EC.url_contains("login"))
        constructor_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Конструктор')]"))
        )
        constructor_button.click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE, \
            f"Ожидался URL {Urls.MAIN_PAGE}, получен {driver.current_url}"

    @allure.title("Успешное открытие страницы  'Лента заказов' тапом по странице")
    def test_click_order_list(self, driver):
        test = ConstructorPage(driver)
        test.click_auth_button()
        test.click_switch_order_feed()
        assert test.current_url() == Urls.ORDER_FEED

    @allure.title("Проверка появления всплывающего окна с деталями при тапе на заказ")
    def test_get_order_popup(self, driver):
        test = ConstructorPage(driver)
        test.click_ingredient_fluorescent_bun()
        element = test.get_ingredient_window()
        assert element.is_displayed()

    @allure.title("Всплывающее окно закрывается нажатием крестика")
    def test_close_popup_window_click_cross(self, driver):
        test = ConstructorPage(driver)
        test.click_ingredient_fluorescent_bun()
        element = test.get_ingredient_window()
        test.click_close_ingredient_window()
        assert not element.is_displayed()

    @allure.title("При использовании ингредиента, увеличивается его счетчик")
    def test_counter_ingredient_increases(self, driver):
        test = ConstructorPage(driver)
        initial_count = test.get_ingredient_counter()
        test.drag_and_drop_ingredient_fluorescent_bun_to_order()
        new_count = test.get_ingredient_counter()
        assert new_count == initial_count + 2

    @allure.title("Успешное оформление заказа авторизованным пользователем")
    def test_logged_user_can_place_order(self, driver):
        test = ConstructorPage(driver)
        test.click_auth_button()
        test.login(email="test_practicum@ya.ru", password="qwerty")
        test.drag_and_drop_ingredient_fluorescent_bun_to_order()
        test.click_on_checkout_button()
        element = test.order_is_being_prepared()
        assert element.is_displayed()
