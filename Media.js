function sentenceFilter() {
    var xhttp = new XMLHttpRequest();
    var query = encodeURI("Ouragan Irma en direct : au moins neuf morts dans les Antilles françaises.");
    xhttp.open("GET", "https://api.textgain.com/1/tag?q=" + query + "&lang=fr&key=***", false);
    // xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send();
    var response = JSON.parse(xhttp.responseText);
    console.log('response : ', response);
    var responseLength = response.text.length;
    var sentenceLength = 0;
    var groupLength = 0;
    var arrayValue = ['NOUN'];
    for (var i = 0; i < responseLength; i++){
        sentenceLength = response.text[i].length;
        console.log("other sentence :");
        for (var a = 0; a < sentenceLength; a++) {
            groupLength = response.text[i][a].length;
            for (var b = 0; b < groupLength; b++) {
                if (arrayValue.indexOf(response.text[i][a][b].tag) > -1) {
                    console.log('tag : ', response.text[i][a][b].tag);
                    console.log('word : ', response.text[i][a][b].word);
                }
            }
        }

    }

}
