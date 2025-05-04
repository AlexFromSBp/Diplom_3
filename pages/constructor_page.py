import allure
from locators import MainPageLocators
from pages.base_page import BasePage
from data.user_data import email, password


class ConstructorPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_auth_button(self):
        auth_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_AUTH_ACCOUNT),
            "Кнопка авторизации не стала кликабельной за 10 секунд"
        )
        auth_button.click()

        self.wait.until(
            lambda d: "login" in d.current_url.lower(),
            "Не произошел переход на страницу логина после клика"
        )
        return self

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход тапом на 'Лента заказов'")
    def click_switch_order_feed(self):
        feed_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON),
            "Кнопка ленты заказов не найдена или не кликабельна"
        )
        feed_button.click()

        self.wait.until(
            lambda d: "feed" in d.current_url.lower(),
            "Не произошел переход в ленту заказов"
        )
        return self

    @allure.step("Кликаем ингредиент 'Флюоресцентная булка R2-D3'")
    def click_ingredient_fluorescent_bun(self):
        self.click_element(MainPageLocators.FLUORESCENT_BUN)

    @allure.step("Поиск элемента 'Детали ингредиента'")
    def get_ingredient_window(self):
        self.wait_to_visibility(MainPageLocators.INGREDIENT_WINDOW)
        return self.get_element(MainPageLocators.INGREDIENT_WINDOW)

    @allure.step("Закрываем окно 'Детали ингредиента'")
    def click_close_ingredient_window(self):
        self.click_element(MainPageLocators.EXIT_INGREDIENT_WINDOW)
        self.wait_to_invisibility(MainPageLocators.INGREDIENT_WINDOW)

    @allure.step("Получаем счётчик ингредиентов")
    def get_ingredient_counter(self):
        return int(self.read_text(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Перемещаем в заказ 'Флюоресцентную булку'")
    def drag_and_drop_ingredient_fluorescent_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.INGREDIENT_BASKET)

    @allure.step("Тап 'Оформить заказ'")
    def click_on_checkout_button(self):
        self.click_element(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step("Авторизация")
    def login(self):
        self.click_element(MainPageLocators.BUTTON_AUTH_ACCOUNT)
        self.send_keys_to_input(MainPageLocators.MAIL_INPUT, email)
        self.send_keys_to_input(MainPageLocators.PASSWORD_INPUT, password)
        self.click_element(MainPageLocators.BUTTON_ENTER)

    @allure.step("Заказ начали готовить")
    def order_is_being_prepared(self):
        self.wait_to_visibility(MainPageLocators.ORDER_PREPARED)
        return self.get_element(MainPageLocators.ORDER_PREPARED)
