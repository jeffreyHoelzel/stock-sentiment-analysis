const {app, BrowserWindow} = require("electron");
const path = require("path");
// require("electron-reload")(__dirname); // turn off when testing

const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800, 
    height: 600, 
    webPreferences: {
      nodeIntegration: true, 
      contextIsolation: false, 
    }, 
    icon: path.join(__dirname, "src/icons/favicon.ico")
  });

  mainWindow.loadFile("./src/index.html");
  mainWindow.webContents.openDevTools(); // debugging
  mainWindow.setMenu(null);
}

app.whenReady().then(() => createWindow());
