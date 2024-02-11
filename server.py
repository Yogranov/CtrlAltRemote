from os import system
from threading import Thread
import json
from flask import Flask, request
import psutil
from win11toast import toast


app = Flask(__name__)

####################
## POST functions ##
####################

@app.route('/sleep', methods=['GET'])
def put_pc_to_sleep():
    system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
    return json.dumps({"message": "PC is going to sleep"})

@app.route('/restart', methods=['GET'])
def restart_pc():
    system('shutdown /r /t 1')
    return json.dumps({"message": "PC is restarting"})

@app.route('/shutdown', methods=['GET'])
def shutdown_pc():
    system('shutdown /s /t 1')
    return json.dumps({"message": "PC is shutting down"})

@app.route('/notify', methods=['POST'])
def notify():
    title = request.json['title']
    message = request.json['msg']
    Thread(target=toast, args=(title, message)).start()

    return json.dumps({"message": "Notification sent"})

###################
## GET functions ##
###################

@app.route('/cpu')
def cpu():
    return json.dumps({"cpu": psutil.cpu_percent(interval=1)})

@app.route('/ram')
def ram():
    ram_info = psutil.virtual_memory()
    ram_gb = {
        "total": round(ram_info.total / (1024 ** 3), 2),
        "available": round(ram_info.available / (1024 ** 3), 2),
        "used": round(ram_info.used / (1024 ** 3), 2),
        "free": round(ram_info.free / (1024 ** 3), 2),
        "percent": ram_info.percent
    }
    return json.dumps({"ram": ram_gb})

@app.route('/disk')
def disk():
    disks = {}
    for partition in psutil.disk_partitions():
        disk_name = partition.mountpoint
        disk_usage = psutil.disk_usage(partition.mountpoint)
        max_capacity_gb = disk_usage.total / (1024 ** 3)  # Convert bytes to GB
        free_storage_gb = disk_usage.free / (1024 ** 3)  # Convert bytes to GB
        disks[disk_name] = {
            "max_capacity": round(max_capacity_gb, 2),  # Round to 2 decimal places
            "free_storage": round(free_storage_gb, 2),  # Round to 2 decimal places
            "free_storage_percentage": disk_usage.percent
        }
    return json.dumps({"disks": disks})

@app.route('/')
def index():
    return "Hello, world!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
