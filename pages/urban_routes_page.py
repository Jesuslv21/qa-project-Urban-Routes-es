from data import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    #1 LOCALIZAR ELEMENTOS
    #CREAR VARIABLE = TIPO DE SELECTOR + DONDE Y COMO LOCALIZAR
    optimo_button = (By.CSS_SELECTOR, '.modes-container .mode:nth-child(1)')

    #PREUBAS DE PROYECTO PEDIR TAXI
    # FLASH BUTTON
    flash_button = (By.XPATH, '//div[@class="mode" and text()="Flash"]')
    # BOTON PEDIR TAXI
    taxi_button = (By.XPATH, '//button[@class="button round" and text()="Pedir un taxi"]')
    # BOTON CONFORT
    comfort_button = (By.XPATH,'//div[text()= "Comfort"]')
    #BOTON AGREGAR TELEFONO
    phone_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]')

    #VENTANA EMERGENTE AGREGAR NUMERO TELEFONICO
    phone_input = (By.CSS_SELECTOR, '.tariff-picker.shown > div.form > div.np-button > div')
    phone_field = (By.ID, "phone")
    next_button = (By.CSS_SELECTOR, '.buttons > button')
    code_input = (By.CSS_SELECTOR, '.np-input > div.input-container')
    code_field = (By.ID, 'code')
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")

    #AÑADIR FORMA DE PAGO TARJETA
    payment_method = (By.CSS_SELECTOR, '.pp-button')
    add_card_button = (By.CSS_SELECTOR, '.payment-picker.open .pp-selector .pp-row.disabled .pp-title')
    card_number_input = (By.ID, 'number')
    card_cvv_input = (By.XPATH, "//input[@placeholder='12']")
    add_card_window = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active')
    link_card_button = (By.CSS_SELECTOR, '.pp-buttons > button:nth-child(1)')
    close_button = (By.CSS_SELECTOR, '.payment-picker .close-button')
    pp_value = (By.CLASS_NAME, "pp-value-text")

    #AÑADIR MENSAJE
    message_for_driver = (By.ID, 'message')

    blanket_and_tissues_option = (By.CSS_SELECTOR, '.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    ice_cream_add_button = (By.CSS_SELECTOR,'.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    ice_cream_counter = (By.CSS_SELECTOR, '.counter-value')
    submit_button = (By.CSS_SELECTOR, '.smart-button-wrapper > button')
    taxi_seeker_modal = (By.CSS_SELECTOR, '.order.shown > div.order-body')
    driver_info = (By.CSS_SELECTOR,'.order-subbody > div.order-buttons > div:nth-child(1) > div.order-button > img')




    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)


    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)


    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

# LO QUE HACE MI ELEMENTO
    def get_optimo_button(self):
        return self.wait.until (EC.element_to_be_clickable(self.optimo_button))
    def click_optimo_button(self):
        self.get_optimo_button().click()

    #Flash button
    def get_flash_button(self):
        return self.wait.until (EC.element_to_be_clickable(self.flash_button))
    def click_flash_button(self):
        self.get_flash_button().click()

    #TAXI BUTTON
    def get_taxi_button(self):
        return self.wait.until (EC.element_to_be_clickable(self.taxi_button))
    def click_taxi_button(self):
        self.get_taxi_button().click()

    #Comfort boton
    def get_comfort_button(self):
        return self.wait.until (EC.element_to_be_clickable(self.comfort_button))
    def click_comfort_button(self):
        self.get_comfort_button().click()

    #phone boton
    def get_phone_button(self):
        return self.wait.until (EC.element_to_be_clickable(self.phone_button))
    def click_phone_button(self):
        self.get_phone_button().click()

#CAMPO NUMERO DE TELEFONO VENTANA EMERGENTE
    def enter_phone_number(self):
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.phone_input)).click()
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.phone_field)).send_keys(data.phone_number)
        self.driver.find_element(*self.next_button).click()
        phone_code_helper = retrieve_phone_code(self.driver)
        code = phone_code_helper.get_sms_code(self.driver)
        #WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.code_field)).send_keys(code)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.code_field))
        self.driver.find_element(*self.code_field).send_keys(code)
        self.driver.find_element(*self.confirm_button).click()
    def is_phone_input_filled_correctly(self):
        return self.driver.find_element(*self.phone_field).get_property('checked')

#AÑADIR FORMA DE PAGO(TARJETA)
    def add_credit_card(self, number, cvv):
        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.payment_method)).click()
            # self.wait.until(EC.element_to_be_clickable(*self.add_card_button)).click()
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.add_card_button)).click()
            self.wait.until(EC.visibility_of_element_located(self.card_number_input)).send_keys(number)
            self.wait.until(EC.visibility_of_element_located(self.card_cvv_input)).send_keys(cvv)
            # self.wait.until(EC.element_to_be_clickable(self.add_card_window)).click()
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.add_card_window)).click()
            self.wait.until(EC.element_to_be_clickable(self.link_card_button)).click()
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.close_button)).click()

        except Exception as e:
            print(f"[ERROR] No se pudo agregar la tarjeta: {e}")

    def is_card_linked(self):
        return self.driver.find_element(*self.pp_value).text

    #AÑDIR MENSAJE
    def message_for_driver(self):
        message_box = self.wait.until(EC.presence_of_element_located(self.message_input))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", message_box)
        message_box.clear()
        message_box.send_keys(message)

    def toggle_blanket_and_tissues(self):
        option = self.wait.until(EC.element_to_be_clickable(self.blanket_and_tissues_option))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
        option.click()

    def is_blanket_and_tissues_selected(self):
        checkbox = self.driver.find_element(By.CSS_SELECTOR, 'input.switch-input')
        return checkbox.is_selected()

    def add_ice_cream(self, quantity=2):
        button = self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        for _ in range(quantity):
            button.click()
            self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button))

    def get_ice_cream_count(self):
        counter = self.driver.find_element(*self.ice_cream_counter)
        return int(counter.text.strip())

    def is_ice_cream_added(self):
        return self.get_ice_cream_count() == 2

    def confirm_trip(self):
        button = self.wait.until(EC.presence_of_element_located(self.submit_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()

    def is_taxi_modal(self, timeout=3):
        driver_img = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.taxi_seeker_modal))
        return driver_img.is_displayed()

    def wait_for_driver_info(self, timeout=20):
        driver_img = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.driver_info)
        )
        return driver_img.is_displayed()












