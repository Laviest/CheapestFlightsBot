from selenium import webdriver
from selenium.webdriver.common.by import By
from search.constants import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
import re



class FlightSearcher(webdriver.Chrome):
    def __init__(self, driver_path = r"C:/Users/Pero/Downloads/chromedriver_win32/chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-logging'])
        super(FlightSearcher, self).__init__(
            executable_path=r"C:/Users/Pero/Downloads/chromedriver_win32/chromedriver.exe", options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def first_page(self):
        self.get(BASE_URL)
        WebDriverWait(self, 2)

    def agree(self):
        agree_button = self.find_element(By.ID, "didomi-notice-agree-button")
        agree_button.click()

    def where_from(self, place):
        where_from_element = self.find_element(By.XPATH, '//input[contains(@class, "odf-input-m ")]')
        where_from_element.clear()
        where_from_element.send_keys(place)

        first_option = self.find_element(By.XPATH, '//li[contains(@class, "hover")]')
        first_option.click()

    def where_to(self, place):
        where_to_element = self.find_element(By.CSS_SELECTOR, 'input[placeholder="Where to?"]')
        where_to_element.clear()
        where_to_element.send_keys(place)

        first_option = self.find_element(By.XPATH, '//li[contains(@class, "hover")]')
        first_option.click()

    def check_in_and_out_date(self, check_in_or_out_month, day):
        check_in_or_out_month = str(check_in_or_out_month).strip().lower().capitalize()
        check_in_or_out_month.replace(" ", "")
        check_in_or_out_month = check_in_or_out_month + " '22"

        month_element = self.find_elements(By.XPATH, '//div[@class="odf-calendar-title"]')
        main_class_element = self.find_elements(By.XPATH, '//div[contains(@class, "odf-calendar-month")]')
        next_button_class = self.find_element(By.CSS_SELECTOR, 'span[glyph="arrow-right"]')

        if month_element[0].get_attribute('textContent') == check_in_or_out_month:
            main_class = main_class_element[0]
            all_days = main_class.find_elements(By.CLASS_NAME, 'odf-calendar-day')

        elif month_element[1].get_attribute('textContent') == check_in_or_out_month:
            main_class = main_class_element[1]
            all_days = main_class.find_elements(By.CLASS_NAME, 'odf-calendar-day')

        else:
            while month_element[1].get_attribute('textContent') != check_in_or_out_month:
                next_button_class.click()
                month_element = self.find_elements(By.XPATH, '//div[@class="odf-calendar-title"]')

            main_class = main_class_element[1]
            all_days = main_class.find_elements(By.CLASS_NAME, 'odf-calendar-day')

        for num in range(0, len(all_days)):
            content = all_days[num].get_attribute("textContent")
            content = re.sub("€.*", "", content)
            if content == day:
                all_days[num].click()
                break

    def passengers(self, adults=1, children=0, infants=0):
        button_element = self.find_element(By.XPATH, '//div[contains(@class, "odf-col-sm")]')
        button_element.click()
        plus_buttons = self.find_elements(By.CSS_SELECTOR, 'button[data-testid="increase-picker"]')

        if int(adults) > 1:
            count = 1
            while count < int(adults):
                count += 1
                plus_buttons[0].click()

        if int(children) > 0:
            count = 0
            while count < int(children):
                count += 1
                plus_buttons[1].click()

        if int(infants) > 0:
            count = 0
            while count < int(infants):
                count += 1
                plus_buttons[2].click()

    def search(self):
        button_element = self.find_element(By.CSS_SELECTOR, 'button[test-id="search-flights-btn"]')
        self.execute_script("arguments[0].click();", button_element)

    def cheapest(self):
        cheapest_button = self.find_element(By.ID, "sorting-tab-cheapest")
        cheapest_button.click()

    def fastest(self):
        fastest_button = self.find_element(By.ID, "sorting-tab-fastest")
        fastest_button.click()

    def flight_class(self, what_class):
        what_class = str(what_class).replace(" ", "").lower().strip()
        if what_class == "premiumeconomy":
            economy_class_button = self.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/section[1]/div/div[6]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div")
            economy_class_button.click()
            all_classes = self.find_elements(By.XPATH, '//li[contains(@class, "odf-text-md")]')
            all_classes[1].click()

        elif what_class == "business":
            business_class_button = self.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/section[1]/div/div[6]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div")
            business_class_button.click()
            all_classes = self.find_elements(By.XPATH, '//li[contains(@class, "odf-text-md")]')
            all_classes[2].click()

        elif what_class == "first":
            first_class_button = self.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/section[1]/div/div[6]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div")
            first_class_button.click()
            all_classes = self.find_elements(By.XPATH, '//li[contains(@class, "odf-text-md")]')
            all_classes[3].click()
        else:
            pass

    def one_way(self):
        one_way_button = self.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/section[1]/div/div[6]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/label/div/div[1]/span")
        one_way_button.click()
