module.exports = {
  apps: [
    {
      name: "CtrlAltRemote", 
      script: "venv/Scripts/pythonw.exe", 
      args: ["server.py"],
      watch: ["server.py", "venv"], 
      env: { 
        PORT: 5000,
      },
      log_date_format: "YYYY-MM-DD HH:mm:ss", 
      output: 'log/ctrlaltremote.log' 
    },
  ],
};
