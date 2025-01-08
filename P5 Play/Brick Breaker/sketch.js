let backgroundImg;
let ball;
let bricks;
let paddle;
let walls;
let score = 0;

function preload() {
	backgroundImg = loadImage('assets/Space Background.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	textAlign(CENTER);

	paddle = createPaddle();
	walls = createWalls();
	ball = createBall();
	bricks = createBricks();

	ball.collides(bricks, hitBrick);

	countdown();
}

function draw() {
	background(backgroundImg);

	fill("white");
	textSize(20);
	text("Score: " + score, 75, 50);

	updatePaddle();
	if (ball.y > height) {
		endGame();
	}
	if (bricks.length < 1) {
		endGame();
	}
}

async function countdown() {
	await delay(2000);
	ball.speed = 5;
}

function createBall() {
	let b = new Sprite();

	b.color = "turquoise";
	b.x = width / 2;
	b.y = height / 2;
	b.diameter = 20;
	b.bounciness = 1;
	b.friction = 0;
	b.direction = 80;
	b.speed = 0;

	return b;
}

function createBricks() {
	let b = new Group();

	b.color = "skyblue";
	b.collider = "static";
	b.width = 40;
	b.height = 20;
	// b.friction = 0;
	// b.bounciness = 1;
	b.tile = "-";

	b.pointValue = 100;

	let tiles = new Tiles(
		[
			"---------------",
			"-----.....-----",
			"---.........---",
			"-.............-",
			"---.........---",
			"-----.....-----",
			"---------------",
		],
		90, 100,
		b.width + 4, b.height + 4
	)

	return b;
}

function createPaddle() {
	let p = new Sprite();

	p.x = width / 2;
	p.y = height - 50;
	p.width = 100;
	p.height = 20;
	p.color = "green";
	p.rotationLock = true;
	p.collider = "kinematic";

	return p;
}

function createWalls() {
	let w = new Group();

	w.color = "green";
	w.collider = "static";
	new w.Sprite(0, height / 2, 20, height);
	new w.Sprite(width, height / 2, 20, height)
	new w.Sprite(width / 2, 0, width, 20);

	return w;
}

function endGame() {
	if (ball.y > height) {
		textSize(50);
		fill('red');
		text("Game Over", width / 2, height / 2);
	}

	if (bricks.length < 1) {
		textSize(50);
		fill("green");
		text("You Win!", width / 2, height / 2);
	}

	noLoop();
}

function hitBrick(ball, brick) {
	score += brick.pointValue;
	brick.remove();
}

function updatePaddle() {
	paddle.moveTowards(mouse.x, height - 50, 0.1);
}