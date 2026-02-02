from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
navigator = webdriver.Chrome(service=service)

navigator.get("https://www.youtube.com/")

navigator.find_element(By.XPATH, 
                       '//*[@id="center"]/yt-searchbox/div[1]/div/form/input').send_keys("Curso em vídeo")
navigator.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/button').click()

wait = WebDriverWait(navigator, 10)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//ytd-channel-renderer//a[@id="main-link"]')
)).click()

input("Pressione ENTER para fechar o navegador...")
navigator.quit()
