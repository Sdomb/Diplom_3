import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.password_recovery_locators import PersonalAccount as lk


class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль")
    @allure.description("Проверяем работу кнопки «Восстановить пароль»")
    def test_tap_on_btn_recovery_page(self, password_recovery, driver):

        password_recovery.go_to_personal_account()
        password_recovery.tap_and_wait_recovery_button()
        assert driver.find_element(*lk.RECOVERY_PASS_HEADER)

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description("Проверяем работу кнопки «Восстановить»")
    def test_input_email_and_tap_on_recovery_btn(self, password_recovery, driver):

        password_recovery.go_to_personal_account()
        password_recovery.tap_and_wait_recovery_button()
        password_recovery.input_email_and_push_recovery_btn()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(lk.PASSWORD_INPUT))

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    @allure.description("Проверяем что после клика по иконке глаза инпут пароля подсвечивается")
    def test_tap_pass_visible_button(self, password_recovery, driver):

        password_recovery.go_to_personal_account()
        password_recovery.tap_and_wait_recovery_button()
        password_recovery.input_email_and_push_recovery_btn()
        password_recovery.find_pass_input_and_enter_pass()

        assert password_recovery.click_on_eye_icon()
