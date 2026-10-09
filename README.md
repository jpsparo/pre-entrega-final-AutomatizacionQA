# Automatización de pruebas - SauceDemo

## Descripción

Proyecto de automatización de pruebas funcionales sobre la aplicación web SauceDemo.

El proyecto fue desarrollado utilizando Python, Pytest y Selenium WebDriver.

El objetivo es automatizar pruebas relacionadas con:

- Inicio de sesión.
- Verificación del inventario.
- Visualización de productos.
- Elementos de la interfaz.
- Información del primer producto.
- Agregado de productos al carrito.
- Contador del carrito.
- Navegación al carrito.
- Verificación del producto agregado.

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Chrome WebDriver
- webdriver-manager
- pytest-html

## Estructura del proyecto

```text
pre-entrega-final/
│
├── tests/
│   ├── __init__.py
│   └── test_saucedemo.py
│
├── pages/
│   ├── __init__.py
│   └── LoginPage.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── reports/
│   ├── screenshots/
│   └── logs/
│
├── README.md
├── requirements.txt
└── .gitignore


## Instalación

Se recomienda utilizar un entorno virtual.

Crear el entorno virtual:

python -m venv .venv

## Activar el entorno virtual en Windows PowerShell:

.\.venv\Scripts\Activate.ps1

## Instalar las dependencias:

pip install -r requirements.txt

##Ejecución de las pruebas

Para ejecutar todos los tests:

pytest -v

## Para ejecutar únicamente el archivo de SauceDemo:

pytest tests/test_saucedemo.py -v
Reporte HTML

##Para generar un reporte HTML:

pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html

El reporte generado se encuentra en:

reports/reporte.html

Aplicación bajo prueba

URL:

https://www.saucedemo.com/

Usuario utilizado:

standard_user

Contraseña utilizada:

secret_sauce
Arquitectura

El proyecto utiliza el patrón Page Object Model (POM).

La clase LoginPage contiene los localizadores y las acciones relacionadas con la página de inicio de sesión.

Los tests contienen las verificaciones que se desean realizar.

Las funciones reutilizables se encuentran en la carpeta utils.

Esperas

Se utilizan esperas implícitas mediante Selenium y esperas explícitas mediante WebDriverWait y Expected Conditions.

Esto permite esperar la disponibilidad de determinados elementos o condiciones de la página sin utilizar esperas fijas mediante time.sleep().

Independencia de los tests

Cada test inicia su propia sesión del navegador y realiza nuevamente el inicio de sesión cuando es necesario.

De esta manera, un test no depende de que otro test haya sido ejecutado previamente.

Evidencias

Los reportes HTML permiten visualizar el resultado de la ejecución de las pruebas.

La carpeta reports/ está destinada a almacenar los reportes y las evidencias generadas durante la ejecución.

