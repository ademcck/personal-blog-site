
const icon = document.querySelector('.icon');
const search = document.querySelector('.search');
const s_a = document.getElementById("s_a");
const choice = document.querySelector(".choice");

document.addEventListener("click",(e)=>{
    const category = document.getElementsByClassName("mainmenu");
    const statuss = category[0].children[0].getAttribute("status");
    const ul = document.getElementById("ul-style");
    const b_1 = document.getElementById("b_1");
    const b_2 = document.getElementById("b_2");
    if (e.target.className == "icon"){
        control(); 
        if (e.target.parentElement.className == "search active"){
            setTimeout(()=>{
                demo();
            },500);
        }
    }
    if (e.target.className == "clear"){
        e.target.previousSibling.previousSibling.children[0].value = "";
    }
    
    if (e.target.id == "b_1"){
        b_1.style.background = "rgb(0, 118, 173)";
        b_1.style.border = "#fff";
        b_1.style.color = "#fff";
        b_2.style.background = "none";
        b_2.style.border = "none";
        b_2.style.color = "rgb(112, 112, 112)";
    }else if (e.target.id == "b_2"){
        b_2.style.background = "rgb(0, 118, 173)";
        b_2.style.border = "#fff";
        b_2.style.color = "#fff";
        b_1.style.background = "none";
        b_1.style.border = "none";
        b_1.style.color = "rgb(112, 112, 112)";
    }
    if (window.screen.availWidth <= 750){
        
        if (e.target.id == "category" && statuss == "false"){
            search.style.removeProperty("transition");
            search.style.visibility= "hidden";
            ul.style.height = "360px";
            category[0].children[0].setAttribute("status","true");

        }else if (e.target.id == "category" && statuss == "true"){
            ul.style.height = "0%";
            category[0].children[0].setAttribute("status","false");
            setTimeout(()=>{
                search.style.visibility= "visible";
            },400);
            search.style.transition = ".5s";
            
        }
        else{
            ul.style.height = "0%";
            setTimeout(()=>{
                search.style.visibility= "visible";
            },400);
            search.style.transition = ".5s";
        }
    }else{
        if (e.target.id == "category" && statuss == "false"){
            search.style.removeProperty("transition");
            search.style.visibility= "hidden";
            ul.style.height = "100%";
            category[0].children[0].setAttribute("status","true");
            
        }else if (e.target.id == "category" && statuss == "true"){
            ul.style.height = "0%";
            category[0].children[0].setAttribute("status","false");
            setTimeout(()=>{
                search.style.visibility= "visible";
            },400);
            search.style.transition = ".5s";
        }else{
            ul.style.height = "0%";
            setTimeout(()=>{
                search.style.visibility= "visible";
            },400);
            search.style.transition = ".5s";
        }

    }

})

function control(){
    let ch = document.querySelector(".choice");
    if (window.screen.availWidth <= 412){
        if (ch.getAttribute("status") == "true"){
            ch.style.visibility = "hidden";
            ch.setAttribute("status","false");
        }else if(ch.getAttribute("status") == "false"){
            setTimeout(e=>{
                ch.style.visibility = "visible";
            },200);
            ch.setAttribute("status","true");
        }
    }
}

function sleep(){
        
    return new Promise(resolve => setTimeout(resolve, 150));
}
async function demo(elemet) {
    let text = "Search...";
    for (var i = 0; i < text.length; i++){
        document.getElementById("mysearch").placeholder += text.charAt(i);
        await sleep();
    };
    for (var i = text.length; i >= 0; i--){
        document.getElementById("mysearch").placeholder = text.slice(0,i);
        await sleep();
    };
    // document.getElementById("mysearch").focus();
    
}
icon.onclick = function(){
    search.classList.toggle('active')
}