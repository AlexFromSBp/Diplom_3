import allure

from locators import OrderPageLocators, MainPageLocators
from pages.base_page import BasePage
from data.user_data import email, password


class OrderFeed(BasePage):

    @allure.step("Переходим в ленту заказов")
    def click_switch_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликаем на последний заказ")
    def click_last_order(self):
        self.click_element(OrderPageLocators.LAST_ORDER)

    @allure.step("Наличие состава")
    def order_details(self):
        self.wait_to_visibility(OrderPageLocators.STRUCTURE)
        return self.get_element(OrderPageLocators.STRUCTURE)

    @allure.step("Авторизация")
    def login(self):
        self.click_element(MainPageLocators.BUTTON_AUTH_ACCOUNT)
        self.send_keys_to_input(MainPageLocators.MAIL_INPUT, email)
        self.send_keys_to_input(MainPageLocators.PASSWORD_INPUT, password)
        self.click_element(MainPageLocators.BUTTON_ENTER)

    @allure.step("Перетаскиваем в заказ 'Флюоресцентную булку'")
    def drag_and_drop_ingredient_fluorescent_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.INGREDIENT_BASKET)

    @allure.step("Тап 'Оформить заказ'")
    def click_on_checkout_button(self):
        self.wait_to_clickable(MainPageLocators.CHECKOUT_BUTTON)
        self.click_element(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        return self.wait_for_text_update(OrderPageLocators.ORDER_NUMBER)

    @allure.step("Закрываем окно с номером заказа")
    def close_popup_order_number(self):
        self.wait_to_clickable(OrderPageLocators.CLOSE_POPUP_NUMBER_ORDER)
        self.click_element(OrderPageLocators.CLOSE_POPUP_NUMBER_ORDER)

    @allure.step("Получаем список заказов")
    def get_orders_numbers(self):
        self.wait_to_visibility(OrderPageLocators.CONTAINER)
        order_elements = self.get_elements(OrderPageLocators.ORDER_ITEM)
        order_numbers = []
        for order in order_elements:
            order_numbers.append(order.text)
        return order_numbers

    @allure.step("Получаем количество оформленных заказов за все время")
    def get_all_orders(self):
        self.wait_to_visibility(OrderPageLocators.ALL_ORDERS_COUNT)
        return self.read_text(OrderPageLocators.ALL_ORDERS_COUNT)

    @allure.step("Переходим в раздел  'Конструктор'")
    def click_constructor_button(self):
        self.wait_to_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Количество заказов сегодня")
    def get_count_today(self):
        self.wait_to_visibility(OrderPageLocators.COUNT_ORDERS_TODAY)
        return self.read_text(OrderPageLocators.COUNT_ORDERS_TODAY)

    @allure.step("Ожидаем количество заказов за сегодня")
    def new_get_count_today(self):
        return self.wait_for_text_update(OrderPageLocators.COUNT_ORDERS_TODAY)

    @allure.step("Получаем номер заказа в разделе 'В работе'")
    def get_order_number_in_progress(self):
        return self.wait_for_text_update(OrderPageLocators.IN_PROGRESS)
