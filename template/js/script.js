const {ipcRenderer} = require('electron');
const http = require('http');
const fs = require('fs');
const os = require('os');
const {exec} = require('child_process');

console.log('Application Started ...');

let osUserName = os.userInfo().username;


function checkTrackingFiles() {

    let trackingData = {
        years: 0,
        allMonths: []
    };

    console.log('4');

    fs.readdir(`/home/${osUserName}/Tracking`, (e, year) => {

        if (e) throw e;

        trackingData.years = year.sort(function(a, b){return b - a});

        trackingData.years.forEach((eachYear) => {
            fs.readdir(`/home/${osUserName}/Tracking/${eachYear}`, (e, month) => {

                if (e) throw e;

                trackingData.allMonths.push(month.sort(function(a, b){return b - a}))

                if (trackingData.years.length === trackingData.allMonths.length) {
                    showMsgs(trackingData);
                }
            });
        });
    });
}

function showMsgs(trackingFilesData) {

    console.log('1');

    console.log(trackingFilesData);
    console.log(trackingFilesData.years);

    console.log('2');
    for (let i = 0; i < trackingFilesData.years.length; i++) {

        console.log('3');


        for (let j = 0; j < trackingFilesData.allMonths[i].length ; j++) {
            trackingFilesData.allMonths[i].forEach((month) => {
                fs.readFile(`/home/${osUserName}/Tracking/${trackingFilesData.years[i]}/${month}/log.csv`, (e, data) => {
                    let prepData;


                    console.log('Hey Iam fs.readFile Function ...');
                    if (e) throw e;

                    prepData = data.toString().split("\n");

                    // loop on each line in the data to represent it
                    for (let i = 0; i < prepData.length; i++) {
                        let lineData, DOMStrings, detailedData, msgHTML, newMsgHTML;

                        DOMStrings = {
                            msgHistory: '#msg_history'
                        };

                        console.log(`I'm line ${i}`);
                        console.log(`\n`);

                        lineData = prepData[i].split(',');
                        console.log(lineData);

                        detailedData = {
                            incMsg: lineData[0],
                            repMsg: lineData[1],
                            command: lineData[2],
                            msgDate: lineData[4],
                            msgTime: lineData[5]
                        };

                        // Create HTML string with placeholder text
                        msgHTML = '<ul>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t<!User Query>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t<li>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t<img src="dist/img/face.jpg" alt="avatar">\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t<div class="content">\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="message">\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="bubble">\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p>%reply%</p>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t</div>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t<span>%date% | %time%</span>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t</div>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t</li>\n' +
                            '\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t<!User Query>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t<li>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t<div class="content">\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="message">\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="bubble">\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<p>%reply%</p>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t</div>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t\t<span>%date% | %time%</span>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t\t</div>\n' +
                            '\t\t\t\t\t\t\t\t\t\t\t</li>\n' +
                            '\t\t\t\t\t\t\t\t\t\t</ul>';

                        // Replace the placeholder text with some actual data

                        newMsgHTML = msgHTML.replace('%reply%', detailedData.repMsg);
                        newMsgHTML = newMsgHTML.replace('%income%', detailedData.incMsg);
                        newMsgHTML = newMsgHTML.replace('%time%', detailedData.msgTime);
                        newMsgHTML = newMsgHTML.replace('%date%', detailedData.msgDate);

                        console.log(`newMsgHTML: ${newMsgHTML}`);

                        document.querySelector(DOMStrings.msgHistory).insertAdjacentHTML('afterbegin', newMsgHTML);
                    }
                });

            });
        }
    }
}

 

//-----------------------------------------------------------------------------

function scrollButtom(eid) {
    var objDiv = document.getElementById(eid);
    objDiv.scrollTop = objDiv.scrollHeight;
}

//-----------------------------------------------------------------------------

 

//----------------------------------------------------------------------------
function buildMyMsg()
{
    var q = document.getElementById("input").value; 
    if(q.replace(" ","") == "") return;
    appendReply(q)
    document.getElementById("input").value ="";

    return q;
}

function sendQuery() {
    let q = buildMyMsg();
    var xhttp = new XMLHttpRequest();

    try {
        xhttp.open("POST", "http://localhost:9000/text", false);
        xhttp.send(q)

        console.log(xhttp.responseText)
        var out = JSON.parse(xhttp.responseText)
        appendSend(out["response"])
        // console.log(out["response"])
        // scrollButtom("scroll")

    }
    catch(err) {
        console.log(err)
        appendSend("Sorry an error has been occured")
        // scrollButtom("scroll")
    }
    
}

//----------------------------------------------------------------------------

 

function appendSend(msg) {
    var query = '<div class="msg left-msg">'+
                    ' <div class="msg-img"style="background-image: url(dist/img/face.jpg)"></div>'+
                    '<div class="msg-bubble">'+
                    '<div class="msg-info">'+
                        '<div class="msg-info-name">BOT</div>'+
                    '</div>'+
                    '<div class="msg-text" >'+
                        msg+
                    '</div>'+
                    '</div>'+
                '</div>';
    
    document.getElementById("discussion").innerHTML += query;

    var messageBody = document.querySelector('#discussion');
    messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;
}
//----------------------------------------------------------------------------

function appendReply(msg) {
    var query = '<div class="msg right-msg">'+
                    '<div class="msg-img"style="background-image: url(dist/img/avatar.png)"></div>'+
                    '<div class="msg-bubble">'+
                    '<div class="msg-info" style="color: black">'+
                        '<div class="msg-info-name">Me</div>'+
                    '</div>'+
                    '<div class="msg-text" style="color: black">'+
                    msg+
                    '</div>'+
                    '</div>'+
                '</div>'; 
            
    document.getElementById("discussion").innerHTML += query;
}
//----------------------------------------------------------------------------

function voiceQuery() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            try {
                var json = JSON.parse(xhttp.responseText);
                if(json["query"] != "") { appendReply(json["query"]) }
                appendSend(json["response"])
            }
            catch {
                appendSend("Sorry an error has been occured " + err)
                // scrollButtom("msg_history")
            }
        }
    }
    try {
        xhttp.open("GET", "http://localhost:9000/voice", true);
        xhttp.send();
    }
    catch(err) {
        console.log(err)
    }
}
 


//--------------------------------------------------------------------------

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

