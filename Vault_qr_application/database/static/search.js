document.querySelector("#search-drop-down").onclick = function(){
    var menu = document.getElementById("dropdown-menu-search");
    menu.classList.toggle("active");
} 

document.querySelector("#sort-drop-down").onclick = function(){
    var menu = document.getElementById("dropdown-menu-sort");
    menu.classList.toggle("active");
} 

const searchContainer = document.querySelector(".search-cont");
const inputForm = searchContainer.querySelector("input");
const result = document.querySelector(".result-container");

inputForm.onkeyup = (e) =>{
    let input = e.target.value;
    let emptyarray = [];
    if (input) {
        result.classList.add("active");
    }else{
        result.classList.remove("active");
    }
    showSuggestion(emptyarray);
}

function showSuggestion(list){
    let listData;
    if (!list.length){
        userValue = inputForm.value;
        listData = `<li>${userValue}<li>`;
    }else{
        listData = list.join('');
    }
    result.innerHTML = listData;
}
