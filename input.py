from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from myutils import editTextByID, randFloat, clickElementByClass

NOTHING = "特になし"


def inputNormalTemp(b, temp):
    normalTemp = b.find_element(By.XPATH, f'//input[@value="{temp}"]')
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


def inputTemp(b):
    inputNormalTemp(b, 35.8)
    inputAMTemp(b)
    inputPMTemp(b)


def inputText(b):
    editTextByID(b, "Ent_Input_Text_Etc", NOTHING)
    for i in range(1, 4):
        editTextByID(b, f"Ent_Input_Text_Behavior_{i}", NOTHING)
    editTextByID(b, "Ent_Input_Summary", NOTHING)


def checkItem(b):
    checkItemLen = 12
    for i in range(1, checkItemLen):
        b.find_element(By.ID, f"Check_{i}_N").click()


def submitResult(b):
    clickElementByClass(b, "btnRegist")
    Alert(b).accept()
    clickElementByClass(b, "btnSearch")
