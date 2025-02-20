let starImgs = [];
let stars = [];
let numStars = 75;

let planetImg;

let spaceShip;
let spaceShipImg;

let asteroids;
let asteroidImg;

let lasers;
let laserImg;

function preload() {
	starImgs.push(loadImage('assets/star1.png'));
	starImgs.push(loadImage('assets/star2.png'));
	starImgs.push(loadImage('assets/star3.png'));
	planetImg = loadImage('assets/planet07.png');
	spaceShipImg = loadImage('assets/playerShip1_green.png');
	asteroidImg = loadImage('assets/meteorBrown_big1.png');
	laserImg = loadImage('assets/laserGreen10.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');
	imageMode(CENTER);

	createStars();
	spaceShip = createSpaceShip();
	asteroids = setupAsteroids();
	lasers = setupLasers();

	asteroids.overlaps(spaceShip, damageShip);
	lasers.overlaps(spaceShip);
	lasers.overlaps(asteroids, damageAsteroid);

	spawnAsteroid();
}

function draw() {
	background('#222222');

	drawStars();
	image(planetImg, width / 2, height / 2);
}

function damageShip(other, spaceShip) {
	spaceShip.remove();
}

function damageAsteroid(laser, asteroid) {
	asteroid.remove();
	laser.remove();
}

function createSpaceShip() {
	let s = new Sprite();
	s.img = spaceShipImg;
	s.rotation = 90;
	s.rotationDrag = 2;

	s.moveSpeed = 5;
	s.rotSpeed = 2;

	s.update = () => {
		if (kb.presses('space')) {
			s.shoot();
		}

		if (kb.pressing('arrowUp')) {
			s.applyForce(s.moveSpeed);
		}

		s.vel.limit(s.moveSpeed);

		let rotDirection = 0;
		if (kb.pressing('arrowLeft')) {
			rotDirection = -1;
		}
		if (kb.pressing('arrowRight')) {
			rotDirection = 1;
		}

		s.applyTorque(s.rotSpeed * rotDirection);
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

function createStars() {
	for (let i = 0; i < numStars; i++) {
		let star = [];
		let x = random(width);
		let y = random(height);
		let img = random(starImgs);

		star.push(x);
		star.push(y);
		star.push(img);
		stars.push(star);
	}
}

function drawStars() {
	for (let star of stars) {
		image(star[2], star[0], star[1]);  // these are not very descriptive, but i'm moving fast
	}
}

function setupAsteroids() {
	let a = new Group();
	a.img = asteroidImg;
	a.diameter = 30;

	// a.debug = true;

	return a;
}

function setupLasers() {
	let l = new Group();
	l.img = laserImg;
	l.diameter = 8;
	l.image.offset.y = 10;
	l.life = 60;

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

	a.moveSpeed = 100;
	a.bearing = random(360);
	a.applyForce(a.moveSpeed);
	a.applyTorque(random(-5, 5));

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
	l.bearing = rotation - 90;

	l.moveSpeed = 30;
	l.applyForce(l.moveSpeed);
}