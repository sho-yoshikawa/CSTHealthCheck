from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from myutils import editTextByID, randFloat, clickElementByClass

NOTHING = "特になし"

# inputYestData for click dismiss modal. bad code, sry...


def inputYestData(b):
    dismiss = b.find_element(By.XPATH, '//button[@data-dismiss="modal"]')
    b.execute_script("arguments[0].click();", dismiss)
    isConsent = b.find_element(By.ID, 'Is_Consent')
    b.execute_script("arguments[0].click();", isConsent)
    clickElementByClass(b, "ToNext")


def inputNormalTemp(b, temp):
    normalTemp = b.find_element(By.ID, 'Ent_Input_Temperature_Normal_String')
    normalTemp.clear()
    normalTemp.send_keys(temp)


def inputAMTemp(b):
    temp = randFloat()
    b.find_element(By.XPATH, '//option[@value="6"]').click()
    AMTemp = b.find_element(By.ID, 'Ent_Input_Temperature_1_String')
    AMTemp.clear()
    AMTemp.send_keys(temp)


def inputPMTemp(b):
    temp = randFloat()
    b.find_element(By.XPATH, '//option[@value="13"]').click()
    PMTemp = b.find_element(By.ID, 'Ent_Input_Temperature_2_String')
    PMTemp.clear()
    PMTemp.send_keys(temp)


def inputTemp(b, f_am, f_pm):
    inputNormalTemp(b, 35.8)
    if f_am and not f_pm:
        inputAMTemp(b)
        return
    if not f_am and f_pm:
        inputPMTemp(b)
        return
    inputAMTemp(b)
    inputPMTemp(b)


def inputText(b):
    editTextByID(b, "Ent_Input_Text_Etc", NOTHING)
    for i in range(1, 4):
        editTextByID(b, f"Ent_Input_Text_Behavior_{i}", NOTHING)
    editTextByID(b, "Ent_Input_Summary", NOTHING)


def checkItem(b):
    checkItemLen = 13
    for i in range(1, checkItemLen):
        b.find_element(By.ID, f"Check_{i}_N").click()


def submitResult(b):
    clickElementByClass(b, "btnRegist")
    Alert(b).accept()
    clickElementByClass(b, "btnSearch")
