//import "./three.js";

export function stool_chair(diam, height, wireframe) {
  const radius = diam / 2;
  const material = new THREE.MeshStandardMaterial({
    color: 0x008cff,
    wireframe: wireframe,
  });
  const seatGeo = new THREE.CylinderGeometry(radius, radius, height * 0.1, 64);
  const legGeo = new THREE.CylinderGeometry(
    radius * 0.3,
    radius * 0.3,
    height * 0.8,
    64
  );
  const bottomGeo = new THREE.CylinderGeometry(
    radius * 0.7,
    radius * 0.7,
    height * 0.1,
    64
  );

  const leg = new THREE.Mesh(legGeo, material);
  const seat = new THREE.Mesh(seatGeo, material);
  const bottom = new THREE.Mesh(bottomGeo, material);

  leg.castShadow = true;
  seat.castShadow = true;
  bottom.castShadow = true;

  leg.position.set(0, height * 0.45, 0);
  bottom.position.set(0, height * 0.05, 0);
  seat.position.set(0, height * 0.9, 0);

  const chair = new THREE.Group();

  chair.add(leg);
  chair.add(seat);
  chair.add(bottom);

  return chair;
}
