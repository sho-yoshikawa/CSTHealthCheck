import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as cs


from myutils import (
    scrollBar
)
from input import (
    inputTemp, inputText, checkItem, submitResult, inputYestData
)
from login import login

PURPLE = '\033[35m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
ENDC = '\033[0m'
CHROMEDRIVER_PATH = "./chromedriver"

chrome_service = cs.Service(executable_path=CHROMEDRIVER_PATH)
b = webdriver.Chrome(service=chrome_service)

g_pageIndex = 1
f_am = False
f_pm = False
f_yest = False


def getNextPage(b, url):
    global g_pageIndex
    b.get(url)
    print(f"[{g_pageIndex}]", "current page is...", PURPLE,
          "---", b.title, "---", ENDC, b.current_url)
    g_pageIndex += 1


def checkArgs():
    global f_am
    global f_pm
    global f_yest
    if "am" in sys.argv:
        f_am = True
    elif "pm" in sys.argv:
        f_pm = True
    elif "yest" in sys.argv:
        f_yest = True


def main():
    global f_am, f_pm, f_yest
    if (len(sys.argv) > 0):
        print("check the arguments...")
        checkArgs()
    else:
        print("No arguments...")
    print(GREEN, "start up scraping...", ENDC)
    b.maximize_window()
    print("maxmized window size...")
    getNextPage(b, "https://condition.nihon-u.ac.jp/Student")
    login(b)
    print(GREEN, "login successful!!!", ENDC)
    print(f_am, f_pm, f_yest)
    if f_yest:
        getNextPage(
            b, "https://condition.nihon-u.ac.jp/Student/Consent/previou")
        inputYestData(b)
    print("attempted login...")
    print("fill in the all blank...")
    inputTemp(b, f_am, f_pm)
    scrollBar(b, 500)
    checkItem(b)
    scrollBar(b, 500)
    inputText(b)
    submitResult(b)
    print(GREEN, "infomation successfully registed!!!", ENDC)
    print("*** done ***")
    b.quit()


if __name__ == "__main__":
    main()
