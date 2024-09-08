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
            "packages": self.navigate_to_packages,
            "explore": self.navigate_to_explore,
            "blog": self.navigate_to_blog,
            "direct_flights": self.navigate_to_direct_flights,
            "best_moment": self.navigate_to_best_moment,
            "kayak_for_business": self.navigate_to_kayak_for_business,
            "trips": self.navigate_to_trips
        }

    def navigate_to_flights(self):
        print(f"Clicking on flights: {self.webElements.flights_option}")
        self.find_element(self.webElements.flights_option).click()

    def navigate_to_stays(self):
        print(f"Clicking on stays: {self.webElements.stays_option}")
        self.find_element(self.webElements.stays_option).click()

    def navigate_to_cars(self):
        print(f"Clicking on cars: {self.webElements.cars_option}")
        self.find_element(self.webElements.cars_option).click()

    def navigate_to_packages(self):
        print(f"Clicking on packages: {self.webElements.packages}")
        self.find_element(self.webElements.packages).click()

    def navigate_to_explore(self):
        print(f"Clicking on explore: {self.webElements.explore}")
        self.find_element(self.webElements.explore).click()

    def navigate_to_blog(self):
        print(f"Clicking on blog: {self.webElements.blog}")
        self.find_element(self.webElements.blog).click()

    def navigate_to_direct_flights(self):
        print(f"Clicking on direct flights: {self.webElements.direct_flights}")
        self.find_element(self.webElements.direct_flights).click()

    def navigate_to_best_moment(self):
        print(f"Clicking on best moment: {self.webElements.best_moment}")
        self.find_element(self.webElements.best_moment).click()

    def navigate_to_kayak_for_business(self):
        print(f"Clicking on kayak for business: {self.webElements.kayak_for_business}")
        self.find_element(self.webElements.kayak_for_business).click()

    def navigate_to_trips(self):
        print(f"Clicking on trips: {self.webElements.trips}")
        self.find_element(self.webElements.trips).click()