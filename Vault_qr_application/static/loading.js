var messages = ["Crawling the Blockchain",
  "Finding a Node",
  "Minting Smart Contract",
  "Creating a New Block",
  "Making the Transaction",
  "Distributing Accross Chain",
  "Adding Finishing Touches"
]


function loopThroughMessages(messages) {
    for (var i = 0; i < messages.length; i++) {
        // for each iteration console.log a word
        // and make a pause after it
        (function (i) {
            setTimeout(function () {
                document.getElementById('loading').innerHTML = messages[i];
                console.log(messages[i]);
            }, 5000 * i);
        })(i);
    };
}


function navigate() {
    window.location.href = 'results';  // redirect to results page when done!
    
}



 // deploy the contract while the loading screen goes then navigate to results page
const data = fetch('deploy', {
    method: 'GET',
    credentials: 'include'
  }).then(navigate);
  

loopThroughMessages(messages);
