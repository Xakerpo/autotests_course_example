from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://sbis.ru/")
    print("Открыта страница sbis.ru")

    contacts_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Контакты"))
    )
    contacts_link.click()
    print("Перешли в раздел 'Контакты'")

    tensor_banner = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor"))
    )
    tensor_banner.click()
    print("Кликнули по баннеру Тензор")

    driver.switch_to.window(driver.window_handles[1])
    print("Переключились на новую вкладку")

    assert "tensor.ru" in driver.current_url
    print("Открыт сайт tensor.ru")

    news_block = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Сила в людях')]"))
    )
    assert news_block.is_displayed()
    print("Блок новости 'Сила в людях' найден")

    more_details_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Сила в людях')]//a[@href='/about']"))
    )

    driver.execute_script("arguments[0].scrollIntoView();", more_details_link)

    more_details_link.click()
    print("Кликнули по ссылке 'Подробнее'")

    WebDriverWait(driver, 10).until(EC.url_to_be("https://tensor.ru/about"))
    assert driver.current_url == "https://tensor.ru/about"
    print("Открыта страница https://tensor.ru/about")

finally:
    driver.quit()
    print("Браузер закрыт")