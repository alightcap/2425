let player;
let playerIdleAnimation;
let playerRunAnimation;
let gravityStrength;
let ground;

function preload() {
	playerIdleAnimation = loadAni(
		'assets/idle.png',
		{ frameSize: [24, 24], frames: 3 }
	)
	playerIdleAnimation.frameDelay = 6;

	playerRunAnimation = loadAni(
		'assets/move.png',
		{ frameSize: [24, 24], frames: 6 }
	)
	playerRunAnimation.frameDelay = 6;
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

	p.moveSpeed = 5;
	p.xScale = 5;
	p.jumpForce = 50;

	p.width = 9;
	p.height = 9;
	p.bounciness = 0;
	p.bearing = -90;

	p.scale = p.xScale;
	p.addAni('run', playerRunAnimation);
	p.addAni('idle', playerIdleAnimation);
	// p.debug = true;

	let g = new Sprite();
	g.radius = 4;
	g.collider = 'none';
	g.x = p.x;
	g.y = p.y + p.halfHeight;
	g.visible = false;

	p.groundSensor = g;
	let j = new GlueJoint(p, p.groundSensor);
	j.visible = false;

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
