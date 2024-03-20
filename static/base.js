function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML =
        this.responseText;
      }
    };
    xhttp.open("GET", "/Users/elliotframe/GameScoreCentral/ajax-info.txt", true);
    xhttp.send();
  }


function loadReview() {
    document.getElementById("demo").innerHTML = "NICE";
}

function loadReviewBox(games) {
    document.getElementById("demo").innerHTML = "<form method='post'>{% csrf_token %} {{ form.as_p }}<button type='submit' class='btn btn-primary' id='buttonMiddle'>Confirm Changes</button></form>";
}

//Code irrelevant just used to figure out JS



