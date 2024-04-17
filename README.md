# Automated Wallet Access Script
![test Interface](https://github.com/Winnode/Hotwallet-Selenium/blob/8c8a19b13cd9a8e0da5b60d23f4d8bd43410b424/screenshot.png "test")

This Python script utilizes Selenium and PyAutoGUI to automate the process of accessing a wallet application using seed phrases. It is particularly useful for scenarios where manual interaction is required to input the seed phrase and perform certain actions on the wallet interface.

## Requirements

- Python 3.x
- Selenium
- PyAutoGUI
- Chrome WebDriver

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Winnode/Hotwallet-Selenium.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download and install the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project directory.

## Usage

1. Ensure that you have a `seed_key.txt` file in the project directory containing the seed phrases, with each seed phrase on a new line.

2. Run the script `claim.py`:

    ```bash
    python claim.py
    ```

3. The script will sequentially process each seed phrase from the `seed_key.txt` file, automating the process of entering the seed phrase and performing actions on the wallet interface.

4. After completing all seed phrases, the script will wait for one hour before restarting the process.

## Configuration

- The script uses image recognition to identify and click on certain buttons within the wallet interface. Make sure to replace the button images (`1.png`, `2.png`, etc.) in the project directory with appropriate images matching the buttons in your wallet interface.

- Adjust the timeouts and delays according to your system's performance and the speed of the wallet interface.

## Disclaimer

- Use this script responsibly and at your own risk. Ensure that you have proper authorization to automate interactions with the wallet application.

- The script is provided as-is, without any warranties or guarantees. The developers shall not be liable for any damages or losses resulting from the use of this script.

## Give
- [Follow kami di Twitter](https://twitter.com/Winnode)
- [Follow kami di GitHub](https://github.com/Winnode)
