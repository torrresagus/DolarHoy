
# DolarHoy

`DolarHoy` es una librería en Python que permite obtener las cotizaciones de diferentes tipos de dólar en Argentina desde el sitio web [DolarHoy](https://www.dolarhoy.com/). Utiliza las librerías `requests` y `BeautifulSoup` para hacer web scraping y extraer la información relevante.

## Instalación

Puedes instalar la librería utilizando `pip`:

```sh
pip install DolarHoy
```

## Uso

### Ejemplo Básico

A continuación se muestra un ejemplo básico de cómo utilizar la clase `DolarHoy` para obtener las cotizaciones del dólar.

```python
from dolarhoy import DolarHoy

# URL del sitio web
url = "https://www.dolarhoy.com/"
dolar_hoy = DolarHoy(url)

# Obtener todas las cotizaciones
all_data = dolar_hoy.get_all_data()
print(all_data)

# Obtener la cotización del dólar blue
blue_price = dolar_hoy.get_blue_price()
print("Dólar Blue:", blue_price)

# Obtener la cotización del dólar oficial
oficial_price = dolar_hoy.get_oficial_price()
print("Dólar Oficial:", oficial_price)

# Obtener un resumen de todas las cotizaciones
summary = dolar_hoy.get_summary()
print(summary)
```

## Métodos

### `get_all_data()`
Obtiene todas las cotizaciones disponibles y las devuelve en forma de diccionario.

### `get_blue_price()`
Obtiene la cotización del dólar blue.

### `get_oficial_price()`
Obtiene la cotización del dólar oficial.

### `get_bolsa_price()`
Obtiene la cotización del dólar bolsa.

### `get_contado_con_liqui_price()`
Obtiene la cotización del dólar contado con liqui.

### `get_tarjeta_price()`
Obtiene la cotización del dólar tarjeta.

### `get_price(tipo_dolar, tipo_operacion)`
Obtiene el precio de un tipo de dólar específico (`tipo_dolar`) y una operación específica (`tipo_operacion`), que puede ser `compra` o `venta`.

### `get_all_prices(tipo_operacion)`
Obtiene los precios de todos los tipos de dólar para una operación específica (`tipo_operacion`), que puede ser `compra` o `venta`.

### `get_summary()`
Obtiene un resumen de todas las cotizaciones disponibles en formato de texto.

## Dependencias

- `requests`
- `beautifulsoup4`

## Instalación de Dependencias

Puedes instalar las dependencias utilizando `pip`:

```sh
pip install requests beautifulsoup4
```

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.