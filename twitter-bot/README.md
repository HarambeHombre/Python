# Internet Speed Twitter Bot - ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

**Internet Speed Twitter Bot** is a Python project designed to measure your internet speed using the Xfinity speed test and tweet the results on Twitter. This script uses Selenium for web automation and allows the user to track their upload and download speeds.

---

## Features

- Automates internet speed testing through the Xfinity speed test site.
- Extracts download and upload speed results.
- Logs into Twitter and posts the speed results automatically.

---

## Requirements

Before running this script, ensure the following:

1. **Python Installation**: Python 3.8 or higher is recommended.
2. **Selenium Installation**: Install the Selenium library using:
   ```bash
   pip install selenium
   ```
3. **WebDriver**: Download the appropriate WebDriver for Chrome from `ChromeDriver` and ensure it's accessible in your PATH.
4. **Twitter Credentials**: Update the script with your Twitter email and password:
  - Replace `TWITTER_EMAIL` and `TWITTER_PASSWORD` with your credentials.
  - If required, add a variable for `TWITTER_USERNAME`.

---

## Setup
1. Clone or download this repository to your local machine.
2. Install required libraries using `pip`:
```bash
  pip install selenium
```
3. Download the `ChromeDriver` and place it in the same directory as the script or add it to your system's PATH.

---

## Usage
### Step 1: Run the Script
Execute the Python script:
```bash
python main.py
```

Step 2: Internet Speed Test
- The script will open the Xfinity speed test website and start the speed test automatically.
- Extracted download and upload speeds will be retrieved.

Step 3: Tweet the Results
- The script logs into Twitter using your credentials.
- It tweets the speed results in the format:
```bash
  My download speed is: {down}, and my upload speed is: {up}. Not too bad!
```

---

## Example Output
Here’s an example of a Twitter post generated by the script:
```bash
My download speed is: 115 Mbps, and my upload speed is: 9 Mbps. Not too bad!
```

---

## Code Overview
### Import Libraries
The script starts by importing the necessary Python libraries:
```bash
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
```

### Define the Class
The `InternetSpeedTwitterBot` class contains two main methods:
1. `get_internet_speed()`: Measures download and upload speeds.
2. `tweet_at_provider(up, down)`: Logs into Twitter and posts the speed results.

---

## Notes
- **Browser Automation**: Ensure the version of `ChromeDriver` matches your installed Chrome browser.
- **Login Credentials**: Replace placeholder variables like `TWITTER_EMAIL`, `TWITTER_PASSWORD`, and `TWITTER_USERNAME` with real values.
- **Internet Speed Variability**: Results depend on the speed test website and your current internet connection.



