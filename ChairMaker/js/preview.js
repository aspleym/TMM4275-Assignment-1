import "./three.js";
import { OrbitControls } from "./OrbitControls.js";
import { dining_chair } from "./dining_chair.js";
import { stool_chair } from "./stool_chair.js";

let camera, scene, renderer;
let geometry, material, mesh, controls;

window.onload = function () {
  let inputLength = document.getElementById("ttlength");
  let inputWidth = document.getElementById("ttwidth");
  let inputHeight = document.getElementById("theight");
  let select = document.getElementById("chairType");

  if (inputLength && inputHeight && inputWidth) {
    inputLength.addEventListener("keyup", inputupdate);
    inputWidth.addEventListener("keyup", inputupdate);
    inputHeight.addEventListener("keyup", inputupdate);
    select.addEventListener("change", changeChair);
  }

  function inputupdate() {
    let length = document.getElementById("ttlength").value / 100;
    let width = document.getElementById("ttwidth").value / 100;
    let height = document.getElementById("theight").value / 100;
    if (length != "" && width != "" && height != "") {
      mesh.clear();
      mesh = dining_chair(length, width, height);
      scene.add(mesh);
    }
  }

  function changeChair() {
    if (select.value == "diningChair") {
      mesh.clear();
      mesh = dining_chair(1, 1, 1);
      scene.add(mesh);
    } else if (select.value == "stoolChair") {
      mesh.clear();
      mesh = stool_chair(0.5, 0.8);
      scene.add(mesh);
    }
  }
};

init();
function init() {
  camera = new THREE.PerspectiveCamera(70, 2 / 3, 0.01, 10);
  camera.position.z = 5;
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0xffffff);

  mesh = dining_chair(0, 0, 0);
  scene.add(mesh);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(200, 300);

  renderer.setAnimationLoop(animation);
  //controls = new DragControls( mesh.children, camera, renderer.domElement );
  controls = new OrbitControls(camera, renderer.domElement);
  renderer.render(scene, camera);

  document.getElementById("preview").appendChild(renderer.domElement);
}

function animation(time) {
  //mesh.rotation.x = time / 2000;
  //mesh.rotation.y = time / 1000;
  renderer.render(scene, camera);
}
