let backgroundImg;
let ball;
let paddle;
let walls;

function preload() {
	backgroundImg = loadImage('assets/Space Background.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	paddle = createPaddle();
	walls = createWalls();
	ball = createBall();
	countdown();
}

function draw() {
	background(backgroundImg);

	updatePaddle();
}

async function countdown() {
	await delay(2000);
	ball.speed = 5;
}

function createBall() {
	let b = new Sprite();

	b.color = "lightgreen"
	b.x = width / 2;
	b.y = height / 2;
	b.diameter = 20;
	b.bounciness = 1;
	b.friction = 0;
	b.direction = 80;
	b.speed = 0;

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

function updatePaddle() {
	paddle.moveTowards(mouse.x, height - 50, 0.1);
}