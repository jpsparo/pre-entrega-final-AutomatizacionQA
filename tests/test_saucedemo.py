import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import iniciar_sesion


@pytest.fixture
def driver():

    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_argument("--lang=es")

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# ---------------------------------------------------------
# TEST 01 - LOGIN
# ---------------------------------------------------------

def test_01_login(driver):

    iniciar_sesion(driver)

    assert "/inventory.html" in driver.current_url, \
        "ERROR: No se redirigió a /inventory.html"


# ---------------------------------------------------------
# TEST 02 - VERIFICAR INVENTARIO
# ---------------------------------------------------------

def test_02_verificar_inventario(driver):

    iniciar_sesion(driver)

    page_title = driver.title

    section_title = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text

    assert page_title == "Swag Labs", \
        f'ERROR: Título de ventana esperado "Swag Labs", obtenido "{page_title}"'

    assert section_title == "Products", \
        f'ERROR: Título de sección esperado "Products", obtenido "{section_title}"'


# ---------------------------------------------------------
# TEST 03 - PRODUCTOS VISIBLES
# ---------------------------------------------------------

def test_03_productos_visibles(driver):

    iniciar_sesion(driver)

    inventory_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    assert len(inventory_items) > 0, \
        "ERROR: No se encontraron productos visibles"


# ---------------------------------------------------------
# TEST 04 - VALIDAR INTERFAZ
# ---------------------------------------------------------

def test_04_validar_interfaz(driver):

    iniciar_sesion(driver)

    menu_button = driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    )

    filtro = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert menu_button.is_displayed(), \
        "ERROR: El menú no está visible"

    assert filtro.is_displayed(), \
        "ERROR: El filtro no está visible"


# ---------------------------------------------------------
# TEST 05 - INFORMACIÓN DEL PRIMER PRODUCTO
# ---------------------------------------------------------

def test_05_informacion_primer_producto(driver):

    iniciar_sesion(driver)

    first_item = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    product_name = first_item.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    product_price = first_item.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    print(f"Primer producto: {product_name}")
    print(f"Precio: {product_price}")

    assert product_name != "", \
        "ERROR: El nombre del producto está vacío"

    assert product_price != "", \
        "ERROR: El precio del producto está vacío"


# ---------------------------------------------------------
# TEST 06 - AGREGAR PRODUCTO AL CARRITO
# ---------------------------------------------------------

def test_06_agregar_producto_al_carrito(driver):

    iniciar_sesion(driver)

    first_item = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )[0]

    product_name = first_item.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    add_button = first_item.find_element(
        By.TAG_NAME,
        "button"
    )

    add_button.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (
                By.CSS_SELECTOR,
                ".inventory_item button"
            ),
            "Remove"
        )
    )

    assert add_button.text == "Remove", \
        f'ERROR: El botón del producto "{product_name}" no cambió a "Remove"'


# ---------------------------------------------------------
# TEST 07 - VERIFICAR CONTADOR DEL CARRITO
# ---------------------------------------------------------

def test_07_verificar_contador_carrito(driver):

    iniciar_sesion(driver)

    first_item = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )[0]

    add_button = first_item.find_element(
        By.TAG_NAME,
        "button"
    )

    add_button.click()

    contador_carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert contador_carrito.text == "1", \
        f'ERROR: Se esperaba "1", se obtuvo "{contador_carrito.text}"'


# ---------------------------------------------------------
# TEST 08 - NAVEGAR AL CARRITO
# ---------------------------------------------------------

def test_08_navegar_carrito(driver):

    iniciar_sesion(driver)

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )

    assert "/cart.html" in driver.current_url, \
        "ERROR: No se redirigió a /cart.html"


# ---------------------------------------------------------
# TEST 09 - COMPROBAR PRODUCTO EN EL CARRITO
# ---------------------------------------------------------

def test_09_comprobar_producto_en_el_carrito(driver):

    iniciar_sesion(driver)

    first_item = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )[0]

    product_name = first_item.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    first_item.find_element(
        By.TAG_NAME,
        "button"
    ).click()

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )

    producto_nombre_en_carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    ).text

    assert producto_nombre_en_carrito == product_name, \
        f'ERROR: Se esperaba "{product_name}", se obtuvo "{producto_nombre_en_carrito}"'