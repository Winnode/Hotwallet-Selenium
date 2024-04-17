from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
import pyautogui
import time

# Setup Chromedriver
chromedriver_path = r'.\chromedriver.exe'
service = Service(executable_path=chromedriver_path)
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")

def automate_wallet(seed_phrase):
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 20)
    try:
        driver.get('https://my.herewallet.app/auth/import/backup')
        
        # Fill the seed phrase
        seed_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[2]/label/textarea')))
        seed_input.send_keys(seed_phrase)
        
        # Click proceed button
        proceed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[3]/button')))
        proceed_button.click()
        
        time.sleep(40)
        driver.execute_script("window.open('https://my.herewallet.app/hot');")
        handles = driver.window_handles
        driver.switch_to.window(handles[1])

        # Wait for the page to load
        time.sleep(10)

        # Handling button clicks by image
        button_image_path_1 = r'.\1.png'
        button_image_path_2 = r'.\2.png'

        button_location_1 = pyautogui.locateCenterOnScreen(button_image_path_1, confidence=0.8)
        if button_location_1:
            pyautogui.click(button_location_1)
            print("Clicked first button. Tab may have opened.")
            handles = driver.window_handles
            if len(handles) > 1:
                driver.switch_to.window(handles[-1])
                driver.close()
                driver.switch_to.window(handles[0])

            driver.get('https://my.herewallet.app/hot')
            time.sleep(5)

        button_location_2 = pyautogui.locateCenterOnScreen(button_image_path_2, confidence=0.8)
        if button_location_2:
            pyautogui.click(button_location_2)
            print("Clicked second button.")
            time.sleep(20)
        else:
            print("Second button image not found on screen.")
        
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

def main():
    try:
        with open('seed_key.txt', 'r') as file:
            seed_keys = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("The seed_key.txt file was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the seed keys: {e}")
        return
    
    while True:
        for seed_key in seed_keys:
            automate_wallet(seed_key)
        print("Completed all seed keys. Waiting for 1 hour before restarting.")
        time.sleep(3600)  # Wait for one hour

if __name__ == '__main__':
    main()
