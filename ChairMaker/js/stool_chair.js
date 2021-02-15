import "./three.js";

export function stool_chair(diam, height) {
  const material = new THREE.MeshBasicMaterial({ color: 0x008cff });
  const seatGeo = new THREE.CylinderGeometry(diam, diam, height / 10, 64);
  const legGeo = new THREE.CylinderGeometry(
    (diam * 2) / 6,
    (diam * 2) / 6,
    height,
    64
  );
  const bottomGeo = new THREE.CylinderGeometry(
    (diam * 2) / 3,
    (diam * 2) / 3,
    height / 12,
    64
  );

  const leg = new THREE.Mesh(legGeo, material);
  const seat = new THREE.Mesh(seatGeo, material);
  const bottom = new THREE.Mesh(bottomGeo, material);

  leg.position.set(0, height / 2 + height / 12, 0);
  bottom.position.set(0, height / 24, 0);
  seat.position.set(0, (height * 27) / 24, 0);

  const chair = new THREE.Group();

  chair.add(leg);
  chair.add(seat);
  chair.add(bottom);

  return chair;
}
