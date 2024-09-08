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

    #menu_options
    flights_option = (By.XPATH, '//nav/ul/li[1]/a/svg')
    stays_option = (By.CSS_SELECTOR, 'li a[href="/stays"]')
    cars_option = (By.CSS_SELECTOR, 'li a[href="/cars"]')
    packages = (By.CSS_SELECTOR, 'li a[href="/citybreaks"]')
    explore = (By.CSS_SELECTOR, '.FVRF-drawer-content-wrapper nav ul li:first-child a div')
    blog = (By.CSS_SELECTOR, 'nav > ul > li:nth-child(2) > a > div')
    direct_flights = (By.CSS_SELECTOR, '#root .mc6t-main-content .c5ab7-mod-absolute .FVRF-drawer-content-wrapper nav ul li:nth-child(3) a div')
    best_moment = (By.CSS_SELECTOR, '#root .mc6t-main-content .c5ab7-mod-absolute .FVRF-drawer-content-wrapper nav ul li:nth-child(4) a div')
    kayak_for_business = (By.CSS_SELECTOR, '#root .mc6t-main-content .c5ab7-mod-absolute .FVRF-drawer-content-wrapper nav ul li:nth-child(5) a div')
    trips = (By.CSS_SELECTOR, '#root > div > header > div > div.mc6t-main-content.mc6t-mod-bordered > div > div.c5ab7.c5ab7-mod-absolute > div.FVRF-drawer-content-wrapper > div > div:nth-child(1) > div:nth-child(5) > div > a > div')

