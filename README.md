# Práctica 1: Web scraping
## Descripción

La información se ha seleccionado en un contexto de análisis de recursos información económica e hipotecas de empresas por provincia en España. El sitio web es un recurso de open data para el análisis de información de diversos contenidos de datos abiertos para que se puedan consultar y analizar. Se elige el sitio web debido a que presentan los conjuntos de datos y posibles datos relacionados por tanto es posible realizar cruces de información y generar conjuntos de datos con mayores características.


## Detalle solución y complejidad

Se presenta una solución que permite la extracción de contenido web dinámico, en donde la presentación del contenido corresponde a cargas parciales de secciones cargadas de manera asíncrona. Se hace uso de programación multihilo y procesamiento de tareas para optimizar los tiempos de respuesta diferenciando entre los procesos de extracción de contenido web y la generación de los documentos csv. En este caso se generan inicialmente varios ficheros luego de extraer el contenido de las diferentes pestañas de una página. Luego, se realizará un procesamiento de tratamiento de los datos e integración de la fuentes de información.

## Dataset
En este caso debido a la versatilidad de la implementación del código fuente es posible utilizar el mismo código para extraer información de diferentes repositorios del portal. En este caso se realizará la integración de dos fuentes tenemos:
Empresas activas: Este servicio muestra las empresas activas por provincia y condición jurídica (2017-1999).
Hipotecas: Este servicio muestra las Hipotecas constituidas sobre el total de fincas por provincias y por meses(2003-2018).
empresas_hipotecas_españa_2013_2017.csv


## Miembros del equipo

La actividad ha sido realizada de manera grupal por **Juan Pablo Upoff** y **Miguel Alejandro Ponce**.

## Ficheros del código fuente

* **src/web-scraper-esri.py**: punto de entrada al programa. Inicia el proceso de scraping. Contiene la implementación multihilo para extraer un conjunto de datos inicala a partir de la base de las bases de datos online [Hipoetecas(2003-2018)](https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089) y [Empresas(2017-1999)](https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089).
* **src/data**: contiene los datos extraidos de las fuentes sin trateminto.
* 

## Recursos

1. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). _Web Scraping with Python: Collecting Data from the Modern Web_. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.

### Ejemplo Salida

```js
MainThread run_blocking_tasks: Inicia tarea procesamiento
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:48721/devtools/browser/9366e5b0-7020-48c4-948d-99cda53d3932
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-0_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-0_0 run_blocking_tasks: Ruta: ./data/hipotecas-constituidas_1.csv
ThreadPoolExecutor-0_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=2
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:33175/devtools/browser/2fee17aa-2c01-459d-b4ed-bccc68d31333
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-1_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-1_0 run_blocking_tasks: Ruta: ./data/hipotecas-constituidas_2.csv
ThreadPoolExecutor-1_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=3
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:52799/devtools/browser/5f353a8c-f4c5-4b71-b29a-611a383501b7
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-2_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-2_0 run_blocking_tasks: Ruta: ./data/hipotecas-constituidas_3.csv
ThreadPoolExecutor-2_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=4
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:41403/devtools/browser/2ac236e1-ee35-4832-a4f2-b711354fa2e1
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-3_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-3_0 run_blocking_tasks: Ruta: ./data/hipotecas-constituidas_4.csv
ThreadPoolExecutor-3_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=5
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:39743/devtools/browser/cb7df125-92de-4548-a5f7-5065e78eed01
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-4_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-4_0 run_blocking_tasks: Ruta: ./data/hipotecas-constituidas_5.csv
ThreadPoolExecutor-4_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Finaliza tarea procesamiento
MainThread run_blocking_tasks: Peticiones hipotecas reprocesar [<__main__.Peticion object at 0x7fe16952bfa0>, <__main__.Peticion object at 0x7fe169441a30>, <__main__.Peticion object at 0x7fe168cb2d60>, <__main__.Peticion object at 0x7fe1694480d0>, <__main__.Peticion object at 0x7fe16314bbe0>]
MainThread run_blocking_tasks: Inicia tarea procesamiento
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:57479/devtools/browser/a3810944-51f4-47e3-b3ef-d98135c07e59
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-5_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-5_0 run_blocking_tasks: Ruta: ./data/empresas-activas_1.csv
ThreadPoolExecutor-5_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=2
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:33395/devtools/browser/b6a2ea0d-2b34-43e8-a7ef-f2b4734228b3
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-6_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-6_0 run_blocking_tasks: Ruta: ./data/empresas-activas_2.csv
ThreadPoolExecutor-6_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=3
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:60217/devtools/browser/2efaafbe-d15e-4b64-9095-3bb99b2ea331
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-7_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-7_0 run_blocking_tasks: Ruta: ./data/empresas-activas_3.csv
ThreadPoolExecutor-7_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=4
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:44637/devtools/browser/85f69fce-a046-4437-a39a-824c3ba02311
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-8_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-8_0 run_blocking_tasks: Ruta: ./data/empresas-activas_4.csv
ThreadPoolExecutor-8_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=5
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:41139/devtools/browser/d1adf312-bf44-4240-a89b-2198a665ade5
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-9_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-9_0 run_blocking_tasks: Ruta: ./data/empresas-activas_5.csv
ThreadPoolExecutor-9_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Finaliza tarea procesamiento
MainThread run_blocking_tasks: Peticiones empresas reprocesar [<__main__.Peticion object at 0x7fe16952bfd0>, <__main__.Peticion object at 0x7fe16943b8b0>, <__main__.Peticion object at 0x7fe163180130>, <__main__.Peticion object at 0x7fe163180a90>, <__main__.Peticion object at 0x7fe16849a5e0>]
MainThread run_blocking_tasks: Finaliza procesamiento
```
