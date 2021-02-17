import "./three.js";
import { OrbitControls } from "./OrbitControls.js";
import { dining_chair } from "./dining_chair.js";
import { stool_chair } from "./stool_chair.js";
import { modern_chair } from "./modern_chair.js";

let camera, scene, renderer;
let geometry, material, mesh, controls, data;

window.onload = function () {
  // Get chair name from url
  var pageURL = window.location.search.substring(1);

  var tag = document.getElementById("DFA");

  var request = new XMLHttpRequest();
  // Request chair params from python server
  request.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText);
      tag.href = "../../products/" + data["pname"] + ".dfa";
      tag.download = data["pname"] + ".dfa";
      initorder();
      showChair();
    }
  };

  request.open("GET", "http://localhost:8080/info" + "?" + pageURL);
  request.send();
};

function initorder() {
  camera = new THREE.PerspectiveCamera(70, 1 / 1, 0.1, 100);
  camera.position.x = 2.2;
  camera.position.y = 2.6;
  camera.position.z = -3.5;
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0xffffff);

  mesh = dining_chair(0, 0, 0);

  scene.add(mesh);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(300, 300);

  renderer.setAnimationLoop(animation);

  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap; // default THREE.PCFShadowMap

  //Create a PointLight and turn on shadows for the light
  const light = new THREE.PointLight(0xffffff, 1, 100);

  light.position.set(10, 10, 10);
  light.castShadow = true; // default false
  scene.add(light);

  //controls = new DragControls( mesh.children, camera, renderer.domElement );
  controls = new OrbitControls(camera, renderer.domElement);
  renderer.render(scene, camera);

  document.getElementById("orderview").appendChild(renderer.domElement);
}

function animation(time) {
  //mesh.rotation.x = time / 2000;
  //mesh.rotation.y = time / 1000;
  renderer.render(scene, camera);
}

function showChair() {
  if (data["dChair"]) {
    mesh.clear();
    mesh = dining_chair(
      data["seat_length"].value / 100,
      data["seat_width"].value / 100,
      data["seat_height"].value / 10,
      false
    );
    scene.add(mesh);
  } else if (data["mChair"]) {
    mesh.clear();
    mesh = modern_chair(
      data["seat_length"].value / 100,
      data["seat_width"].value / (100 * 0.6),
      data["seat_height"].value / (100 * 0.5),
      false
    );
    scene.add(mesh);
  } else if (data["sChair"]) {
    mesh.clear();
    mesh = stool_chair(
      data["seat_diameter"].value / 100,
      data["leg_height"].value / (100 * 0.8),
      false
    );
    scene.add(mesh);
  }
}
