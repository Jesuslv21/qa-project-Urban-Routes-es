import time
from data import data
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from pages import urban_routes_page as urp


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
       chrome_options = webdriver.ChromeOptions()
       chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
       cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
       cls.driver.get(data.urban_routes_url)
       cls.routes_page = urp.UrbanRoutesPage(cls.driver)



    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = urp.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(1)

    #PRUEBA CLIC EN BOTON OPTIMO
    def test_optimo_button(self):
        self.routes_page.click_optimo_button()
        time.sleep(2)

    #PRUEBA CLIC BOTON FLASH
    def test_flash_button(self):
        self.routes_page.click_flash_button()
        time.sleep(2)

    #BOTON PEDIR TAXI
    def test_taxi_button(self):
        self.routes_page.click_taxi_button()
        time.sleep(2)

    #BOTON COMFORT
    def test_comfort_button(self):
        self.routes_page.click.comfort_button()
        time.sleep(2)


    #BOTON TELEFONO
    def test_phone_button(self):
        self.routes_page.click_phone_button()
    time.sleep(5)

    #INGRESAR TELEFONO PARNTALLA EMERGERNTE
    def test_enter_phone_number(self):
        self.routes_page.enter_phone_number()
        actual_number = data.phone_number
        phone_number_written = self.routes_page.is_phone_input_filled_correctly()
        assert phone_number_written == actual_number
        WebDriverWait(self.driver, timeout=5)
        time.sleep(5)

    #AGREGAR INFORMACION DE TARJETA
    def test_add_credit_card(self):
        self.routes_page.add_credit_card(card_number, card_cvv)
        card_number = data.card_number
        cerd_cvv = data.card_cvv
        assert self.routes_page.is_card_linked(), "La tarjeta no fue vinculada correctamente"

    #INGRESAR MENSAJE PARA CONDUCTOR
    def test_write_driver_message(self):
        self.routes_page.write_driver_message(message_for_driver)
        assert self.routes_page.is_message_sent(message_for_driver), "El mensaje no se ingresó correctamente"

    def test_toggle_blanket_and_tissues(self):
        self.page.toggle_blanket_and_tissues()
        assert self.page.is_blanket_and_tissues_selected(), "La opción de manta y pañuelos no fue activada"

    def test_add_ice_cream(self):
        self.page.add_ice_cream()
        assert self.page.is_ice_cream_added(), "No se agregaron 2 helados"

    def test_taxi_seeker_appears(self):
        self.page.confirm_trip()
        assert self.page.is_taxi_modal(), "No apareció el modal para buscar un taxi"

    def test_confirm_trip_and_check_driver(self):
        assert self.page.wait_for_driver_info(), "La información del conductor no apareció"



    @classmethod
    def teardown_class(cls):
     cls.driver.quit()