from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, '#main-search-form .P4Ui-text-content h2')
    # where_label = (By.CSS_SELECTOR, '.primary-content h2')
    signin_button = (By.CSS_SELECTOR, '#root .mc6t-main-content .wRhj-mod-justify-end span div')
    # signin_button = (By.CSS_SELECTOR, '.menu__wrapper .menu-label__wrapper button')
    search_button = (By.CSS_SELECTOR, '#main-search-form button span')
    # search_button = (By.CSS_SELECTOR, '.pageContent .SearchPage__FrontDoor .HPw7-form-fields-and-submit .HPw7-submit button')
    name_tag_input = (By.CSS_SELECTOR, '.c_neb-item-value')
    name_dropdown_column_input = (By.CSS_SELECTOR, 'input[placeholder="Destino"]')
    search_tag_input = (By.CSS_SELECTOR, '.JONo-button div')
    cancel_button = (By.CSS_SELECTOR, '.c_neb-item-close div')
    create_column_disabled_button = (By.CSS_SELECTOR, '.c_neb-mod-add-button')
    search_menu = (By.CSS_SELECTOR, 'nav[aria-label="Buscar"]')

    flights_option = (By.XPATH, '//nav/ul/li[1]/a/svg')
    stays_option = (By.CSS_SELECTOR, 'li a[href="/stays"]')
    cars_option = (By.CSS_SELECTOR, 'li a[href="/cars"]')
    citybreaks_option = (By.CSS_SELECTOR, 'li a[href="/citybreaks"]')
    trip_planning_menu = (By.CSS_SELECTOR, '.pRB0 div div:nth-child(2) > nav')
    trips_menu = (By.CSS_SELECTOR, '.pRB0-nav-items div a')
    final_menu = (By.CSS_SELECTOR, '.pRB0 div div:nth-child(4)')

