"""
File: webcrawler.py
Name: Zoe Lai
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)

        driver = webdriver.Chrome()

        driver.get('https://www.ssa.gov/oact/babynames/decades/names' + year + '.html')
        try:
            element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        # Get the entire HTML content of the page
        html = driver.page_source
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        total_male = 0
        total_female = 0

        tbody_tags = soup.find_all('tbody')
        for tbody_tag in tbody_tags:
            tr_tags = tbody_tag.find_all('tr')
            for tr_tag in tr_tags:
                td_tags = tr_tag.find_all('td')
                row = [td_tag.text for td_tag in td_tags]
                if len(row) == 5:   # exclude last line (not baby data)
                    total_male += int(row[2].replace(',', ''))
                    total_female += int(row[4].replace(',', ''))

        # print output
        print('Male Number:', total_male)
        print('Female Number:', total_female)

        driver.quit()


if __name__ == '__main__':
    main()
