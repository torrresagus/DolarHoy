"""
# DolarHoy

`DolarHoy` es una librería en Python que permite obtener las cotizaciones de diferentes tipos de dólar en Argentina desde el sitio web [DolarHoy](https://www.dolarhoy.com/). Utiliza las librerías `requests` y `BeautifulSoup` para hacer web scraping y extraer la información relevante.

## Clases Enum

### `TipoDolar`
Una enumeración que representa los diferentes tipos de dólares:
- `BLUE`: "dolar_blue"
- `OFICIAL`: "dolar_oficial"
- `BOLSA`: "dolar_bolsa"
- `CONTADO_CON_LIQUI`: "contado_con_liqui"
- `TARJETA`: "dolar_tarjeta"

### `TipoOperacion`
Una enumeración que representa el tipo de operación:
- `COMPRA`: "compra"
- `VENTA`: "venta"

## Clase `DolarHoy`

### Constructor

#### `__init__(self, url: str = "https://www.dolarhoy.com")`
Inicializa una instancia de `DolarHoy` con la URL especificada. Por defecto, la URL es "https://www.dolarhoy.com".

### Métodos Privados

#### `_scrape_data(self)`
Extrae los datos de la URL y devuelve un diccionario que contiene las cotizaciones de diferentes tipos de dólares.

#### `_extract_cotizacion(self, soup, href)`
Extrae las cotizaciones (compra y venta) para un tipo específico de dólar del objeto BeautifulSoup y la URL proporcionada.

#### `_get_value(self, parent, class_name)`
Obtiene el valor de compra o venta del elemento HTML correspondiente.

### Métodos Públicos

#### `get_all_data(self) -> dict`
Devuelve un diccionario con todas las cotizaciones de los diferentes tipos de dólares.

#### `get_blue_price(self) -> dict`
Devuelve un diccionario con la cotización del dólar blue.

#### `get_oficial_price(self) -> dict`
Devuelve un diccionario con la cotización del dólar oficial.

#### `get_bolsa_price(self) -> dict`
Devuelve un diccionario con la cotización del dólar bolsa.

#### `get_contado_con_liqui_price(self) -> dict`
Devuelve un diccionario con la cotización del dólar contado con liqui.

#### `get_tarjeta_price(self) -> dict`
Devuelve un diccionario con la cotización del dólar tarjeta.

#### `get_price(self, tipo_dolar: TipoDolar, tipo_operacion: TipoOperacion) -> float`
Devuelve el precio de compra o venta para un tipo de dólar y operación específicos.

#### `get_all_prices(self, tipo_operacion: TipoOperacion) -> dict`
Devuelve un diccionario con todos los precios de compra o venta para todos los tipos de dólares.

#### `get_summary(self) -> str`
Devuelve un resumen en formato de cadena con todas las cotizaciones de los diferentes tipos de dólares, incluyendo los precios de compra y venta, la fuente y la URL de la fuente.
"""

from enum import Enum
import requests
from bs4 import BeautifulSoup

class TipoDolar(Enum):
    BLUE = "dolar_blue"
    OFICIAL = "dolar_oficial"
    BOLSA = "dolar_bolsa"
    CONTADO_CON_LIQUI = "contado_con_liqui"
    TARJETA = "dolar_tarjeta"

class TipoOperacion(Enum):
    COMPRA = "compra"
    VENTA = "venta"
class DolarHoy:
    def __init__(self, url: str = "https://www.dolarhoy.com"):
        self.url = url

    def _scrape_data(self):
        try:
            response = requests.get(self.url)    
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error making request: {e}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
            
        data = {}

        cotizaciones = {
            TipoDolar.BLUE: "/cotizaciondolarblue",
            TipoDolar.OFICIAL: "/cotizaciondolaroficial",
            TipoDolar.BOLSA: "/cotizaciondolarbolsa",
            TipoDolar.CONTADO_CON_LIQUI: "/cotizaciondolarcontadoconliqui",
            TipoDolar.TARJETA: "/cotizacion-dolar-tarjeta"
        }
        
        for tipo_dolar, href in cotizaciones.items():
            data[tipo_dolar.value] = self._extract_cotizacion(soup, href)

        return data
    
    def _extract_cotizacion(self, soup, href):
        element = soup.find('a', href=href)
        if not element:
            print(f"No element found for href {href}")
            return {}

        parent = element.find_parent('div', class_='tile is-child')
        if not parent:
            print(f"No parent found for href {href} with class 'tile is-child'")
            return {}

        compra = self._get_value(parent, 'compra')
        venta = self._get_value(parent, 'venta')

        return {
            "compra": compra,
            "venta": venta,
            "source": "DolarHoy.com ®",
            "source_url": self.url
        }

    def _get_value(self, parent, class_name):
        element = parent.find('div', class_=class_name)
        if element and element.find('div', class_='val'):
            value = element.find('div', class_='val').text.strip('$').replace(',', '')
            try:
                return float(value)
            except ValueError:
                print(f"Error converting {value} to float")
        return None

    def get_all_data(self) -> dict:
        return self._scrape_data()

    def get_blue_price(self) -> dict:
        return self._scrape_data().get('dolar_blue')

    def get_oficial_price(self) -> dict:
        return self._scrape_data().get('dolar_oficial')

    def get_bolsa_price(self) -> dict:
        return self._scrape_data().get('dolar_bolsa')

    def get_contado_con_liqui_price(self) -> dict:
        return self._scrape_data().get('contado_con_liqui')

    def get_tarjeta_price(self) -> dict:
        return self._scrape_data().get('dolar_tarjeta')

    def get_price(self, tipo_dolar: TipoDolar, tipo_operacion: TipoOperacion) -> float:
        data = self._scrape_data()
        return data.get(tipo_dolar.value, {}).get(tipo_operacion.value)
    
    def get_all_prices(self, tipo_operacion: TipoOperacion) -> dict:
        data = self._scrape_data()
        prices = {key: value.get(tipo_operacion.value) for key, value in data.items() if tipo_operacion.value in value}
        return prices

    def get_summary(self) -> str:
        data = self._scrape_data()
        summary = []
        for key, value in data.items():
            tipo_dolar = key.replace('_', ' ').capitalize()
            compra = value.get('compra', 'N/A')
            venta = value.get('venta', 'N/A')
            summary.append(f"{tipo_dolar}:\nCompra: ${compra}\nVenta: ${venta}\nSource: {value.get('source')}\nSource URL: {value.get('source_url')}")
            
        return "\n".join(summary)