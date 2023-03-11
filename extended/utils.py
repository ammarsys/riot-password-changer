import time
import random
import string

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


import selenium.webdriver.support.expected_conditions as EC
import undetected_chromedriver as uc

from terminalcolorpy import colored

# NOTE: To whoever is maintaining the program in the future, \ and \\ have caused issues. Do **not** include ':'.
ALL = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"""


def gen_sec_pass() -> str:
    return "".join(random.sample(ALL, 20))


def change_account_password(
    username: str, initial_password: str, new_password: str, sleep_time: int = 1
) -> None:
    """Generate a secure account password for the riot page.

    This function utilises the direct link for the sign-in page rather than the homepage (saves roughly 50% of the time
    it would take indirectly).
    """
    # Keep using fstrings here because of \ and \\. FR/RF flag
    print(colored("[INFO]", "#808080"), "Proces zapocet za", rf"{username}")
    print(colored("[INFO]", "#808080"), "Stara sifra je", rf"{initial_password}")
    print(
        colored("[INFO]", "#808080"),
        "Nova sifra je",
        rf"{colored(new_password, 'blue')}",
    )

    # Driver initialization

    driver = uc.Chrome(version_main=109)
    driver.maximize_window()
    driver.get("https://account.riotgames.com/en/log-in/")  # direct sign-in/log-in page

    WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/input",
            )
        )
    )  # check if sign-in input is present i.e. if the page is 100% loaded

    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/input",
    ).send_keys(
        username
    )  # sign-in input field for name

    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/input",
    ).send_keys(
        initial_password
    )  # sign-in input field for password

    driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/button"
    ).click()  # sign-in login button

    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="riot-account"]/div/div[2]/div/div[2]/div[1]/div/div/input',
                )
            )
        )  # check to see if a field from the page present. if not present indicates wrong credentials

    except TimeoutException:
        driver.quit()
        raise ValueError

    # Changing the password
    driver.find_element(
        By.XPATH, '//*[@id="riot-account"]/div/div[2]/div/div[2]/div[1]/div/div/input'
    ).send_keys(
        initial_password
    )  # initial password field on account managment page

    driver.find_element(
        By.XPATH, '//*[@id="riot-account"]/div/div[2]/div/div[2]/div[2]/div/input'
    ).send_keys(
        new_password
    )  # new password field

    driver.find_element(
        By.XPATH, '//input[@data-testid="password-card__confirmNewPassword"]'
    ).send_keys(
        new_password
    )  # confirm password field

    driver.find_element(
        By.XPATH, '//*[@id="riot-account"]/div/div[2]/div/div[3]/button[2]'
    ).click()  # change password now

    print(colored("[INFO]", "#808080"), "Proces zavrsen")
    time.sleep(10 + sleep_time)  # let the HTTP request (hopefully) go through
    driver.quit()
