var request = new XMLHttpRequest();
// Request chair params from python server
var data = "";
request.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    data = JSON.parse(this.responseText);
    console.log(data);
    setConstraints(data);
  }
};

request.open("GET", "http://localhost:8080/chairConstraints");
request.send();

function setConstraints(data) {
  const dCHeight = document.getElementById("dCHeight");
  const dCLength = document.getElementById("dCLength");
  const dCWidth = document.getElementById("dCWidth");
  const sCHeight = document.getElementById("sCHeight");
  const sCDiam = document.getElementById("sCDiam");
  const mCHeight = document.getElementById("mCHeight");
  const mCLength = document.getElementById("mCLength");
  const mCWidth = document.getElementById("mCWidth");
  dCHeight.min = data["dCConstL"]["seat_height"].value * 10;
  dCHeight.max = data["dCConstU"]["seat_height"].value * 10;
  dCLength.min = data["dCConstL"]["seat_length"].value;
  dCLength.max = data["dCConstU"]["seat_length"].value;
  dCWidth.min = data["dCConstL"]["seat_width"].value;
  dCWidth.max = data["dCConstU"]["seat_width"].value;
  sCHeight.min = data["sCConstL"]["leg_height"].value / 0.8;
  sCHeight.max = data["sCConstU"]["leg_height"].value / 0.8;
  sCDiam.min = data["sCConstL"]["seat_diameter"].value;
  sCDiam.max = data["sCConstU"]["seat_diameter"].value;
  mCHeight.min = data["mCConstL"]["seat_height"].value / 0.5;
  mCHeight.max = data["mCConstU"]["seat_height"].value / 0.5;
  mCLength.min = data["mCConstL"]["seat_length"].value;
  mCLength.max = data["mCConstU"]["seat_length"].value;
  mCWidth.min = data["mCConstL"]["seat_width"].value / 0.6;
  mCWidth.max = data["mCConstU"]["seat_width"].value / 0.6;
}
