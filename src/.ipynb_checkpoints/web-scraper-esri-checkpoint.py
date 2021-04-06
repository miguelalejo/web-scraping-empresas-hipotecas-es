#Se importan las librerías necesarias
import asyncio
import pyppeteer as pyp
import concurrent.futures
import logging
import sys
import time
import numpy as np
import pandas as pd
import threading
from pyppeteer import launch
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor


#Clase utilizada para relacionar las peticiones hacia las urls y los archivos csv.
class Peticion:
    def __init__(self, url, csv):
        self.url = url
        self.csv = csv

    def __str__(self):
        return "url{furl}".format(furl=url)

def tratamiento_cabeceras(cadena):
    return cadena.replace('\n', '').replace(" ", "")

#Método utilizado como tarea para realizar la exportación de contenido web en un archivo cvs.
#Este métod extrae únicamente el contenidos de las tablas en formato HTML.
#peticion: El cual contiene la URL a procesar y la ruta donde se guardara el resultado cvs del procesamiento.
#contenido: Corresponde al contedio en formato html del sitio procesado.
def procesar_data(peticion,contenido):
    log = logging.getLogger('run_blocking_tasks')
    log.info('Inicia exportar csv')
    log.info('Ruta: {fruta}'.format(fruta=peticion.csv)) 
    soup = BeautifulSoup(contenido,'lxml')
    table = soup.find('table')
    table_heads = table.find_all('tr')
    lista_cabeceras = []
    for th in table_heads:
        td = th.find_all('th')
        row = [tr.text for tr in td]
        lista_cabeceras.append(row)
    cabeceras = [tratamiento_cabeceras(cad) for cad in lista_cabeceras[0]]    
    table_rows = table.find_all('tr')
    filas = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        filas.append(row)
    df = pd.DataFrame(filas,columns=cabeceras)
    df.to_csv(peticion.csv)
    log.info('Finaliza exportar csv')
        
#Método ascricronico para realizar el web-scraping, se definen los parámetros. 
#Este método procesa peticiones de manera asincrona utiliznado las librerías pyppeteer.
#peticion: El cual contiene la URL a procesar y la ruta donde se guardara el resultado del procesamiento.
#nfilas: Corresponde al número de filas en cada pestaña.
async def procesar_web_scraping(peticion,nfilas): 
    log = logging.getLogger('run_blocking_tasks')
    log.info('Inicia procesar web-scraping')
    log.info('Url: {furl}'.format(furl=peticion.url))    
    browser = await launch()
    page = await browser.newPage()        
    await page.goto(peticion.url,{'waitUntil' : 'domcontentloaded', 'timeout': 500000})
    await page.waitForSelector('table',{'timeout': 300000})
    await page.waitForFunction("$('.table tr').length >= {nfilas}".format(nfilas=nfilas),{'timeout': 300000})
    contenido = await page.content()    
    await browser.close()
    executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=3,
    )
    log.info('Finaliza procesar web-scraping')
    loop = asyncio.get_event_loop()
    tareas = [loop.run_in_executor(executor, procesar_data, peticion,contenido)]
    await asyncio.wait(tareas)

#Método utilizado para procesar cada uno de las pestañas de una URL, se definen los parámetros. 
#cvs_path: Ruta donde se guardaran los archivos generados.
#nfilas: Corresponde al número de filas en cada pestaña.
#npaginas: Corresponde al número de pestañas del sitio web. 
#nMaxfilas: Corresponde al número máximo de filas a procesar. 
def tarea_procesamiento_web_scraping(url_base,cvs_path,npaginas=1,nfilas=11,nMaxfilas=5):
    log = logging.getLogger('run_blocking_tasks')
    log.info('Inicia tarea procesamiento')    
    lista_peticiones=[]    
    peticiones_reproceso = []    
    
    for i in range(1,(npaginas+1)):
        cvs = cvs_path.format(fname = str(i))
        url = url_base
        peticion = Peticion(url, cvs)        
        nfilas = nfilas if i<(npaginas) else nMaxfilas
        if i>1:
            var_page = '&page={fid}'.format(fid = str(i))
            url = url_base + var_page
            cvs = cvs_path.format(fname = str(i))
            peticion = Peticion(url, cvs)
            lista_peticiones.append(peticion)
        try:            
            event_loop.run_until_complete(procesar_web_scraping(peticion,nfilas))                        
        except Exception as e:            
            log.info("Error al procesar la url:{furl}".format(furl=url))  
        finally:
            peticiones_reproceso.append(peticion)    
    log.info('Finaliza tarea procesamiento')
    return peticiones_reproceso

#Inicio de la aplicacion
if __name__ == '__main__':    
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )
    #Se defiene la URL de donde se van a extraer los datos y otros parámetros.
    #cvs_path: Ruta donde se guardaran los archivos generados.
    #nfilas: Corresponde al número de filas en cada pestaña.
    #npaginas: Corresponde al número de pestañas del sitio web. 
    #nMaxfilas: Corresponde al número máximo de filas a procesar. 
    nfilas = 10
    event_loop = asyncio.get_event_loop()
    log = logging.getLogger('run_blocking_tasks')
    url_base = 'https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089'
    cvs_path = './data/hipotecas-constituidas_{fname}.csv'    
    npaginas = 5
    nMaxfilas = 3
    #Se defiene la URL de donde se van a extraer los datos y otros parámetros.
    #cvs_path: Ruta donde se guardaran los archivos generados.
    #nfilas: Corresponde al número de filas en cada pestaña.
    #npaginas: Corresponde al número de pestañas del sitio web. 
    #nMaxfilas: Corresponde al número máximo de filas a procesar. 
    lista_reprocesamiento_hipotecas = tarea_procesamiento_web_scraping(url_base,cvs_path,npaginas,nfilas,nMaxfilas)
    log.info('Peticiones hipotecas reprocesar {fhip}'.format(fhip=lista_reprocesamiento_hipotecas))
    url_base = 'https://opendata.esri.es/datasets/empresas-activas-por-provincias/data?geometry=-36.558%2C29.677%2C22.725%2C42.089'
    cvs_path = './data/empresas-activas_{fname}.csv'    
    npaginas = 5
    nMaxfilas = 3    
    lista_reprocesamiento_empresas = tarea_procesamiento_web_scraping(url_base,cvs_path,npaginas,nfilas,nMaxfilas)
    log.info('Peticiones empresas reprocesar {femp}'.format(femp=lista_reprocesamiento_empresas))
    event_loop.close()
    log.info('Finaliza procesamiento')
    
                   
                   
    
    