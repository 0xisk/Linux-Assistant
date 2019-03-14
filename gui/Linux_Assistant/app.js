const electron = require('electron'),
       {app, BrowserWindow , Menu} = electron ;
let mainWin ;
let {pyshell} =  require('python-shell');


let appMenu = [
    {
        label : "menue 1"
    },
    {
        label : "menue 2"
    }
]
    
app.on('ready', () => {
    mainWin = new BrowserWindow({
        // fullscreen:true
    });
    // mainWin.loadURL('file:///' + __dirname+ '/index.html')

    mainWin.loadFile('index.html')
    
    // mainWin.maximize()
    
    mainWin.on('closed',()=>{ app.quit() })
   
   
    let mainMenu = Menu.buildFromTemplate(appMenu)

    // Menu.setApplicationMenu(mainMenu)
    // function createWindow () {
    //     /*...*/
    //     var python = require('child_process').spawn('python', ['./hello.py']);
    //     python.stdout.on('data',function(data){
    //         console.log("data: ",data.toString('utf8'));
    //     });
    //  }

     

// pyshell.run('hello.py',  function  (err, results)  {
//  if  (err)  throw err;
//  console.log('hello.py finished.');
//  console.log('results', results);
// });
})    
