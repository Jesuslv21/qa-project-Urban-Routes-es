URBAN ROUTES 🚕 Proyecto 9

Este proyecto automatiza una serie de pruebas funcionales sobre el sitio web de Urban Routes, una aplicación de solicitud de transporte. La automatización fue realizada utilizando Selenium WebDriver, Pytest

📌 ¿Qué pruebas automatiza?

El proyecto realiza las siguientes acciones de forma automática:

Configura una dirección de origen y destino.
Selecciona la tarifa "Comfort".
Ingresa un número de teléfono.
Ingresa el código SMS recibido.
Agrega una tarjeta de crédito.
Escribe un mensaje personalizado para el conductor.
Solicita manta y pañuelos.
Pide dos helados.
Confirma el viaje y espera a que aparezca la información del conductor.

🧩 Estructura del proyecto


qa-project-urban-routes-es/
│
├── Data.py                                 # Datos como URL base, número de teléfono, tarjeta, etc.
├── Retrieve_Code.py                        # API para obtener el código SMS
├── Urban_Routes_Tests.py                   # Archivo principal con pruebas estructuradas en Pytest
├── Urban_Routes_Page.py                    # Dependencias del proyecto

⚙️ Requisitos

Python 3.9+
Google Chrome instalado
ChromeDriver (compatible con tu versión de Chrome)
📦 Instalación

Clona el repositorio:

git clone https://github.com/tu-usuario/qa-project-urban-routes-es.git
cd qa-project-urban-routes-es
Crea y activa un entorno virtual (opcional pero recomendado)**:

python -m venv .venv
.venv\Scripts\activate   # En Windows
Instala las dependencias:

pip install -r requirements.txt
▶️ Cómo ejecutar las pruebas

Desde la terminal (dentro del proyecto):

pytest urban_routes_tests.py
O bien, desde PyCharm puedes hacer clic derecho sobre urban_routes_tests.py y seleccionar "Run 'pytest in urban_routes_tests.py'".

NO OLVIDES ACTUALIZAR EL URL EN data.py con el generado por servidor en la plataforma de TripleTen en la práctica, de otra forma, no correrá el script.

🧪 Tecnologías y herramientas usadas

Python
Selenium WebDriver
Pytest
WebDriverWait (esperas explícitas, evitando time.sleep)
Page Object Model
