const nawBar = document.getElementById('nawBar');
const profile_user = document.getElementById("profile_user");
const header_choice = document.getElementsByClassName('header_choice');


nawBar.addEventListener("click", (e)=>{
    if (e.target.id == 'nawBar'){
        if (window.screen.availWidth < 768){
            if (nawBar.getAttribute('act') == 'false'){
                profile_user.style.width = window.screen.availWidth + "px";
                profile_user.style.zIndex = "1000";
                profile_user.style.height = window.screen.availHeight + "px";
                nawBar.setAttribute('class','bg-primary p-2 col-sm-12 col-md-2  fas fa-times');
                nawBar.setAttribute('act','true')
            }else if(nawBar.getAttribute('act') == 'true'){
                profile_user.style.width =  "0";
                nawBar.setAttribute('class','bg-primary p-2 col-sm-12 col-md-2  fas fa-bars');
                nawBar.setAttribute('act','false')
            }
        }else{
            if (nawBar.getAttribute('act') == 'false'){
                profile_user.style.width =  "270px";
                profile_user.style.height = '583px'; 
                profile_user.style.zIndex = "1000";
                nawBar.setAttribute('class','bg-primary p-2 col-sm-12 col-md-2  fas fa-times');
                nawBar.setAttribute('act','true')
            }else if(nawBar.getAttribute('act') == 'true'){
                profile_user.style.height = '0';
                profile_user.style.width =  "0";
                nawBar.setAttribute('class','bg-primary p-2 col-sm-12 col-md-2  fas fa-bars');
                nawBar.setAttribute('act','false')
            }
        }
        
    }
});

document.addEventListener('click',e => {
    if (e.target.parentElement.className == "row parrentMenu"){
        Array.from(header_choice).forEach(element => {
            if (element != nawBar){

                element.style.color = "#fff";
                element.style.backgroundColor = "#007bff";
            }
        });
        if (e.target != nawBar){

            e.target.style.color = "#007bff";
            e.target.style.backgroundColor = "#fff"; 
        }
        
    }else{
        //
    }
});