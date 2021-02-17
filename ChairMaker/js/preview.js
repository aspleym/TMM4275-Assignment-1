import "./three.js";
import { OrbitControls } from "./OrbitControls.js";
import { dining_chair } from "./dining_chair.js";
import { stool_chair } from "./stool_chair.js";
import { modern_chair } from "./modern_chair.js";

let camera, scene, renderer;
let geometry, material, mesh, controls;

window.onload = function () {
  // DiningChair
  let dCLength = document.getElementById("dCLength");
  let dCWidth = document.getElementById("dCWidth");
  let dCHeight = document.getElementById("dCHeight");
  //StoolChair
  let sCDiam = document.getElementById("sCDiam");
  let sCHeight = document.getElementById("sCHeight");
  //ModernChair
  let mCLength = document.getElementById("mCLength");
  let mCWidth = document.getElementById("mCWidth");
  let mCHeight = document.getElementById("mCHeight");

  let select = document.getElementById("chairType");
  let wireframe = document.getElementById("wireframe");

  if (
    dCLength &&
    dCHeight &&
    dCWidth &&
    sCDiam &&
    sCHeight &&
    mCLength &&
    mCHeight &&
    mCWidth
  ) {
    dCLength.addEventListener("change", inputupdate);
    dCWidth.addEventListener("change", inputupdate);
    dCHeight.addEventListener("change", inputupdate);

    sCDiam.addEventListener("change", inputupdate);
    sCHeight.addEventListener("change", inputupdate);

    mCLength.addEventListener("change", inputupdate);
    mCWidth.addEventListener("change", inputupdate);
    mCHeight.addEventListener("change", inputupdate);

    select.addEventListener("change", changeChair);
    wireframe.addEventListener("change", inputupdate);
  }

  function inputupdate() {
    if (select.value == "diningChair") {
      let length = dCLength.value / 100;
      let width = dCWidth.value / 100;
      let height = dCHeight.value / 100;
      if (length != "" && width != "" && height != "") {
        mesh.clear();
        mesh = dining_chair(length, width, height, wireframe.checked);
        scene.add(mesh);
      }
    } else if (select.value == "stoolChair") {
      let diam = sCDiam.value / 100;
      let height = sCHeight.value / 100;
      if (diam != "" && height != "") {
        mesh.clear();
        mesh = stool_chair(diam, height, wireframe.checked);
        scene.add(mesh);
      }
    } else if (select.value == "modernChair") {
      let length = mCLength.value / 100;
      let width = mCWidth.value / 100;
      let height = mCHeight.value / 100;
      if (length != "" && width != "" && height != "") {
        mesh.clear();
        mesh = modern_chair(length, width, height, wireframe.checked);
        scene.add(mesh);
      }
    }
  }

  function changeChair() {
    if (select.value == "diningChair") {
      mesh.clear();
      mesh = dining_chair(1, 1, 1, wireframe.checked);
      scene.add(mesh);
    } else if (select.value == "stoolChair") {
      mesh.clear();
      mesh = stool_chair(1, 1, wireframe.checked);
      scene.add(mesh);
    } else if (select.value == "modernChair") {
      mesh.clear();
      mesh = modern_chair(1, 1, 1, wireframe.checked);
      scene.add(mesh);
    }
  }
};

init();
function init() {
  camera = new THREE.PerspectiveCamera(70, 2 / 3, 0.1, 100);
  camera.position.x = 2.2;
  camera.position.y = 2.6;
  camera.position.z = -3.5;
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0xffffff);

  mesh = dining_chair(0, 0, 0);

  scene.add(mesh);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(200, 300);

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

  document.getElementById("preview").appendChild(renderer.domElement);
}

function animation(time) {
  //mesh.rotation.x = time / 2000;
  //mesh.rotation.y = time / 1000;
  renderer.render(scene, camera);
}
