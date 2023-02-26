import ezsheets
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


def clean(data: list[str]) -> list[str]:
    for i in data:
        if "" == i:
            data.remove(i)  # DOC: remove white space
        if re.search(r"[0-9]", i):
            i = i[:-1]  # DOC: remove percent signs from numbers

    return data


def make_id(student: str, assignment_number: int) -> str:
    return "grade" + student[-1] + str(assignment_number)


def main():
    # DOC: request spreadsheet using spreadsheet id and then select the spreadsheet object
    ss = ezsheets.Spreadsheet("1y_3KpN2XrG-snlt_Ldc1Q1RSgEiXFX51lYf5YSFuIPE")
    sh = ss[0]

    # DOC: collect the web broweser driver (firefox for me)
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    # NOTE: link to use (local file for me)
    link = "file:///home/marvel/Coding/carey/src/web/index.html"

    # DOC: access the link
    driver.get(link)

    # DOC: get, clean, and validate the data from the spreadsheet
    data = sh.getRows()

    data = list(map(clean, data))
    data.remove(data[0])

    # DOC: iterate through the data putting them in the gradebook
    for grades in data:
        student = grades.pop(0)  # DOC: get the student name
        for grade in range(len(grades)):
            id = make_id(student, grade)  # DOC: create the id and use it to select the correct text input

            text_box = driver.find_element(by=By.ID, value=id)

            text_box.send_keys(grades[grade])  # DOC: 'type' in the grade

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")  # DOC: submit the form

        submit_button.click()

    sleep(100) # DOC: wait for a few seconds to make sure everything went right before ending the session

    driver.quit()

if __name__ == "__main__":
    main()
