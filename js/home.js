var help = document.getElementById("help");
var helpWindow = document.getElementById("help-window");
var helpWindowContainer = document.getElementById("help-window-container");
help.addEventListener("click", clickHelp);

function clickHelp(){
    if (helpWindow.classList.contains("active")){
        helpWindowContainer.classList.remove("active");
        helpWindow.classList.remove("active");
        help.classList.remove("active");
    } else {
        helpWindowContainer.classList.add("active");
        helpWindow.classList.add("active");
        help.classList.add("active");
    }
}


var closeHelp = document.getElementById("close-help");
closeHelp.addEventListener("click", clickHelpClose);

function clickHelpClose(){
    helpWindowContainer.classList.remove("active");
    helpWindow.classList.remove("active");
    help.classList.remove("active");
}