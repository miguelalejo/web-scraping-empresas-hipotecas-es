# Práctica 1: Web scraping
## Descripción

La información se ha seleccionado en un contexto de análisis de recursos información económica e hipotecas de empresas por provincia en España. El sitio web es un recurso de open data para el análisis de información de diversos contenidos de datos abiertos para que se puedan consultar y analizar. Se elige el sitio web debido a que presentan los conjuntos de datos y posibles datos relacionados por tanto es posible realizar cruces de información y generar conjuntos de datos con mayores características.


## Detalle solución y complejidad

Se presenta una solución que permite la extracción de contenido web dinámico, en donde la presentación del contenido corresponde a cargas parciales de secciones cargadas de manera asíncrona. Se hace uso de programación multihilo y procesamiento de tareas para optimizar los tiempos de respuesta diferenciando entre los procesos de extracción de contenido web y la generación de los documentos csv. En este caso se generan inicialmente varios ficheros luego de extraer el contenido de las diferentes pestañas de una página. Luego, se realizará un procesamiento de tratamiento de los datos e integración de la fuentes de información.

## Miembros del equipo

La actividad ha sido realizada de manera grupal por **Juan Pablo Upoff** y **Miguel Alejandro Ponce**.

## Ficheros del código fuente

* **src/web-scraper-esri.py**: punto de entrada al programa. Inicia el proceso de scraping. Contiene la implementación multihilo para extraer un conjunto de datos inicala a partir de la base de las bases de datos online [PlaneCrashInfo](https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089) y [PlaneCrashInfo](https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089).
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
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:33267/devtools/browser/bb6cb87b-2d8b-4fbd-a2af-544b38d96e3c
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-0_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-0_0 run_blocking_tasks: Ruta: hipotecas-constituidas_1.csv
ThreadPoolExecutor-0_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=2
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:38681/devtools/browser/223fde47-ab14-4a75-8112-a702c3212712
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-1_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-1_0 run_blocking_tasks: Ruta: hipotecas-constituidas_2.csv
ThreadPoolExecutor-1_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=3
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:47413/devtools/browser/881db4b9-9731-4424-bcf7-57e539606d0f
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-2_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-2_0 run_blocking_tasks: Ruta: hipotecas-constituidas_3.csv
ThreadPoolExecutor-2_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=4
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:41875/devtools/browser/53aa06e8-8092-4eca-b2a1-79323aa2f5cb
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-3_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-3_0 run_blocking_tasks: Ruta: hipotecas-constituidas_4.csv
ThreadPoolExecutor-3_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=5
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:53753/devtools/browser/5de9463c-14d7-4795-88e5-6f11d127cadf
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-4_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-4_0 run_blocking_tasks: Ruta: hipotecas-constituidas_5.csv
ThreadPoolExecutor-4_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Finaliza tarea procesamiento
MainThread run_blocking_tasks: Peticiones hipotecas reprocesar [<__main__.Peticion object at 0x7ff7aef4f970>, <__main__.Peticion object at 0x7ff7aeefdfa0>, <__main__.Peticion object at 0x7ff7ae6ed310>, <__main__.Peticion object at 0x7ff7ae6c5a30>, <__main__.Peticion object at 0x7ff7aee8b8b0>]
MainThread run_blocking_tasks: Inicia tarea procesamiento
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:57495/devtools/browser/deb8f9a7-3f4b-4f65-ab30-381061e26840
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-5_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-5_0 run_blocking_tasks: Ruta: empresas-activas_1.csv
ThreadPoolExecutor-5_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=2
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:58743/devtools/browser/3df4bc23-4c20-45a6-9643-f16c77d19e41
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-6_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-6_0 run_blocking_tasks: Ruta: empresas-activas_2.csv
ThreadPoolExecutor-6_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=3
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:55161/devtools/browser/d3f70142-90c4-4428-9039-4f28a8759f2c
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-7_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-7_0 run_blocking_tasks: Ruta: empresas-activas_3.csv
ThreadPoolExecutor-7_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=4
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:56485/devtools/browser/d0633309-d069-454d-82f0-f2173e6b2818
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-8_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-8_0 run_blocking_tasks: Ruta: empresas-activas_4.csv
ThreadPoolExecutor-8_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Inicia procesar web-scraping
MainThread run_blocking_tasks: Url: https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089&page=5
[I:pyppeteer.launcher] Browser listening on: ws://127.0.0.1:54585/devtools/browser/b1c00888-a7e7-45ed-8aea-8bc69b7b84ab
[I:pyppeteer.launcher] terminate chrome process...
MainThread run_blocking_tasks: Finaliza procesar web-scraping
ThreadPoolExecutor-9_0 run_blocking_tasks: Inicia exportar csv
ThreadPoolExecutor-9_0 run_blocking_tasks: Ruta: empresas-activas_5.csv
ThreadPoolExecutor-9_0 run_blocking_tasks: Finaliza exportar csv
MainThread run_blocking_tasks: Finaliza tarea procesamiento

```
