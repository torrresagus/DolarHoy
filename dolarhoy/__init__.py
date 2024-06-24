import requests
from bs4 import BeautifulSoup

class DolarHoy:
    def __init__(self, url):
        self.url = url

    def _scrape_data(self):
        response = requests.get(self.url)
        with open("dolarhoy.html", "w") as file:
            file.write(response.text
            )
            
        soup = BeautifulSoup(response.content, 'html.parser')
        data = {}

        cotizaciones = [
            ("/cotizaciondolarblue", "dolar_blue"),
            ("/cotizaciondolaroficial", "dolar_oficial"),
            ("/cotizaciondolarbolsa", "dolar_bolsa"),
            ("/cotizaciondolarcontadoconliqui", "contado_con_liqui"),
            ("/cotizacion-dolar-tarjeta", "dolar_tarjeta")
        ]

        for href, key in cotizaciones:
            element = soup.find('a', href=href)
            if element:
                parent = element.find_parent('div', class_='tile is-child')

                if parent:
                    compra_element = parent.find('div', class_='compra')
                    venta_element = parent.find('div', class_='venta')

                    compra = None
                    if compra_element and compra_element.find('div', class_='val'):
                        compra = float(compra_element.find('div', class_='val').text.strip('$').replace(',', ''))

                    venta = None
                    if venta_element and venta_element.find('div', class_='val'):
                        venta = float(venta_element.find('div', class_='val').text.strip('$').replace(',', ''))

                    data[key] = {}
                    if compra is not None:
                        data[key]['compra'] = compra
                    if venta is not None:
                        data[key]['venta'] = venta
                else:
                    print(f"No parent found for {key} with class 'tile is-child'")
            else:
                print(f"No element found for {key} with href {href}")

        return data

    def get_all_data(self):
        return self._scrape_data()

    def get_blue_price(self):
        return self._scrape_data().get('dolar_blue')

    def get_oficial_price(self):
        return self._scrape_data().get('dolar_oficial')

    def get_bolsa_price(self):
        return self._scrape_data().get('dolar_bolsa')

    def get_contado_con_liqui_price(self):
        return self._scrape_data().get('contado_con_liqui')

    def get_cripto_price(self):
        return self._scrape_data().get('dolar_cripto')

    def get_tarjeta_price(self):
        return self._scrape_data().get('dolar_tarjeta')

    def get_price(self, tipo_dolar, tipo_operacion):
        data = self._scrape_data()
        return data.get(tipo_dolar, {}).get(tipo_operacion)

    def get_all_prices(self, tipo_operacion):
        data = self._scrape_data()
        prices = {key: value.get(tipo_operacion) for key, value in data.items() if tipo_operacion in value}
        return prices

    def get_summary(self):
        data = self._scrape_data()
        summary = []
        for key, value in data.items():
            tipo_dolar = key.replace('_', ' ').capitalize()
            compra = value.get('compra', 'N/A')
            venta = value.get('venta', 'N/A')
            summary.append(f"{tipo_dolar}:\nCompra: ${compra}\nVenta: ${venta}\n")
        return "\n".join(summary)