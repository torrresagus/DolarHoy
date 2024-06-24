from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'DolarHoy es una librería en Python que facilita la obtención de cotizaciones actualizadas de diferentes tipos de dólar en Argentina, utilizando web scraping para extraer datos del sitio web DolarHoy.'

# Setting up
setup(
    name="dolarhoy",
    version=VERSION,
    url="https://github.com/torrresagus/DolarHoy",
    author="Agustin Torres",
    author_email="agustintorres2001@outlook.com.ar",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4'],
    keywords=['python', 'dolar', 'dolarhoy', 'DolarHoy', 'web scraping', 'exchange rates', 'cotizaciones', 'dollar rates', 'argentina', 'financial data', 'beautifulsoup', 'requests'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",  
        "Operating System :: OS Independent",
    ],
)
