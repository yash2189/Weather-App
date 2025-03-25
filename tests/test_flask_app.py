import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_setup")
class TestClassWeatherUI:
    @pytest.mark.ui
    def test_title(self):
        self.driver.get("http://localhost:5000/")
        self.driver.implicitly_wait(50)
        assert self.driver.title == "Weather App"

    @pytest.mark.ui
    def test_city_weather(self):
        self.driver.get("http://localhost:5000/")
        self.driver.find_element(By.XPATH, "//input[@class='input']").send_keys(
            "Washington"
        )
        self.driver.find_element(By.XPATH, "//button[@class='button is-info']").click()
        assert self.driver.find_element(
            By.XPATH, "//span[contains(text(),'Washington, ')]"
        )

    @pytest.mark.ui
    def test_empty_city_weather(self):
        self.driver.get("http://localhost:5000/")
        self.driver.find_element(By.XPATH, "//button[@class='button is-info']").click()
        assert self.driver.find_element(
            By.XPATH, "//h1[contains(text(),'City is Required')]"
        )

    @pytest.mark.ui
    def test_incorrect_city_weather(self):
        self.driver.get("http://localhost:5000/")
        self.driver.find_element(By.XPATH, "//input[@class='input']").send_keys(
            "x123jb"
        )
        self.driver.find_element(By.XPATH, "//button[@class='button is-info']").click()
        assert self.driver.find_element(
            By.XPATH, "// h1[contains(text(), 'Internal Server Error')]"
        )
