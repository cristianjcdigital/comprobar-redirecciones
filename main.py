import requests
import time
nuevo_csv = open("new_url.csv", "a", encoding="utf-8")
with open("url.csv", "r") as archivo:
    for linea in archivo:
        linea = linea.rstrip()
        time.sleep(2)
        resp = requests.get(linea, timeout=10.00)
        nuevo_csv.write(linea + ";" + resp.url + "\n")
        print(linea,resp.url)
archivo.close()
nuevo_csv.close()
