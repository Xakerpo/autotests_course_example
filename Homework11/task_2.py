# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import sleep

sbis_site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
user_login = 'retailmobile'
user_password = 'Test123'

try:
    print('Авторизоваться на сайте https://fix-online.sbis.ru/')
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(2)
    inputs = driver.find_elements(By.CSS_SELECTOR, '.controls-Field ')
    login, password = inputs
    login.send_keys(user_login, Keys.ENTER)
    sleep(2)
    password.send_keys(user_password, Keys.ENTER)

    print('Перейти в реестр Контакты')
    sleep(5)
    nav_contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa=Контакты]')
    nav_contacts.click()
    sleep(2)
    contacts = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__lvl-1')
    contacts.click()
    sleep(8)

    print('Отправить сообщение самому себе')
    add_message_btn = driver.find_element(By.CSS_SELECTOR, '[data-name=sabyPage-addButton]')
    add_message_btn.click()
    sleep(2)
    search_fields = driver.find_elements(By.CSS_SELECTOR, '.controls-Field')
    search_fields[0].send_keys('Иванова Анастасия Петровна', Keys.ENTER)
    sleep(2)
    user = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-selector__addressee')
    user.click()
    sleep(2)
    text_area = driver.find_element(By.CSS_SELECTOR, '.textEditor_slate_Field')
    text_area.send_keys('Задание 11')
    sleep(2)
    send_message_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa=msg-send-editor__send-button]')
    send_message_btn.click()

    print('Убедиться, что сообщение появилось в реестре')
    sleep(2)
    my_message = driver.find_elements(By.XPATH, ".//p[text()='Задание 11']")
    assert len(my_message) > 0, 'Сообщение не появилось'
    print('Удалить сообщение и убедиться что удалили')
    my_message[0].click()
    sleep(2)
    remove_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa=remove]')
    remove_btn.click()
    sleep(2)
    my_message = driver.find_elements(By.XPATH, ".//p[text()='Задание 11']")
    assert len(my_message) == 0, 'Сообщение не удалили'

finally:
    driver.quit()