//import "./three.js";

export function modern_chair(length, width, height, wireframe) {
  const material = new THREE.MeshStandardMaterial({
    color: 0x008cff,
    wireframe: wireframe,
  });

  const legGeo = new THREE.BoxGeometry(length, height, width * 0.2);
  const seatGeo = new THREE.BoxGeometry(length, height * 0.5, width * 0.6);
  const backGeo = new THREE.BoxGeometry(
    length * 0.2,
    height * 0.5,
    width * 0.6
  );

  const leftLeg = new THREE.Mesh(legGeo, material);
  const rightLeg = new THREE.Mesh(legGeo, material);

  const seat = new THREE.Mesh(seatGeo, material);

  const back = new THREE.Mesh(backGeo, material);

  leftLeg.castShadow = true;
  rightLeg.castShadow = true;
  seat.castShadow = true;
  back.castShadow = true;

  leftLeg.position.set(0, height * 0.5, width * 0.4);
  rightLeg.position.set(0, height * 0.5, width * -0.4);

  seat.position.set(0, height * 0.25, 0);

  back.position.set(length * -0.4, height * 0.75, 0);

  const chair = new THREE.Group();
  chair.add(leftLeg);
  chair.add(rightLeg);
  chair.add(seat);
  chair.add(back);

  return chair;
}
