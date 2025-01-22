let ball;
let topWall, bottomWall;
let leftPaddle, rightPaddle;
let leftGoal, rightGoal;
let leftScore, rightScore;
let isGameActive = true;

function setup() {
	new Canvas(800, 600);
	displayMode('centered');
	textSize(40);

	leftScore = 0;
	rightScore = 0;


	createPaddles();
	createEnvironment();
	createGoals();
	createBall();

	startRound();
	updateBall();
}

function draw() {
	background('skyblue');
	updateLeftPaddle();
	updateRightPaddle();

	text(leftScore, 60, 75);
	text(rightScore, width - 80, 74);
}

function createBall() {
	ball = new Sprite();
	ball.x = width / 2;
	ball.y = height / 2;
	ball.diameter = 30;
	ball.color = 'black';
	ball.moveSpeed = 5;
	ball.bounciness = 1;
	ball.friction = 0;
}

function createEnvironment() {
	topWall = new Sprite();
	topWall.x = width / 2;
	topWall.y = 0;
	topWall.width = width;
	topWall.height = 40;
	topWall.collider = 'static';
	topWall.color = 'white';
	topWall.friction = 0;
	topWall.bounciness = 1;

	bottomWall = new Sprite();
	bottomWall.x = width / 2;
	bottomWall.y = height;
	bottomWall.width = width;
	bottomWall.height = 40;
	bottomWall.collider = 'static';
	bottomWall.color = 'white';
	bottomWall.friction = 0;
	bottomWall.bounciness = 1;
}

function createGoals() {
	leftGoal = new Sprite();
	leftGoal.x = 0;
	leftGoal.y = height / 2;
	leftGoal.collider = 'static';
	leftGoal.width = 40;
	leftGoal.height = height;
	leftGoal.color = 'red';

	rightGoal = new Sprite();
	rightGoal.x = width;
	rightGoal.y = height / 2;
	rightGoal.collider = 'static';
	rightGoal.width = 40;
	rightGoal.height = height;
	rightGoal.color = 'green';
}

function createPaddles() {
	leftPaddle = new Sprite();
	leftPaddle.startX = 70;
	leftPaddle.startY = height / 2;
	leftPaddle.x = leftPaddle.startX;
	leftPaddle.y = leftPaddle.startY;
	leftPaddle.color = 'red';
	leftPaddle.width = 20;
	leftPaddle.height = 120;
	leftPaddle.collider = 'kinematic'
	leftPaddle.bounciness = 1;
	leftPaddle.friction = 0;
	leftPaddle.moveSpeed = 5;

	rightPaddle = new Sprite();
	rightPaddle.startX = width - 70;
	rightPaddle.startY = height / 2;
	rightPaddle.x = rightPaddle.startX;
	rightPaddle.y = rightPaddle.startY;
	rightPaddle.color = 'green';
	rightPaddle.width = 20;
	rightPaddle.height = 120;
	rightPaddle.collider = 'kinematic';
	rightPaddle.bounciness = 1;
	rightPaddle.friction = 0;
	rightPaddle.moveSpeed = 5;
}

function generateRandomVelocity() {
	let x = random();
	while (x < 0.5) {
		x = random();
	}
	let y = sqrt(1 - (x * x));
	if (random() < 0.5) {
		x *= -1;
	}
	if (random() < 0.5) {
		y *= -1;
	}

	return new p5.Vector(x, y);
}

async function startRound() {
	ball.x = width / 2;
	ball.y = height / 2;
	ball.vel = new p5.Vector();

	await (delay(3000));

	ball.vel = generateRandomVelocity().mult(ball.moveSpeed);
}

function updateLeftPaddle() {
	leftPaddle.vel.y = 0;
	let direction = 0;
	if (kb.pressing('w')) {
		direction = -1;
	}
	if (kb.pressing('s')) {
		direction = 1;
	}

	leftPaddle.vel.y = direction * leftPaddle.moveSpeed;
}

function updateRightPaddle() {
	rightPaddle.vel.y = 0;
	let direction = 0;

	if (kb.pressing('arrowUp')) {
		direction = -1;
	}

	if (kb.pressing('arrowDown')) {
		direction = 1;
	}

	rightPaddle.vel.y = direction * rightPaddle.moveSpeed;
}

async function updateBall() {
	while (isGameActive) {
		await (delay(3000));
		ball.vel.mult(1.1);
	}
}