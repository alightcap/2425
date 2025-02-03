let player;
let playerIdleAnimation;
let playerRunAnimation;
let gravityStrength;
let ground;
let basketball;
let basketballImg;
let goal;
let score = 0;

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

	basketballImg = loadImage('assets/basketball.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');
	textSize(40);

	gravityStrength = 10;
	world.gravity.y = gravityStrength;

	player = createPlayer();
	ground = createGround();
	basketball = createBasketball();
	createWalls();
	goal = createGoal();

	basketball.overlaps(player);
	basketball.overlaps(goal);
	basketball.overlaps(goal.frontRim);
}

function draw() {
	background('skyblue');

	playerController();

	if (basketball.overlapped(goal.frontRim)) {
		if (basketball.vel.y > 0) {
			score++;
			moveGoal();
		}
	}

	text('Score: ' + score, 10, 40);
}

function createBasketball() {
	let b = new Sprite();
	b.img = basketballImg;

	b.x = width / 2 + 50;

	b.scale = 2;
	b.radius = 10;
	b.bounciness = 0.67;
	b.mass = 1;

	return b;
}

function createGoal() {
	let b = new Sprite();

	b.collider = 'kinematic';
	b.color = 'white';
	b.x = width / 2 + 50;
	b.y = height / 2;
	b.width = 150;
	b.height = 100;
	b.layer = -1;

	let leftRim = new Sprite();
	leftRim.color = 'orange';
	leftRim.diameter = 5;
	leftRim.x = b.x - 20;
	leftRim.y = b.y + b.halfHeight / 2;
	new GlueJoint(b, leftRim);

	let rightRim = new Sprite();
	rightRim.color = 'orange';
	rightRim.diameter = 5;
	rightRim.x = b.x + 20;
	rightRim.y = b.y + b.halfHeight / 2;
	new GlueJoint(b, rightRim);

	let frontRim = new Sprite();
	frontRim.color = 'orange';
	frontRim.width = 40;
	frontRim.height = 5;
	frontRim.x = b.x;
	frontRim.y = b.y + b.halfHeight / 2;
	new GlueJoint(b, frontRim);

	b.frontRim = frontRim;

	return b;
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

	p.isGrounded = false;
	p.isShooting = false;
	p.jumpForce = 5000;
	p.moveSpeed = 5;
	p.shotForce = 500;
	p.xScale = 5;

	p.bearing = -90;
	p.bounciness = 0;
	p.height = 9;
	p.mass = 10;
	p.scale = p.xScale;
	p.width = 9;

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

function createWalls() {
	let leftWall = new Sprite();
	leftWall.x = 0;
	leftWall.y = height / 2;
	leftWall.w = 20;
	leftWall.h = height;
	leftWall.collider = 'static';
	leftWall.visible = false;

	let rightWall = new Sprite();
	rightWall.x = width;
	rightWall.y = height / 2;
	rightWall.w = 20;
	rightWall.h = height;
	rightWall.collider = 'static';
	rightWall.visible = false;
}

function moveGoal() {
	let x = random(100, width - 100);
	let y = random(height / 2, 3 * height / 4);
	goal.moveTo(x, y, 5);
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
		if (player.isGrounded) {
			player.isGrounded = false;
			player.applyForce(player.jumpForce);
		}
	}

	if (kb.presses('space')) {
		if (player.joints[1]) {
			player.isShooting = true;
			player.joints[1].remove();
			basketball.bearing = -60;
			let torque = -1;
			if (player.scale.x < 0) {
				basketball.bearing = -120;
				torque = 1;
			}
			basketball.vel.mult(0);
			basketball.applyTorque(torque);
			basketball.applyForce(player.shotForce);
		}
	}

	if (player.overlapped(basketball)) {
		player.isShooting = false;
	}

	if (player.groundSensor.overlaps(ground)) {
		player.isGrounded = true;
	}

	if (player.overlaps(basketball) && !player.isShooting) {
		basketball.x = player.x;
		basketball.y = player.y;
		new GlueJoint(player, basketball);
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
