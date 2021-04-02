import asyncio
import pyppeteer as pyp
from pyppeteer import launch
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import threading
import logging
from concurrent.futures import ProcessPoolExecutor
import asyncio
import concurrent.futures
import logging
import sys
import time



class Peticion:
    def __init__(self, url, csv):
        self.url = url
        self.csv = csv

    def __str__(self):
        return "url{furl}".format(furl=url)

def tratamiento_cabeceras(cadena):
    return cadena.replace('\n', '').replace(" ", "")

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
    return contenido

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
            contenido = event_loop.run_until_complete(procesar_web_scraping(peticion,nfilas))                        
        except Exception as e:            
            log.info("Error al procesar la url:{furl}".format(furl=url))  
        finally:
            peticiones_reproceso.append(peticion)    
    log.info('Finaliza tarea procesamiento')
    return peticiones_reproceso


if __name__ == '__main__':    
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )
    
    nfilas = 10
    event_loop = asyncio.get_event_loop()
    log = logging.getLogger('run_blocking_tasks')
    url_base = 'https://opendata.esri.es/datasets/hipotecas-constituidas-sobre-fincas/data?geometry=-36.558%2C29.677%2C22.725%2C42.089'
    cvs_path = './data/hipotecas-constituidas_{fname}.csv'    
    npaginas = 5
    nMaxfilas = 3
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
    
                   
                   
    
    