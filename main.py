from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as cs


from myutils import (
    scrollBar
)
from input import (
    inputTemp, inputText, checkItem, submitResult
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


def getNextPage(b, url):
    global g_pageIndex
    b.get(url)
    print(f"[{g_pageIndex}]", "current page is...", PURPLE,
          "---", b.title, "---", ENDC, b.current_url)
    g_pageIndex += 1


def main():
    print(GREEN, "start up scraping...", ENDC)
    b.maximize_window()
    print(GREEN, "maxmized window size...", ENDC)
    getNextPage(b, "https://condition.nihon-u.ac.jp/Student")
    print(GREEN, "attempted login...", ENDC)
    login(b)
    print(GREEN, "login successful!!!", ENDC)
    print(GREEN, "fill in the all blank...", ENDC)
    inputTemp(b)
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
