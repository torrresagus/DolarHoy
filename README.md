![Logo](https://media.licdn.com/dms/image/C4E1BAQH9AcGUgii0ZQ/company-background_10000/0/1643139180993/dlar_hoy_cover?e=1719846000&v=beta&t=-qzaCmD0tI0ut3nfHMtJAFaOqOUuFCZizD8G3pnVTis)

![PyPI](https://img.shields.io/pypi/v/dolarhoy)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dolarhoy)
![PyPI - License](https://img.shields.io/pypi/l/dolarhoy)
![GitHub last commit](https://img.shields.io/github/last-commit/torrresagus/dolarhoy)
[![Python Test and Build](https://github.com/torrresagus/DolarHoy/actions/workflows/ci.yaml/badge.svg)](https://github.com/torrresagus/DolarHoy/actions/workflows/ci.yaml/badge.svg)

# DolarHoy

`DolarHoy` es una librería en Python que permite obtener las cotizaciones de diferentes tipos de dólar en Argentina desde el sitio web [DolarHoy](https://www.dolarhoy.com/). Utiliza las librerías `requests` y `BeautifulSoup` para hacer web scraping y extraer la información relevante.

## Instalación

Puedes instalar la librería utilizando `pip`:

```sh
pip install dolarhoy
```

## Uso

### Ejemplo Básico

A continuación se muestra un ejemplo básico de cómo utilizar la clase `DolarHoy` para obtener las cotizaciones del dólar.

```python
from dolarhoy import DolarHoy

# URL del sitio web
dolar_hoy = DolarHoy()

# Obtener todas las cotizaciones
all_data = dolar_hoy.get_all_data()

# Obtener la cotización del dólar blue
blue_price = dolar_hoy.get_blue_price()

# Obtener la cotización del dólar oficial
oficial_price = dolar_hoy.get_oficial_price()

# Obtener un resumen de todas las cotizaciones
summary = dolar_hoy.get_summary()
```

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


## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Descargo de Responsabilidad

Esta librería es para fines educativos y no se asume responsabilidad alguna por los usos que se le den. La información utilizada por esta librería proviene del sitio [DolarHoy.com](https://www.dolarhoy.com), un sitio meramente informativo que no brinda consejo, recomendación, asesoramiento o invitación de ningún tipo para realizar actos y/u operaciones de cualquier clase. 

Las fuentes de información citadas son de acceso público y los datos mostrados son elaborados sobre la base de dicha información. No se garantiza la precisión, veracidad, exactitud, integridad o vigencia de los datos. 

El uso de la información proporcionada es responsabilidad exclusiva del usuario y no se asume responsabilidad por eventuales daños o perjuicios derivados de decisiones basadas en los datos obtenidos. Esta librería no mantiene acuerdos, asociaciones, alianzas o vínculos con los anunciantes de [DolarHoy.com](https://www.dolarhoy.com) y no se responsabiliza por los contenidos de las piezas publicitarias o banners en dicho sitio.
