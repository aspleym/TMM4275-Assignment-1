//import "./three.js";

export function dining_chair(length, width, height, wireframe) {
  const material = new THREE.MeshStandardMaterial({
    color: 0x008cff,
    wireframe: wireframe,
  });
  const legGeo = new THREE.BoxGeometry(length * 0.1, height * 0.4, width * 0.1);
  const seatGeo = new THREE.BoxGeometry(length, height * 0.1, width);
  const backGeo = new THREE.BoxGeometry(length * 0.1, height * 0.5, width);

  const leg1 = new THREE.Mesh(legGeo, material);
  const leg2 = new THREE.Mesh(legGeo, material);
  const leg3 = new THREE.Mesh(legGeo, material);
  const leg4 = new THREE.Mesh(legGeo, material);

  const seat = new THREE.Mesh(seatGeo, material);

  const back = new THREE.Mesh(backGeo, material);

  leg1.castShadow = true;
  leg2.castShadow = true;
  leg3.castShadow = true;
  leg4.castShadow = true;
  seat.castShadow = true;
  back.castShadow = true;

  leg1.position.set(length * 0.45, 0, width * 0.45);
  leg2.position.set(-length * 0.45, 0, -width * 0.45);
  leg3.position.set(length * 0.45, 0, -width * 0.45);
  leg4.position.set(-length * 0.45, 0, width * 0.45);

  seat.position.set(0, height * 0.25, 0);

  back.position.set(-length * 0.45, height * 0.5, 0);

  const chair = new THREE.Group();

  chair.add(leg1);
  chair.add(leg2);
  chair.add(leg3);
  chair.add(leg4);
  chair.add(seat);
  chair.add(back);

  return chair;
}
