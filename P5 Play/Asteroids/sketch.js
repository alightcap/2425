let backgroundImg;
let planet;
let planetAnimation;
let ship;
let shipImg;

function preload() {
	backgroundImg = loadImage('assets/dark space.png');
	planetAnimation = loadAnimation(
		'assets/planet sprite sheet.png',
		{ frameSize: [100, 100], frames: 60 }
	);

	planetAnimation.frameDelay = 6;

	shipImg = loadImage('assets/ship.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	planet = createPlanet();
	ship = createShip();
}

function draw() {
	background(backgroundImg);

	updateShip();
}

function createShip() {
	let s = new Sprite();
	s.image = shipImg;
	s.diameter = 4;
	s.scale = 5;
	s.thrustForce = 5;
	// s.debug = true;
	s.bearing = -90;
	// s.maxVel = 3;
	// s.maxRotSpeed = 2.5;
	s.rotationForce = 0.05;

	return s;
}

function createPlanet() {
	let p = new Sprite();
	p.addAni('idle', planetAnimation);
	p.scale = 6;
	p.collider = 'none';

	return p;
}

function updateShip() {
	if (kb.pressing('up')) {
		ship.applyForce(ship.thrustForce);
	}

	if (kb.pressing('left')) {
		ship.applyTorque(-ship.rotationForce);
	}

	if (kb.pressing('right')) {
		ship.applyTorque(ship.rotationForce);
	}

	ship.bearing = ship.rotation - 90;

	// ship.velocity.limit(ship.maxVel);
	// if (ship.rotationSpeed > ship.maxRotSpeed) {
	// 	ship.rotationSpeed = ship.maxRotSpeed;
	// // }
	// if (ship.rotationSpeed < -ship.maxRotSpeed) {
	// 	ship.rotationSpeed = -ship.maxRotSpeed;
	// }
}
