var messages = ["Crawling the Blockchain",
  "Finding a Node",
  "Writing the Smart Contract",
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
                document.getElementById('loading_txt').innerHTML = messages[i];
                console.log(messages[i]);
            }, 5000 * i);
        })(i);
    };
}


function navigate() {
    window.location.href = 'results';  // redirect to results page when done!
}

fetch('deploy').then(navigate); // load the slow url then navigate


loopThroughMessages(messages);
