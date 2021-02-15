import "./three.js";

export function dining_chair(width, length, height) {
  const material = new THREE.MeshBasicMaterial({ color: 0x008cff });
  const legGeo = new THREE.BoxGeometry(length * 0.1, height, width * 0.1);
  const seatGeo = new THREE.BoxGeometry(length, height * 0.1, width);
  const backGeo = new THREE.BoxGeometry(length, height, width * 0.1);

  const leg1 = new THREE.Mesh(legGeo, material);
  const leg2 = new THREE.Mesh(legGeo, material);
  const leg3 = new THREE.Mesh(legGeo, material);
  const leg4 = new THREE.Mesh(legGeo, material);

  const seat = new THREE.Mesh(seatGeo, material);

  const back = new THREE.Mesh(backGeo, material);

  leg1.position.set(0, 0, 0);
  leg2.position.set(length, 0, width);
  leg3.position.set(0, 0, width);
  leg4.position.set(length, 0, 0);

  seat.position.set(length / 2, height / 2, width / 2);

  back.position.set(length / 2, height, 0);

  const chair = new THREE.Group();
  chair.add(leg1);
  chair.add(leg2);
  chair.add(leg3);
  chair.add(leg4);
  chair.add(seat);
  chair.add(back);

  return chair;
}
