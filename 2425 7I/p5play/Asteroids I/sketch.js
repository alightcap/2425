let starImgs = [];
let numStars = 75;

let planetImg;
let backgroundImg;

let spaceShip;
let spaceShipImg;

let asteroids;
let asteroidBigImg;
let asteroidMedImg;
let asteroidSmImg;

let lasers;
let laserImg;

let waveNum;
let isGameActive;

function preload() {
	starImgs.push(loadImage('assets/star1.png'));
	starImgs.push(loadImage('assets/star2.png'));
	starImgs.push(loadImage('assets/star3.png'));

	planetImg = loadImage('assets/planet01.png');

	spaceShipImg = loadImage('assets/playerShip1_green.png');

	asteroidBigImg = loadImage('assets/meteorBrown_big1.png');
	asteroidMedImg = loadImage('assets/meteorBrown_med1.png');
	asteroidSmImg = loadImage('assets/meteorBrown_small1.png');

	laserImg = loadImage('assets/laserGreen10.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	backgroundImg = createBackground();
	spaceShip = setupSpaceShip();
	asteroids = setupAsteroids();
	lasers = setupLasers();

	waveNum = 1;
	isGameActive = true;

	// spawnAsteroid(3, 100, 100, 90);

	spaceShip.overlaps(asteroids, damageSpaceship);
	spaceShip.overlaps(lasers);
	// maybe this can happen in their setup functions?
	lasers.overlaps(lasers);
	asteroids.overlaps(asteroids);
	lasers.overlaps(asteroids, damageAsteroid);
}

function draw() {
	background(backgroundImg);
	asteroidSpawner();
}

function asteroidSpawner() {
	if (isGameActive) {
		if (asteroids.size() <= 0) {
			waveNum += 1;
			for (let i = 0; i < waveNum; i++) {
				let x = random(width);
				let y = random(height);
				let dir = random(360);
				spawnAsteroid(3, x, y, dir);
			}
		}
	}
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

function setupSpaceShip() {
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

		wrap(s);
	}

	s.shoot = () => {
		spawnLaser(s.x, s.y, s.rotation);
	}

	return s;
}

function damageAsteroid(laser, asteroid) {
	laser.remove();
	asteroid.damage(/*could be a param here*/);
}

function damageSpaceship(ship, asteroid) {
	ship.remove();
}

function setupAsteroids() {
	let a = new Group();
	a.images = [asteroidSmImg, asteroidMedImg, asteroidBigImg];
	a.diameter = 30;
	// a.debug = true;

	return a;
}

function setupLasers() {
	let l = new Group();
	l.img = laserImg;
	l.diameter = 8;
	l.img.offset.y = 10;
	l.life = 120;

	// l.debug = true;

	return l;
}

function spawnAsteroid(size, x, y, direction) {
	let a = new asteroids.Sprite();
	// let x = random(width);
	// let y = random(height);

	// while (dist(x, y, spaceShip.x, spaceShip.y) < 150) {
	// 	x = random(width);
	// 	y = random(height);
	// }

	a.x = x;
	a.y = y;
	a.bearing = direction;
	a.applyForce(100);
	a.applyTorque(random(-5, 5));

	a.health = size;
	// should adjust the size of the collider here.
	a.img = a.images[size - 1];

	a.update = () => {
		wrap(a);
	}

	a.damage = () => {
		a.health -= 1;

		if (a.health > 0) {
			spawnAsteroid(a.health, a.x, a.y, a.bearing - 90);
			spawnAsteroid(a.health, a.x, a.y, a.bearing + 90);
		}
		a.remove();
	}
}

function spawnLaser(x, y, rotation) {
	let l = new lasers.Sprite();
	l.x = x;
	l.y = y;
	l.rotation = rotation;
	l.bearing = l.rotation - 90;

	l.applyForce(50);

	l.update = () => {
		wrap(l);
	}
}

function wrap(obj) {
	if (obj.x > width) {
		obj.x -= width;
	}
	if (obj.x < 0) {
		obj.x += width;
	}
	if (obj.y > height) {
		obj.y -= height;
	}
	if (obj.y < 0) {
		obj.y += height;
	}
}