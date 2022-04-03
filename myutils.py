import random
from selenium.webdriver.common.by import By


def editTextByID(b, id, str):
    text = b.find_element(By.ID, id)
    text.clear()
    text.send_keys(str)


def clickElementByClass(b, className):
    element = b.find_element(By.CLASS_NAME, className)
    b.execute_script("arguments[0].click();", element)


def randFloat():
    ret = round(random.uniform(36.2, 36.8), 1)
    return ret


def scrollBar(b, px):
    b.execute_script(f"window.scrollTo(0, {px});")
