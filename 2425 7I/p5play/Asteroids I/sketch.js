let starImgs = [];
let numStars = 75;

let planetImg;
let backgroundImg;

let spaceShip;
let spaceShipImg;

let asteroids;
let asteroidBigImg;

let lasers;
let laserImg;

function preload() {
	starImgs.push(loadImage('assets/star1.png'));
	starImgs.push(loadImage('assets/star2.png'));
	starImgs.push(loadImage('assets/star3.png'));

	planetImg = loadImage('assets/planet01.png');

	spaceShipImg = loadImage('assets/playerShip1_green.png');

	asteroidBigImg = loadImage('assets/meteorBrown_big1.png');

	laserImg = loadImage('assets/laserGreen10.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	backgroundImg = createBackground();
	spaceShip = createSpaceShip();
	asteroids = setupAsteroids();
	lasers = setupLasers();

	// spawnAsteroid();

	spaceShip.overlaps(asteroids, damageSpaceship);
	spaceShip.overlaps(lasers);
}

function draw() {
	background(backgroundImg);
}

function createBackground() {
	let b = createImage(width, height);
	for (let x = 0; x < width; x++) {
		for (let y = 0; y < height; y++) {
			b.set(x, y, color('#222222'));
		}
	}
	b.updatePixels();

	for (let i = 0; i < numStars; i++) {
		b.set(random(width), random(height), random(starImgs));
	}

	b.set(width / 2, height / 2, planetImg);

	return b;
}

function createSpaceShip() {
	let s = new Sprite();
	s.img = spaceShipImg;
	s.diameter = 20;
	s.rotation = 90;
	s.rotationDrag = 2;

	s.thrust = 6;
	s.maxVel = 3;
	s.rotSpeed = 0.05;

	// s.debug = true;

	s.update = () => {
		if (kb.presses('space')) {
			s.shoot();
		}

		if (kb.pressing('arrowUp')) {
			s.applyForce(s.thrust);
		}

		s.vel.limit(s.maxVel);

		let rotDir = 0;
		if (kb.pressing('arrowLeft')) {
			rotDir = -1;
		}

		if (kb.pressing('arrowRight')) {
			rotDir = 1;
		}
		s.applyTorque(s.rotSpeed * rotDir);

		s.bearing = s.rotation - 90;

		if (s.x > width) {
			s.x -= width;
		}
		if (s.x < 0) {
			s.x += width;
		}
		if (s.y > height) {
			s.y -= height;
		}
		if (s.y < 0) {
			s.y += height;
		}
	}

	s.shoot = () => {
		spawnLaser(s.x, s.y, s.rotation);
	}

	return s;
}

function damageSpaceship(ship, asteroid) {
	ship.remove();
	asteroid.remove();
}

function setupAsteroids() {
	let a = new Group();
	a.img = asteroidBigImg;
	a.diameter = 30;
	// a.debug = true;

	return a;
}

function setupLasers() {
	let l = new Group();
	l.img = laserImg;
	l.diameter = 8;
	l.img.offset.y = 10;

	// l.debug = true;

	return l;
}

function spawnAsteroid() {
	let a = new asteroids.Sprite();
	let x = random(width);
	let y = random(height);

	while (dist(x, y, spaceShip.x, spaceShip.y) < 150) {
		x = random(width);
		y = random(height);
	}

	a.x = x;
	a.y = y;
	a.bearing = random(360);
	a.applyForce(100);

	a.update = () => {
		if (a.x > width) {
			a.x -= width;
		}
		if (a.x < 0) {
			a.x += width;
		}
		if (a.y > height) {
			a.y -= height;
		}
		if (a.y < 0) {
			a.y += height;
		}
	}
}

function spawnLaser(x, y, rotation) {
	let l = new lasers.Sprite();
	l.x = x;
	l.y = y;
	l.rotation = rotation;
	l.bearing = l.rotation - 90;
	l.life = 60;

	l.applyForce(50);

	l.update = () => {
		if (l.x > width) {
			l.x -= width;
		}
		if (l.x < 0) {
			l.x += width;
		}
		if (l.y > height) {
			l.y -= height;
		}
		if (l.y < 0) {
			l.y += height;
		}
	}
}