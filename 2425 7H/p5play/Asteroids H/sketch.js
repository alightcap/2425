let starImgs = [];
let stars = [];
let numStars = 50;

let planetImg;

let spaceShip;
let spaceShipImg;

function preload() {
	starImgs.push(loadImage('assets/star1.png'));
	starImgs.push(loadImage('assets/star2.png'));
	starImgs.push(loadImage('assets/star3.png'));
	planetImg = loadImage('assets/planet07.png');
	spaceShipImg = loadImage('assets/playerShip1_green.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');
	imageMode(CENTER);

	createStars();
	spaceShip = createSpaceShip();
}

function draw() {
	background('#222222');

	drawStars();
	image(planetImg, width / 2, height / 2);
}

function createSpaceShip() {
	let s = new Sprite();
	s.img = spaceShipImg;

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