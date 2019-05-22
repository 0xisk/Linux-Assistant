const {ipcRenderer} = require('electron')

function getUsage() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // document.getElementById("test").innerHTML = xhttp.responseText;
        }
    };
    try {
        xhttp.open("GET", "http://localhost:9000/usage", true);
        xhttp.send();
    }
    catch(err) {}
}

//-----------------------------------------------------------------------------

function scrollButtom(eid) {
    var objDiv = document.getElementById(eid);
    objDiv.scrollTop = objDiv.scrollHeight;
}

//-----------------------------------------------------------------------------

function sendQuery() {
    var q = document.getElementById("input").value; 
    if(q.replace(" ","") == "") return;
    appendReply(q)

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            appendSend(xhttp.responseText)
            scrollButtom("msg_history")
        }
    };    
    try {
        xhttp.open("POST", "http://localhost:9000/text", true);
        xhttp.send(q);
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
