let starImgs = [];
let stars = [];
let numStars = 50;

let planetImg;

let spaceShip;
let spaceShipImg;

let asteroids;
let asteroidImg;

function preload() {
	starImgs.push(loadImage('assets/star1.png'));
	starImgs.push(loadImage('assets/star2.png'));
	starImgs.push(loadImage('assets/star3.png'));
	planetImg = loadImage('assets/planet07.png');
	spaceShipImg = loadImage('assets/playerShip1_green.png');
	asteroidImg = loadImage('assets/meteorBrown_big1.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');
	imageMode(CENTER);

	createStars();
	spaceShip = createSpaceShip();
	asteroids = setupAsteroids();

	new asteroids.Sprite();
}

function draw() {
	background('#222222');

	drawStars();
	image(planetImg, width / 2, height / 2);
}

function createSpaceShip() {
	let s = new Sprite();
	s.img = spaceShipImg;
	s.rotation = 90;
	s.rotationDrag = 2;

	s.moveSpeed = 5;
	s.rotSpeed = 2;

	s.update = () => {
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

	return a;
}