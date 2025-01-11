let backgroundImg;
let lasers;
let laserImg;
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

	// shipImg = loadImage('assets/ship.png');
	shipImg = loadImage('assets/playerShip1_green.png');
	laserImg = loadImage('assets/laserGreen10.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	planet = createPlanet();
	ship = createShip();
	lasers = createLasers();

	lasers.overlaps(ship);
	lasers.overlaps(lasers);

	ship.fire = spawnLaser;
	// laser = new lasers.Sprite();
}

function draw() {
	background(backgroundImg);

	updateShip();
	updateLasers();
}

function createLasers() {
	let l = new Group();
	l.image = laserImg;
	l.radius = 5;
	l.image.offset.y = 10;
	l.moveSpeed = 5;
	l.life = 60 * 2;
	// l.debug = true;

	return l;
}

function createShip() {
	let s = new Sprite();
	s.image = shipImg;
	s.diameter = 20;
	s.thrustForce = 5;
	// s.debug = true;
	s.bearing = -90;
	s.maxVel = 3;
	s.maxRotSpeed = 2.5;
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

function spawnLaser() {
	let l = new lasers.Sprite();
	l.x = ship.x;
	l.y = ship.y;
	l.direction = ship.bearing;
	l.rotation = ship.rotation;
	l.speed = l.moveSpeed;
}

function updateLasers() {
	for (let laser of lasers) {
		wrapObject(laser);
	}
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

	if (kb.presses('space')) {
		ship.fire();
	}

	ship.bearing = ship.rotation - 90;

	ship.velocity.limit(ship.maxVel);

	if (ship.rotationSpeed > ship.maxRotSpeed) {
		ship.rotationSpeed = ship.maxRotSpeed;
	}
	if (ship.rotationSpeed < -ship.maxRotSpeed) {
		ship.rotationSpeed = -ship.maxRotSpeed;
	}

	wrapObject(ship);
}

function wrapObject(object) {
	if (object.x < 0) {
		object.x = width;
	}

	if (object.x > width) {
		object.x = 0;
	}

	if (object.y < 0) {
		object.y = height;
	}

	if (object.y > height) {
		object.y = 0;
	}
}
