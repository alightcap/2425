let player;
let playerIdleAnim;
let playerRunAnim;
let gravityStrength;
let ground;

function preload() {
	playerIdleAnim = loadAni(
		'assets/idle.png',
		{ frameSize: [24, 24], frames: 3 }
	);

	playerIdleAnim.frameDelay = 6;

	playerRunAnim = loadAni(
		'assets/move.png',
		{ frameSize: [24, 24], frames: 6 }
	);

	playerRunAnim.frameDelay = 6;
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');
	gravityStrength = 10;
	world.gravity.y = gravityStrength;

	player = createPlayer();
	ground = createGround();
}

function draw() {
	background('skyblue');

	playerController();
}

function createGround() {
	let g = new Sprite();

	g.x = width / 2;
	g.y = height;
	g.width = width;
	g.height = 40;
	g.collider = 'static';
	g.color = 'green';
	g.bounciness = 0;

	return g;
}

function createPlayer() {
	let p = new Sprite();

	p.width = 9;
	p.height = 9;

	p.addAni('idle', playerIdleAnim);
	p.addAni('run', playerRunAnim);
	p.xScale = 5;
	p.scale = p.xScale;
	p.bearing = -90;
	p.bounciness = 0;
	// p.debug = true;

	p.moveSpeed = 5;
	p.jumpForce = 50;

	let groundSensor = new Sprite();
	groundSensor.debug = true;
	groundSensor.radius = 4;
	groundSensor.collider = 'none';
	groundSensor.x = p.x;
	groundSensor.y = p.y + p.height;
	p.groundSensor = groundSensor;

	return p;
}

function playerController() {
	let inputX = 0;

	if (kb.pressing('left')) {
		inputX = -1;
	}

	if (kb.pressing('right')) {
		inputX = 1;
	}

	if (kb.presses('up')) {
		player.applyForce(player.jumpForce);
	}

	player.vel.x = inputX * player.moveSpeed;

	playerVisuals();
}

function playerVisuals() {
	if (player.vel.x > 0) {
		player.scale.x = player.xScale;
	}

	if (player.vel.x < 0) {
		player.scale.x = -player.xScale;
	}

	if (player.isMoving) {
		player.changeAni('run');
	} else {
		player.changeAni('idle');
	}
}