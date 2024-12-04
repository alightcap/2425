let dots = [];
let numDots = 15;
let colors = ['#ccdbdc', '#80ced7', '#63c7b2', '#8e6c88'];

function setup() {
	new Canvas(800, 600);

	for (let i = 0; i < numDots; i++) {
		dots.push(createDot());
	}
	// dot = createDot();
}

function draw() {
	background('#263d42');

	for (let dot of dots) {
		updateDot(dot);
	}
}

function createDot() {
	let	dot = new Sprite();
	dot.color = random(colors);
	dot.radius = 25;
	dot.x = width / 2;
	dot.y = height / 2;
	dot.direction = random(360);
	dot.speed = random(5, 10);
	dot.overlaps(allSprites);
	return dot;
}

function updateDot(dot) {
	if (dot.x < 0 + dot.radius) {
		dot.velocity.x *= -1;
	}

	if (dot.x > width - dot.radius) {
		dot.velocity.x *= -1;
	}

	if (dot.y < 0 + dot.radius) {
		dot.velocity.y *= -1;
	}

	if (dot.y > height - dot.radius) {
		dot.velocity.y *= -1;
	}
}
