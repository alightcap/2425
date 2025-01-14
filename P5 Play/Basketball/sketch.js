let player;
let playerIdleAni;
let playerRunAni;
let gravityStrength = 10;
let ground;
let basketball;
let basketballImg;
let goal;
let score = 0;
let scoreText;


function preload() {
	playerIdleAni = loadAnimation(
		"assets/idle.png",
		{ frameSize: [24, 24], frames: 3 }
	);
	playerIdleAni.frameDelay = 6;

	playerRunAni = loadAnimation(
		"assets/move.png",
		{ frameSize: [24, 24], frames: 6 }
	);
	playerRunAni.frameDelay = 6;

	basketballImg = "assets/basketball.png";
}

function setup() {
	new Canvas(800, 600);
	world.gravity.y = gravityStrength;

	player = createPlayer();
	ground = createGround();
	basketball = createBasketball();
	goal = createGoal();

	createWalls();
	// createScoreUI();

	basketball.overlaps(player);
	basketball.overlaps(goal);
	basketball.overlaps(goal.frontRim);
	basketball.overlaps(goal.goalSensor);

	textSize(40);
}

function draw() {
	background('skyblue');

	playerController();
	if (basketball.overlapped(goal.goalSensor)) {
		if (basketball.vel.y > 0) {
			score += 1;
			moveGoal();
		}
	}

	text('Score: ' + score, 10, 40);
}

function createBasketball() {
	let basketball = new Sprite();
	// basketball.debug = true;
	basketball.img = basketballImg;
	basketball.radius = 10;
	basketball.bounciness = 0.67;
	basketball.x = width / 2 + 50;
	basketball.mass = 0.01;
	basketball.layer = 2;

	return basketball;
}

function createGoal() {
	let backboard = new Sprite();

	backboard.collider = 'kinematic';
	backboard.color = 'white';
	backboard.x = width / 2;
	backboard.y = height / 2;
	backboard.width = 150;
	backboard.height = 100;
	backboard.layer = 1;

	let leftRim = new Sprite();
	leftRim.color = 'orange';
	leftRim.width = 5;
	leftRim.height = 5
	leftRim.x = backboard.x - 20;
	leftRim.y = backboard.y + backboard.halfHeight / 2;
	leftRim.layer = 2;

	let j1 = new GlueJoint(backboard, leftRim);
	j1.visible = false;

	let rightRim = new Sprite();
	rightRim.color = 'orange';
	rightRim.width = 5;
	rightRim.height = 5;
	rightRim.x = backboard.x + 20;
	rightRim.y = backboard.y + backboard.halfHeight / 2;
	rightRim.layer = 2;

	let j2 = new GlueJoint(backboard, rightRim);
	j2.visible = false;

	let frontRim = new Sprite();
	frontRim.color = 'orange';
	frontRim.width = 40;
	frontRim.height = 5;
	frontRim.x = backboard.x;
	frontRim.y = backboard.y + backboard.halfHeight / 2;
	frontRim.layer = 3;

	let j3 = new GlueJoint(backboard, frontRim);
	j3.visible = false;

	let goalSensor = new Sprite();
	goalSensor.w = 30;
	goalSensor.h = 1;
	goalSensor.x = backboard.x;
	goalSensor.y = backboard.y + backboard.halfHeight / 2;
	goalSensor.visible = false;

	let j4 = new GlueJoint(backboard, goalSensor);
	j4.visible = false;

	backboard.leftRim = leftRim;
	backboard.rightRim = rightRim;
	backboard.frontRim = frontRim;
	backboard.goalSensor = goalSensor;

	return backboard;
}

function createGround() {
	let ground = new Sprite();
	ground.x = width / 2;
	ground.y = height;
	ground.w = width;
	ground.h = 40;
	ground.collider = "static";
	ground.color = "green";
	ground.bounciness = 0;
	return ground;
}

function createPlayer() {
	let player = new Sprite();

	player.x = width / 2;
	player.y = height - 24;

	player.w = 16;
	player.h = 16;

	player.jumpForce = 100;
	player.shotForce = 5;
	player.moveSpeed = 5;
	player.isShooting = false;
	player.isGrounded = true;

	let groundSensor = new Sprite();
	groundSensor.r = 6;
	groundSensor.collider = 'none';
	groundSensor.x = player.x
	groundSensor.y = player.y + 1.5 * player.height;
	groundSensor.visible = false;
	player.groundSensor = groundSensor;

	let j = new GlueJoint(player, player.groundSensor);
	j.visible = false;

	player.addAni("idle", playerIdleAni);
	player.addAni("move", playerRunAni);
	player.changeAni("idle");

	player.bounciness = 0;
	player.friction = 0;
	player.rotationLock = true;
	player.scale = 3;
	// player.debug = true;


	return player;
}

function createWalls() {
	let leftWall = new Sprite();
	leftWall.x = 0;
	leftWall.y = height / 2;
	leftWall.width = 20;
	leftWall.height = height;
	leftWall.collider = 'static';
	leftWall.visible = false;

	let rightWall = new Sprite();
	rightWall.x = width;
	rightWall.y = height / 2;
	rightWall.width = 20;
	rightWall.height = height;
	rightWall.collider = 'static';
	rightWall.visible = false;
}

function moveGoal() {
	let x = random(100, width - 100);
	let y = random(300, 400);
	goal.moveTo(x, y, 5);
}

function playerController() {
	let inputVector = createVector(0, 0);

	if (kb.pressing("left")) {
		inputVector.x = -1;
	}

	if (kb.pressing("right")) {
		inputVector.x = 1;
	}

	if (kb.presses("up")) {
		if (player.isGrounded) {
			player.bearing = -90;
			player.applyForce(player.jumpForce);
			// player.vel.y = player.jumpForce;
		}
	}

	if (player.groundSensor.overlaps(ground)) {
		player.isGrounded = true;
	}

	if (player.groundSensor.overlapped(ground)) {
		player.isGrounded = false;
	}

	if (player.overlapping(basketball) && !player.isShooting) {
		basketball.x = player.x;
		basketball.y = player.y;
		new GlueJoint(player, basketball);
	}

	if (kb.presses('space')) {
		player.isShooting = true;
		if (player.joints[1]) {
			player.joints[1].remove();
			basketball.bearing = -60;
			let torque = -1;
			if (player.mirror.x) {
				basketball.bearing = -120;
				torque = 1;
			}

			basketball.applyTorque(torque);
			basketball.applyForce(player.shotForce);
		}
	}

	if (player.overlapped(basketball) && player.isShooting) {
		player.isShooting = false;
	}

	inputVector.normalize().mult(player.moveSpeed);
	player.vel.x = inputVector.x;

	playerVisuals();
}

function playerVisuals() {
	if (player.vel.x > 0) {
		player.mirror.x = false;
	}

	if (player.vel.x < 0) {
		player.mirror.x = true;
	}

	if (player.isMoving) {
		player.changeAni("move");
	}

	if (!player.isMoving) {
		player.changeAni("idle");
	}
}