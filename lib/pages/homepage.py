import logging

from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import validate_wait_results
from lib.pages.basepage import BasePage
from lib.pages.webelements.homewebelements import HomeWebElements

logger = logging.getLogger(__name__)


class HomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)
        self.context = context
        self.web_driver = context.browser
        self.webElements = HomeWebElements
        print("HomePage initialized")

    def get_title_page(self):
        return self.web_driver.get_title_page()

    def get_current_url(self):
        return self.web_driver.get_current_url()

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(self.context, HomeWebElements.where_label),
            GeneralComponents.wait_until_element_is_present(self.context, HomeWebElements.signin_button))

    def reload_page(self):
        return self.reload_page()

    def menu_actions(self):
        return {
                "flights": self.navigate_to_flights,
                "stays": self.navigate_to_stays,
                "cars": self.navigate_to_cars,
                "city_breaks": self.navigate_to_city_breaks
            }

    def navigate_to_flights(self):
        print(f"Clicking on flights: {self.webElements.flights_option}")
        self.find_element(*self.webElements.flights_option).click()

    def navigate_to_stays(self):
        print(f"Clicking on stays: {self.webElements.stays_option}")
        self.find_element(self.webElements.stays_option).click()

    def navigate_to_cars(self):
        print(f"Clicking on cars: {self.webElements.cars_option}")
        self.find_element(self.webElements.cars_option).click()

    def navigate_to_city_breaks(self):
        print(f"Clicking on city breaks: {self.webElements.citybreaks_option}")
        self.find_element(self.webElements.citybreaks_option).click()
