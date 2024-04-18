# **Winnode Hot Wallet Automation**
![test Interface](https://github.com/Winnode/Hotwallet-Selenium/blob/8c8a19b13cd9a8e0da5b60d23f4d8bd43410b424/screenshot.png "test")

This Python script utilizes Selenium and PyAutoGUI to automate the process of accessing a wallet application using seed phrases. It is particularly useful for scenarios where manual interaction is required to input the seed phrase and perform certain actions on the wallet interface.

## Requirements

- Python 3.x
- Selenium
- PyAutoGUI
- Chrome WebDriver

## **Overview**

This script automates interactions with the Winnode Hot Wallet using Selenium. It handles logging in with account phrases and performs tasks such as checking news and claiming rewards if available.

## **Features**

- **Automated Login**: Logs into the Winnode Hot Wallet using provided account phrases.
- **Task Automation**: Automatically checks news and attempts to claim rewards.
- **Resilience**: Retries operations on failure, ensuring robustness against network issues.

## **Prerequisites**

Ensure the following requirements are met before running the script:
- Python 3.8+
- Google Chrome
- Selenium
- webdriver-manager

## **Installation Instructions**

### **Windows:**

1. **Install Python**:
   - Download and install the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project directory.
   - Ensure to check 'Add Python to PATH' during the installation.

2. **Install Required Packages**:
   - Open Command Prompt and run:
     ```
     pip install selenium webdriver-manager
     ```

### **Linux:**

1. **Install Python and pip**:
   - Run in your terminal:
     ```
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Install Required Packages**:
   - In your terminal, run:
     ```
     pip3 install selenium webdriver-manager
     ```

3. **Clone the Repository** (Applicable to both Windows and Linux):
   - Use Git to clone the repository to your local machine:
     ```
     git clone https://github.com/Winnode/Hotwallet-Selenium.git
     cd Hotwallet-Selenium
     ```

4. **Prepare the `accounts.txt` File**:
   - Create a file named `accounts.txt` in the script directory.
   - Add your account phrases to this file, one per line.

## **Usage**

Run the script from a command prompt or terminal in the script's directory:

```bash
python main.py

Replace python with python3 on Linux if necessary.
```


## Give
- [Follow kami di Twitter](https://twitter.com/Winnode)
- [Follow kami di GitHub](https://github.com/Winnode)
