import allure
import random
import string
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ищем элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ждем появление элемента")
    def wait_element_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ждем когда элемент исчезнет")
    def wait_not_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Нажимаем на элемент")
    def click_on_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Получаем текст из локатора")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Получаем урл странички на которой находимся")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Вводим символы/текст")
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_user_data():
        email = BasePage.generate_random_string(6) + '@yandex.ru'
        password = BasePage.generate_random_string(10)
        name = BasePage.generate_random_string(10)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload

    @allure.step("Ищем все элементы локатора ")
    def find_all(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)
