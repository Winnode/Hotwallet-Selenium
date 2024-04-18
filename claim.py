from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_chrome_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36")
    return options

def automate_wallet(account_phrase):
    options = get_chrome_options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
    try:
        driver.get('https://my.herewallet.app/auth/import/backup')
        account_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[2]/label/textarea')))
        account_input.send_keys(account_phrase)
        proceed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[3]/button')))
        proceed_button.click()
        
        time.sleep(25)
        driver.execute_script("window.open('https://my.herewallet.app/hot');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(10)
        
        if click_button_in_iframe(driver, "Check NEWS"):
            log_message("Clicked 'Check NEWS' button successfully.", bcolors.OKGREEN)
        
        driver.get('https://my.herewallet.app/hot')
        time.sleep(5)
        
        if click_button_in_iframe(driver, "Claim HOT", skip_if_not_clickable=True):
            log_message("Clicked 'Claim HOT' button successfully.", bcolors.OKGREEN)
        else:
            log_message("'Claim HOT' button was not clickable at this time, skipped.", bcolors.WARNING)
        
    except (WebDriverException, TimeoutException) as e:
        log_message(f"Error occurred: {e}", bcolors.FAIL)
        return False
    finally:
        driver.quit()
    return True

def click_button_in_iframe(driver, button_text, skip_if_not_clickable=False):
    frames = driver.find_elements(By.TAG_NAME, "iframe")
    for frame in frames:
        driver.switch_to.frame(frame)
        try:
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{button_text}')]"))
            )
            driver.execute_script("arguments[0].click();", button)
            driver.switch_to.default_content()
            return True
        except Exception as e:
            if skip_if_not_clickable:
                log_message(f"Button '{button_text}' not clickable, skipping.", bcolors.WARNING)
                driver.switch_to.default_content()
                return False
            else:
                log_message(f"Not found in this iframe: {e}", bcolors.FAIL)
        driver.switch_to.default_content()
    return False

def log_message(message, color=bcolors.OKBLUE):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"{bcolors.BOLD}{current_time}{bcolors.ENDC} {color}{message}{bcolors.ENDC}")

def main():
    print(bcolors.HEADER + "========================================")
    print("          Winnode Automation Hot Wallet         ")
    print("========================================" + bcolors.ENDC)
    try:
        with open('accounts.txt', 'r') as file:
            accounts = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        log_message("The accounts.txt file was not found.", bcolors.FAIL)
        return
    except Exception as e:
        log_message(f"An error occurred while reading the accounts: {e}", bcolors.FAIL)
        return
    
    while True:
        account_number = 1
        for account in accounts:
            success = False
            while not success:
                log_message(f"--- Processing account #{account_number} ---", bcolors.OKBLUE)
                success = automate_wallet(account)
                if not success:
                    log_message("Session failed, trying again in 5 minutes...", bcolors.WARNING)
                    time.sleep(300)  
                log_message("--- Account Processing Completed ---\n", bcolors.OKBLUE)
            account_number += 1
            time.sleep(10)  
        log_message("Completed all accounts. Waiting for 1 hour before restarting.", bcolors.OKGREEN)
        time.sleep(3600)  

if __name__ == '__main__':
    main()
