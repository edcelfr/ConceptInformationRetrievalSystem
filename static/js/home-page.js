var conceptId = 0;
var concepts = [];
var words = [];
var conceptNames = [];
var keywords = [];
var authors = [];
var colleges = [];
var searchText = "";

/*
function loadQueries() {
    let xhttp = new XMLHttpRequest();
    words = document.getElementById("searchbar").value.split(" ");
    for (let i = 0; i < words.length; i++) {
        if (words[i].charAt(0) == "<" && words[i].charAt(words[i].length - 1) == ">") {
            authors.push(words[i].replace("<", "").replace(">", ""));
            alert(authors);
        } else {
            keywords.push(words[i]);
        }
        //if (words[i].charAt(0) == "[" && words[i].charAt(words[i].length - 1)) {
            //authors.push(words[i].replace("[", "").replace("]", ""));
        //}
    }
    
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            
            concepts = JSON.parse(xhttp.response);

            loadStuff();

        }
      };
    xhttp.open("POST", "/query", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    xhttp.send("keywords=" + keywords.join("-"));
}

function loadConcepts(index) {
    document.getElementById("keyword").innerText = 'What do you mean by ' + '"' + words[index] + '"?';
    document.getElementById("definitions").innerHTML = '';
    
    for (let i = 0; i < concepts[index].length; i++) {
        document.getElementById("definitions").innerHTML += '<option value="' + concepts[index][i][0] + '">' + concepts[index][i][1] + '</option>'
    }
}

function loadStuff() {
    document.getElementById("query-modal").style.display = "block";
    document.getElementById("query-modal").style.zIndex = "2";
    let opacity = 0;
    let animationInterval = setInterval(() => {
        if (opacity > 1) {
            loadConcepts(conceptId);
            clearInterval(animationInterval);
        } else {
            opacity += 0.1;
            document.getElementById("query-modal").style.opacity = opacity;
        }
    }, 10)
}

function loadNextConcepts() {
    conceptNames.push(document.getElementById("definitions").value);
    document.getElementById("definitions").value = '';
    conceptId++;
    if (conceptId >= concepts.length) {
        let urlString = "/results?concept=" + conceptNames.join("-") + "&sort=" + document.getElementById("sort").value;
        if (authors.length > 0) {
            urlString += "&authors=" + authors.join("-");
        }
        window.location.href = urlString;
    } else {
        loadConcepts(conceptId);
    }
}
*/
/* ajax sample

let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        
        concepts = JSON.parse(xhttp.response);

        loadStuff();

    }
  };
xhttp.open("POST", "/query", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
xhttp.send("keywords=" + keywords.join("-"));
*/

