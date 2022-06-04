
/*
function darkMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
}
*/

const check = document.getElementById("check")

if (localStorage.getItem("darkMode")===null){
    localStorage.setItem("darkMode","false");
}

const link = document.createElement("link");
link.rel = "stylesheet";
document.getElementsByTagName('HEAD')[0].appendChild(link);


checkStatus()

function checkStatus(){
    if (localStorage.getItem("darkMode")==="true"){       
        check.checked = true;
        document.body.style.backgroundColor = "#0f0f48"
    } else {
        check.checked = false;
        document.body.style.backgroundColor = "#00ffff67"
    }
}

function changeStatus(){
    if (localStorage.getItem("darkMode")==="true"){       
        localStorage.setItem("darkMode", "false")
        document.body.style.backgroundColor = "#00ffff67"
    } else {
        localStorage.setItem("darkMode", "true")
        document.body.style.backgroundColor = "#0f0f48"
    }
}
