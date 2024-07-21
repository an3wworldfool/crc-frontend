let counter = document.getElementsByClassName("counter")[0];
const linkedinURL = "https://www.linkedin.com/in/german-soto-bab8ab226/*"



document.getElementsByClassName("linkedin-grid")[0].onclick = function(){
  location.href = linkedinURL;
}

fetch("https://u71izje6c9.execute-api.us-west-2.amazonaws.com/Prod/views")
  .then((response) => response.json())
  .then((json) => {
    res = json["views"];
    console.log(res);
    counter.innerText = res;
  })

