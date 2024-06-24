from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configuración del navegador
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')
options.add_argument(
    '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"')

# Ruta al chromedriver
webdriver_service = Service(
    'D:/Programas/chrome-win64/chromedriver-win64/chromedriver.exe')

# Crear una instancia del WebDriver
wd = webdriver.Chrome(service=webdriver_service, options=options)

try:
    # Navegar a Google
    wd.get("https://www.google.com/")

    # Esperar a que la página se cargue completamente
    WebDriverWait(wd, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Usar JavaScript para realizar la búsqueda
    search_term = "humai inteligencia artificial"
    wd.execute_script(
        f"document.querySelector('textarea[name=\"q\"]').value = '{search_term}';")
    wd.execute_script(
        "document.querySelector('form[role=\"search\"]').submit();")

    # Esperar a que los resultados de búsqueda se carguen
    WebDriverWait(wd, 20).until(
        EC.presence_of_element_located((By.ID, "search")))

    # Intentar aceptar el consentimiento de cookies
    try:
        accept_button = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Aceptar todo')]"))
        )
        accept_button.click()
        print("Consentimiento de cookies aceptado.")
    except Exception as e:
        print("No se encontró el botón de aceptar cookies o ya estaba aceptado:", str(e))

    # Esperar unos segundos para asegurar que la página se actualice después de aceptar las cookies
    time.sleep(5)

    # Tomar una captura de pantalla
    wd.save_screenshot('screenshot_google.png')

    print("Búsqueda realizada y captura de pantalla guardada con éxito.")

except Exception as e:
    print(f"Se produjo un error: {str(e)}")

finally:
    # Cerrar el WebDriver
    wd.quit()
