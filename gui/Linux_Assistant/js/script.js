const {ipcRenderer} = require('electron')
const http = require('http');
const fs = require('fs');
const os = require('os');

console.log('Application Started ...');

function showMsgHistroy() {

    let osUserName = os.userInfo().username;

    fs.readFile(`/home/${osUserName}/Tracking/2019/05/log.csv`, (e, data) => {
        console.log('Hey Iam fs Function ...');
        if (e) throw e;
        let prepData = data.toString().split("\n");

        for (let i = 0; i < prepData.length; i++) {
            let lineData, DOMStrings, detailedData, msgHTML, newMsgHTML;

            DOMStrings = {
                msgHistory: '.msg_history'
            };

            console.log(`I'm line ${i}`);
            console.log(`\n`);

            lineData = prepData[i].split(',');
            console.log(lineData)

            detailedData = {
                incMsg: lineData[0],
                repMsg: lineData[1],
                command: lineData[2],
                msgDate: lineData[4],
                msgTime: lineData[5]
            };

            // Create HTML string with placeholder text

            msgHTML = '<div class="outgoing_msg">\n' +
                '\t\t\t\t  <div class="sent_msg">\n' +
                '\t\t\t\t\t<p>%income%</p>\n' +
                '\t\t\t\t\t<span class="time_date"> %time%    |    %date%</span> </div>\n' +
                '\t\t\t\t</div>' +
                '<div class="incoming_msg">\n' +
                '\t\t\t\t <div class="incoming_msg_img"> <img src="linux.png" alt="sunil"> </div>\n' +
                '\t\t\t\t  <div class="received_msg">\n' +
                '\t\t\t\t\t<div class="received_withd_msg">\n' +
                '\t\t\t\t\t  <p>%reply%</p>\n' +
                '\t\t\t\t\t  <span class="time_date"> %time%    |    %date%</span></div>\n' +
                '\t\t\t\t  </div>\n' +
                '\t\t\t\t</div>'

            // Replace the placeholder text with some actual data

            newMsgHTML = msgHTML.replace('%reply%', detailedData.repMsg);
            newMsgHTML = newMsgHTML.replace('%income%', detailedData.incMsg);
            newMsgHTML = newMsgHTML.replace('%time%', detailedData.msgTime);
            newMsgHTML = newMsgHTML.replace('%date%', detailedData.msgDate);

            document.querySelector(DOMStrings.msgHistory).insertAdjacentHTML('afterend', newMsgHTML);
        }
    });
}
// function getUsage() {
//     var xhttp = new XMLHttpRequest();
//     function toTwoArrays(j) {
//         if(j == null) { return [[],[]]; }
//         data = JSON.parse(j);
//         var keys = Object.keys(data)
//         var values = Object.values(data)
//         return [keys , values]
//     }
//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//             // document.getElementById("test").innerHTML = xhttp.responseText;
//             document.getElementById("test").innerHTML = xhttp.responseText

//         }
//     };
//     try {
//         xhttp.open("GET", "http://localhost:9000/usage", true);
//         xhttp.send();
//     }
//     catch(err) {}
// }

//-----------------------------------------------------------------------------

function scrollButtom(eid) {
    var objDiv = document.getElementById(eid);
    objDiv.scrollTop = objDiv.scrollHeight;
}

//-----------------------------------------------------------------------------

// function sendQuery() {
//     var q = document.getElementById("input").value; 
//     if(q.replace(" ","") == "") return;
//     appendReply(q)

//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//             appendSend(xhttp.responseText)
//             scrollButtom("msg_history")
//         }
//     };    
//     try {
//         xhttp.open("POST", "http://localhost:9000/text", true);
//         xhttp.send(q);
//     }
//     catch(err) {
//         appendSend("Sorry an error has been occured")
//         scrollButtom("msg_history")
//     }
	
// }

//----------------------------------------------------------------------------

function sendQuery() {
    var q = document.getElementById("input").value; 
    if(q.replace(" ","") == "") return;
    appendReply(q)

    var xhttp = new XMLHttpRequest();
    
    try {
        xhttp.open("POST", "http://localhost:9000/text", false);
        xhttp.send(q);
        appendSend(xhttp.responseText)
        scrollButtom("msg_history")

    }
    catch(err) {
        appendSend("Sorry an error has been occured")
        scrollButtom("msg_history")
    }
    
}

//----------------------------------------------------------------------------

function appendSend(msg) {
    var query = '<div class="incoming_msg"><div class="incoming_msg_img"><img src="linux.png" alt="sunil"> </div><div class="received_msg"><div class="received_withd_msg"><p>' + msg + '</p><span class="time_date"></span></div></div></div>';
    document.getElementById("msg_history").innerHTML += query;
}

//----------------------------------------------------------------------------

function appendReply(msg) {
    var query = '<div class="outgoing_msg">'+
                '<div class="sent_msg"><p>' + msg + '</p><span class="time_date"></span></div></div>';
    document.getElementById("msg_history").innerHTML += query;

}

//----------------------------------------------------------------------------

// appendReply("jesus christ is here")
// appendSend("jesus christ is here");


// $('#send').click(function(){
//     var input = document.getElementById("input").value; 
//     if(input.replace(" ","") == "") return;
//     ipcRenderer.send('add', input)
//     ipcRenderer.on('added',(e,data) => document.getElementById("response").innerHTML = data) 
//     appendSend(input)
//     sendQuery(input)
// })


function createBrowserWindow() {
    const remote = require('electron').remote;
    const BrowserWindow = remote.BrowserWindow;
    const win = new BrowserWindow({
    height: 600,
    width: 800
    });
    win.loadFile('chart/samples/vue/bar/bar-with-custom-data-labels.html')
    getUsage()
}