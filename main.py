from fastapi import FastAPI
import mysql.connector

import socket

mydb = mysql.connector.connect(
  host="arpudhacloud.tk",
  database='pqurufmu_checkdatabase',
  user="pqurufmu_arpudha",
  password="arpudha@123")

app = FastAPI()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


@app.get("/")
async def root():
     select_count_query = """select total_count from downloadcount where name = "total" """
     cursor = mydb.cursor()
     cursor.execute(select_count_query)
     total_count=cursor.fetchall()
     final_count_value = int(total_count[-1][-1])
     return {"Total Count": final_count_value}

@app.get("/get/{id}")
async def read_item(id):
    return {"item_id": id}

@app.get("/client/get")
async def getClientDetails():
    global hostname;
    global ip_address;
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    return {"Hostname": hostname,
            "IP Address": ip_address
     }
