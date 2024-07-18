let counter = document.getElementsByClassName("counter")[0];
const linkedinURL = "https://www.linkedin.com/in/german-soto-bab8ab226/*"
const githubURL = "https://github.com/an3wworldfool"
const youtube_link = "https://www.youtube.com/@ANewWorldFool"
const devto_link = "https://dev.to/german_soto_d36c725384787"


document.getElementsByClassName("linkedin-grid")[0].onclick = function(){
  location.href = linkedinURL;
}

document.getElementsByClassName("github-grid")[0].onclick = function(){
  location.href = githubURL;
}

document.getElementsByClassName("youtube-grid")[0].onclick = function(){
  location.href = youtube_link;
}

document.getElementsByClassName("devto-grid")[0].onclick = function(){
  location.href = devto_link;
}


fetch("https://u71izje6c9.execute-api.us-west-2.amazonaws.com/Prod/views")
  .then((response) => {
    console.log(response
      
    )
    response.json()
  })
  .then((json) => {
    console.log(json)
    res = JSON.parse(json["body"]);
    console.log(res);
    counter.innerText = res["views"];
  })

