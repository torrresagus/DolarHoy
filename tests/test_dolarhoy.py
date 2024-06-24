import pytest
from DolarHoy import DolarHoy

# URL a utilizar
url = "https://www.dolarhoy.com/"

@pytest.fixture
def dolar_hoy():
    return DolarHoy(url)

def test_get_all_data(dolar_hoy):
    data = dolar_hoy.get_all_data()
    
    expected_keys = {
        "dolar_blue", "dolar_oficial", "dolar_bolsa", "contado_con_liqui", "dolar_tarjeta"
    }
    
    for key in expected_keys:
        assert key in data, f"Missing key {key} in data"
        assert isinstance(data[key], dict), f"Value for {key} should be a dict"
        if 'compra' in data[key]:
            assert isinstance(data[key]['compra'], float), f"compra for {key} should be a float"
        if 'venta' in data[key]:
            assert isinstance(data[key]['venta'], float), f"venta for {key} should be a float"

def test_get_blue_price(dolar_hoy):
    price = dolar_hoy.get_blue_price()
    if price is not None:
        assert 'compra' in price or 'venta' in price, "Both 'compra' and 'venta' keys should be in the data"
        if 'compra' in price:
            assert isinstance(price['compra'], float), "'compra' should be a float"
        if 'venta' in price:
            assert isinstance(price['venta'], float), "'venta' should be a float"

def test_get_oficial_price(dolar_hoy):
    price = dolar_hoy.get_oficial_price()
    if price is not None:
        assert 'compra' in price or 'venta' in price, "Both 'compra' and 'venta' keys should be in the data"
        if 'compra' in price:
            assert isinstance(price['compra'], float), "'compra' should be a float"
        if 'venta' in price:
            assert isinstance(price['venta'], float), "'venta' should be a float"

def test_get_bolsa_price(dolar_hoy):
    price = dolar_hoy.get_bolsa_price()
    if price is not None:
        assert 'compra' in price or 'venta' in price, "Both 'compra' and 'venta' keys should be in the data"
        if 'compra' in price:
            assert isinstance(price['compra'], float), "'compra' should be a float"
        if 'venta' in price:
            assert isinstance(price['venta'], float), "'venta' should be a float"

def test_get_contado_con_liqui_price(dolar_hoy):
    price = dolar_hoy.get_contado_con_liqui_price()
    if price is not None:
        assert 'compra' in price or 'venta' in price, "Both 'compra' and 'venta' keys should be in the data"
        if 'compra' in price:
            assert isinstance(price['compra'], float), "'compra' should be a float"
        if 'venta' in price:
            assert isinstance(price['venta'], float), "'venta' should be a float"

def test_get_tarjeta_price(dolar_hoy):
    price = dolar_hoy.get_tarjeta_price()
    if price is not None:
        assert 'venta' in price, "'venta' key should be in the data"
        if 'venta' in price:
            assert isinstance(price['venta'], float), "'venta' should be a float"

def test_get_price(dolar_hoy):
    for tipo_dolar in ["dolar_blue", "dolar_oficial", "dolar_bolsa", "contado_con_liqui", "dolar_tarjeta"]:
        for tipo_operacion in ["compra", "venta"]:
            price = dolar_hoy.get_price(tipo_dolar, tipo_operacion)
            if price is not None:
                assert isinstance(price, float), f"{tipo_operacion} for {tipo_dolar} should be a float"

def test_get_all_prices(dolar_hoy):
    for tipo_operacion in ["compra", "venta"]:
        prices = dolar_hoy.get_all_prices(tipo_operacion)
        for key, value in prices.items():
            assert isinstance(value, float), f"{tipo_operacion} for {key} should be a float"

def test_get_summary(dolar_hoy):
    summary = dolar_hoy.get_summary()
    assert isinstance(summary, str), "Summary should be a string"
    assert len(summary) > 0, "Summary should not be empty"