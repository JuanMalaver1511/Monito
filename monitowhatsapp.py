from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def enviar_mensaje_personalizado(numero, mensaje):
    try:
        options = Options()
        options.add_argument("--start-maximized")  # Para maximizar la ventana de Chrome
        driver = webdriver.Chrome(options=options)  # Inicializar el controlador de Chrome

        driver.get('https://web.whatsapp.com/')
        input("Presiona Enter después de escanear el código QR...")

        # Esperar a que aparezca el campo de búsqueda
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_2_1wd copyable-text selectable-text"]')))

        # Buscar el campo de búsqueda
        search_box = driver.find_element(By.XPATH, '//div[@class="_2_1wd copyable-text selectable-text"]')
        search_box.click()

        # Ingresar el número de teléfono
        search_box.send_keys(numero)
        sleep(2)

        # Seleccionar el chat
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//span[@title="{numero}"]')))
        chat = driver.find_element(By.XPATH, f'//span[@title="{numero}"]')
        chat.click()
        sleep(2)

        # Ingresar el mensaje personalizado
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_3FRCZ copyable-text selectable-text"]')))
        message_box = driver.find_element(By.XPATH, '//div[@class="_3FRCZ copyable-text selectable-text"]')
        message_box.click()
        message_box.send_keys(mensaje)

        # Enviar el mensaje
        message_box.send_keys(Keys.RETURN)
        sleep(2)

    except Exception as e:
        print(f"Error al enviar mensaje a {numero}: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()

def main():
    # Lista de números de teléfono a los que se enviarán los mensajes
    numeros = [
        "+573202594521",
        "+573202594521"
        # Agrega más números según sea necesario
    ]

    # Mensaje personalizado que se enviará
    mensaje = "¡Hola! Este es un mensaje personalizado."

    for numero in numeros:
        enviar_mensaje_personalizado(numero, mensaje)

if __name__ == "__main__":
    main()
