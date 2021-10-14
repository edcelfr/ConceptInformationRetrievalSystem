let concepts = [];
let searchText = "";

//getting all required elements
const searchWrapper = document.querySelector(".search_input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".concept");

/*document.onload = () => {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            concepts = JSON.parse(xhttp.response);
            console.log(concepts);
        }
    }; 
    xhttp.open("POST", "/get-concepts-list", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    xhttp.send("keyword=" + searchText);
}*/

//if user press any key and release
inputBox.onkeydown = (e) => {

    


}

inputBox.onkeyup = (e)=>{
    
    let conceptPromise = new Promise((resolve, reject) => {
        console.log(e.key);
        if (e.key == "Backspace") {
            if (searchText.length > 0) {
                searchText = searchText.slice(0, -1);
            }
        } else if (e.key == " "){
            searchText = "";
        } else if ((/[a-zA-Z]/).test(e.key)) {
            searchText += e.key;
        }
        console.log(searchText);
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                concepts = JSON.parse(xhttp.response);
                resolve()
            }
        };
        xhttp.open("POST", "/get-concepts-list", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        xhttp.send("keyword=" + searchText);

    })

    conceptPromise.then((value) => {
        let userData = e.target.value; //user entered data
        let emptyArray = [];
        if(userData){
            for (let i = 0; i < concepts.length; i++) {
                emptyArray.push(concepts[i][0] + ": " + concepts[i][1]);
            }
            emptyArray = emptyArray.map((data)=>{
                return data = '<li>'+ data +'</li>';
            });
            console.log(emptyArray);
            searchWrapper.classList.add("active"); //show concept box
            showConcepts(emptyArray);
            let allList = suggBox.querySelectorAll("li");
            for (let i = 0; i < allList.length; i++) { //adding onclick attribute in all concepts
                allList[i].setAttribute("onclick", "select(this)");
            }

        } else {
            searchWrapper.classList.remove("active"); //hide concept box
        }
    })
    
}

function select(element){
    let selectUserData = element.textContent;
    inputBox.value = selectUserData.split(":")[0]; //passing the concept that the user has selected
    searchWrapper.classList.remove("active"); //hide concept box

}

function showConcepts(list){
    let listData;
    if(!list.length){
        userValue = inputBox.value;
        listData = '<li>'+ userValue +'</li>';
    }else{
        listData = list.join('');
    }
    suggBox.innerHTML = listData;

}