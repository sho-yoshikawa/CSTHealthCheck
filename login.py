from selenium.webdriver.common.by import By
from myutils import editTextByID, clickElementByClass

from password import (
    ID, PASSWORD
)


def login(b):
    try:
        editTextByID(b, "No_Member_1", ID)
        editTextByID(b, "Birthday_String", PASSWORD)
        login = b.find_element(By.XPATH, '//input[@value="ログイン"]')
        b.execute_script("arguments[0].click();", login)
        dismiss = b.find_element(By.XPATH, '//button[@data-dismiss="modal"]')
        b.execute_script("arguments[0].click();", dismiss)
        isConsent = b.find_element(By.ID, 'Is_Consent')
        b.execute_script("arguments[0].click();", isConsent)
        clickElementByClass(b, "ToNext")
    except:
        print("login went wrong.")
