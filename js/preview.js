import "./three.js";
import {OrbitControls} from "./OrbitControls.js";
import { normal_chair } from "./normal_chair.js";

let camera, scene, renderer;
let geometry, material, mesh, controls;
/*
window.onload = function () {
  let inputLength = document.getElementById("length");
  let inputWidth = document.getElementById("width");
  let inputHeight = document.getElementById("height");

  if (inputLength && inputHeight && inputWidth) {
    inputLength.addEventListener("keyup", inputupdate);
    inputWidth.addEventListener("keyup", inputupdate);
    inputHeight.addEventListener("keyup", inputupdate);
  }

  function inputupdate() {
    let length = document.getElementById("length").value / 100;
    let width = document.getElementById("width").value / 100;
    let height = document.getElementById("height").value / 100;
    if (length != "" && width != "" && height != "") {
      mesh.clear();
      mesh = normal_chair(length, width, height);
      scene.add(mesh);
    }
  }
};
*/

init(1, 1, 1);
function init(length, width, height) {
  camera = new THREE.PerspectiveCamera(
    70,
    2/3,
    0.01,
    10
  );
  camera.position.z = 5;
  scene = new THREE.Scene();

  mesh = normal_chair(length, width, height);
  scene.add(mesh);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(200,300);
  renderer.setAnimationLoop(animation);
  //controls = new DragControls( mesh.children, camera, renderer.domElement );
  controls = new OrbitControls( camera, renderer.domElement );
  renderer.render(scene, camera);
  

  document.getElementById("preview").appendChild(renderer.domElement);
}

function animation(time) {
  //mesh.rotation.x = time / 2000;
  //mesh.rotation.y = time / 1000;
  renderer.render(scene, camera);
}
