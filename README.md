## About this repository
This repository creates a simple web application that allows controlling a pc remotely.
Available features:
- Shutdown
- Restart
- Logoff
- Lock
- Hibernate
- Sleep
- Pop up a notification
- Turn off the monitor
- Turn on the monitor

Getting system info:
- CPU usage
- Memory usage
- Disk usage

---

### Before starting
Open the terminal and navigate to the directory where you want to install the application. Then, run the following commands to clone the repository and navigate to the project directory.

### Open a virtual environment and install the required packages 
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Run the application
```
python server.py
or venv\Scripts\python server.py (if you are out of the virtual environment)
```

### pm2 commands
```
pm2 start ecosystem.config.js
```