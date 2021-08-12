

var messages = ["Crawling the Blockchain",
"Duplicate Detected"
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
    setTimeout(function () {
        window.location.href = 'duplicate'; // redirect to duplicate page after 7 sec
        window.clearTimeout(tID);		// clear time out.
    }, 7000);  
  
}



// this is a convuted af solution to get the cookies but it works
const data = fetch('deploying', {
    method: 'GET',
    credentials: 'include'
  }).then(navigate);


loopThroughMessages(messages);
