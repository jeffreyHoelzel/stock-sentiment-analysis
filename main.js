const {app, BrowserWindow} = require("electron");
require("electron-reload")(__dirname);

const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800, 
    height: 600
  });

  mainWindow.loadFile("./src/index.html");
  mainWindow.webContents.openDevTools(); // debugging
}

app.whenReady().then(() => createWindow());
