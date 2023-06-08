import time
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import selenium.webdriver.support.expected_conditions as EC
import undetected_chromedriver as uc

from terminalcolorpy import colored

# NOTE: To whoever is maintaining the program in the future, \ and \\ have caused issues. Do **not** include ':'.
ALL = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"""

INITIAL_PASSWORD_FIELD_XPATH = '//*[@id="riot-account"]/div/div[2]/div/div[2]/div[1]/div/div/input'
NEW_PASSWORD_FIELD_XPATH = '//*[@id="riot-account"]/div/div[2]/div/div[2]/div[2]/div/input'
CONFIRM_PASSWORD_FIELD_XPATH = '//input[@data-testid="password-card__confirmNewPassword"]'
CHANGE_PASSWORD_BUTTON = '//*[@id="riot-account"]/div/div[2]/div/div[3]/button[2]'

SIGN_IN_INPUT_XPATH = "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/input"
SIGN_IN_INPUT_FIELD_FOR_NAME_XPATH = "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/input"
SIGN_IN_INPUT_FIELD_FOR_PASSWORD_XPATH = "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/input"
SIGN_IN_PAGE_LOGIN_BUTTON = "/html/body/div[2]/div/div/div[2]/div/div/button"

LOGIN_ELEMENT_CHECK_SUCCESS_XPATH = '//*[@id="riot-account"]/div/div[2]/div/div[2]/div[1]/div/div/input'
TWOFA_REQUIRED_XPATH = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/h5[1]'


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
    print(colored("[INFO]", "#808080"), "Process started for", rf"{username}")
    print(colored("[INFO]", "#808080"), "The old password is", rf"{initial_password}")
    print(
        colored("[INFO]", "#808080"),
        "The new password is",
        rf"{colored(new_password, 'blue')}",
    )

    # Driver initialization
    # We initialize a new driver each time because of safety and the fact that this program is a batch login process
    driver = uc.Chrome(version_main=114)
    driver.maximize_window()
    driver.get("https://account.riotgames.com/en/log-in/")  # direct sign-in/log-in page

    WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                SIGN_IN_INPUT_XPATH,
            )
        )
    )

    driver.find_element(By.XPATH, SIGN_IN_INPUT_FIELD_FOR_NAME_XPATH,).send_keys(username)
    driver.find_element(By.XPATH, SIGN_IN_INPUT_FIELD_FOR_PASSWORD_XPATH).send_keys(initial_password)
    driver.find_element(By.XPATH, SIGN_IN_PAGE_LOGIN_BUTTON).click()

    try:
        driver.find_element(By.XPATH, TWOFA_REQUIRED_XPATH)
        print(
            colored("[CRUCIAL]", "#ff7b00"),
            "Please go to your email and enter the required 2FA auth. You have 120 seconds."
        )
    except NoSuchElementException:
        pass

    try:
        WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    LOGIN_ELEMENT_CHECK_SUCCESS_XPATH,
                )
            )
        )  # check to see if a field from the page present. if not present indicates wrong credentials

    except TimeoutException:
        driver.quit()
        raise ValueError

    # Changing the password
    driver.find_element(By.XPATH, INITIAL_PASSWORD_FIELD_XPATH).send_keys(initial_password)
    driver.find_element(By.XPATH, NEW_PASSWORD_FIELD_XPATH).send_keys(new_password)
    driver.find_element(By.XPATH, CONFIRM_PASSWORD_FIELD_XPATH).send_keys(new_password)
    driver.find_element(By.XPATH, CHANGE_PASSWORD_BUTTON).click()

    print(colored("[INFO]", "#808080"), "Process finished.")
    time.sleep(10 + sleep_time)  # let the HTTP request (hopefully) go through
    driver.quit()
