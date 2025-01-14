let asteroids;
let bigAsteroidImg;
let explosions;
let explosionSheet;
let medAsteroidImg;
let smAsteroidImg;
let backgroundImg;
let lasers;
let laserImg;
let planet;
let planetAnimation;
let ship;
let shipImg;
let waveNumber;

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
	bigAsteroidImg = loadImage('assets/meteorBrown_big1.png');
	medAsteroidImg = loadImage('assets/meteorBrown_med1.png');
	smAsteroidImg = loadImage('assets/meteorBrown_tiny1.png');

	explosionSheet = loadImage('assets/explosion sheet.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	// planet = createPlanet();
	ship = createShip();
	lasers = createLasers();
	asteroids = createAsteroids();
	explosions = createExplosions();

	lasers.overlaps(ship);
	lasers.overlaps(lasers);
	lasers.collides(asteroids, damageObject);

	asteroids.overlaps(asteroids);
	asteroids.collides(ship, damageShip);

	ship.fire = spawnLaser;
	// laser = new lasers.Sprite();
	// asteroid = new asteroids.Sprite();
	// spawnAsteroid();

	waveNumber = 0;

	let e = new explosions.Sprite();
	e.x = 100;
	e.y = 100;
	e.changeAni('asteroid');
}

function draw() {
	background(backgroundImg);

	updateShip();
	updateLasers();
	updateAsteroids();

	if (asteroids.length == 0) {
		spawnWave();
	}
}

function damageShip(asteroid, ship) {
	ship.remove();
}

function createAsteroids() {
	let a = new Group();

	a.hits = 3;

	a.images = [0, smAsteroidImg, medAsteroidImg, bigAsteroidImg];
	a.radii = [0, 5, 20, 40];

	a.image = a.images[a.hits];
	// a.debug = true;
	a.scale = 2;
	a.radius = a.radii[a.hits];
	a.direction = random(360);
	a.rotationSpeed = random(1, 5);
	a.speed = random(1, 3);

	return a;
}

function createExplosions() {
	let e = new Group();

	e.width = 64;
	e.height = 64;
	e.collider = 'none';
	e.spriteSheet = explosionSheet;
	e.addAnis(
		{
			asteroid: { row: 9, frames: 8 },
			ship: { row: 10, frames: 8 }
		}
	)
	e.anis['asteroid'].noLoop();
	e.anis['ship'].noLoop();
	e.scale = 2;

	return e;
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

function damageObject(laser, asteroid) {
	laser.remove();
	asteroid.hits -= 1;
	splitAsteroid(asteroid);
}

function spawnAsteroid() {
	let minDist = 100;
	let x = random(width);
	let y = random(height);
	while (dist(x, y, ship.x, ship.y) < minDist) {
		x = random(width);
		y = random(height);
	}

	new asteroids.Sprite(x, y);
}

function spawnLaser() {
	let l = new lasers.Sprite();

	l.x = ship.x;
	l.y = ship.y;
	l.direction = ship.bearing;
	l.rotation = ship.rotation;
	l.speed = l.moveSpeed;
}

function spawnWave() {
	waveNumber += 1;
	for (let i = 0; i < waveNumber; i++) {
		spawnAsteroid();
	}
}

function splitAsteroid(asteroid) {
	if (asteroid.hits > 0) {
		let a1 = new asteroids.Sprite(asteroid.x, asteroid.y);
		a1.direction = asteroid.direction + 90;
		a1.hits = asteroid.hits;

		let a2 = new asteroids.Sprite(asteroid.x, asteroid.y);
		a2.direction = asteroid.direction - 90;
		a2.hits = asteroid.hits;

		a1.image = a1.images[a1.hits];
		a1.radius = a1.radii[a1.hits];

		a2.image = a2.images[a2.hits];
		a2.radius = a2.radii[a2.hits];
	}

	asteroid.remove();
}

function updateAsteroids() {
	for (let asteroid of asteroids) {
		wrapObject(asteroid);
	}
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
