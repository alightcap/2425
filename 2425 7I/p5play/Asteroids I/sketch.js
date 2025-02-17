let starImgs = [];
let stars = [];
let numStars = 75;

let planetImg;
// let backgroundImg;

let spaceShip;
let spaceShipImg;

let asteroids;
let asteroidBigImg;

function preload() {
	starImgs.push(loadImage('assets/star1.png'));
	starImgs.push(loadImage('assets/star2.png'));
	starImgs.push(loadImage('assets/star3.png'));

	planetImg = loadImage('assets/planet01.png');

	spaceShipImg = loadImage('assets/playerShip1_green.png');

	asteroidBigImg = loadImage('assets/meteorBrown_big1.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	createStars();
	spaceShip = createSpaceShip();
	asteroids = createAsteroids();
	// backgroundImg = createBackground();
	new asteroids.Sprite();
}

function draw() {
	background('#222222');

	drawStars();
	image(planetImg, width / 2, height / 2);
}

function createAsteroids() {
	let a = new Group();
	a.img = asteroidBigImg;

	return a;
}

function createSpaceShip() {
	let s = new Sprite();
	s.img = spaceShipImg;
	s.diameter = 20;
	s.rotation = 90;

	s.thrust = 10;
	s.maxVel = 3;
	s.rotSpeed = 0.1;
	s.maxRotSpeed = 1;

	// s.debug = true;
	s.update = () => {
		if (kb.pressing('arrowUp')) {
			s.applyForce(s.thrust);
		}

		if (kb.pressing('arrowLeft')) {
			s.applyTorque(-s.rotSpeed);
		}

		if (kb.pressing('arrowRight')) {
			s.applyTorque(s.rotSpeed);
		}

		s.vel.limit(s.maxVel);

		if (s.rotationSpeed < -s.maxRotSpeed) {
			s.rotationSpeed = -s.maxRotSpeed;
		}
		if (s.rotationSpeed > s.maxRotSpeed) {
			s.rotationSpeed = s.maxRotSpeed;
		}

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
	return s;
}

function createStars() {
	for (let i = 0; i < numStars; i++) {
		let star = [];

		let x = random(width);
		let y = random(height);
		let img = random(starImgs);

		star.push(img);
		star.push(x);
		star.push(y);

		stars.push(star);
	}
}

function drawStars() {
	for (let star of stars) {
		image(star[0], star[1], star[2]);
	}
}

// function createBackground() {
// 	let b = createImage(width, height);
//  for (let x = 0; x < width; x++){
//    for (let y = 0; y < height; y++) {
//      
//    }
//  }
// 	return b;
// }
