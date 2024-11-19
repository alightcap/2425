let player;
let playerIdleAni;
let playerRunAni;
let playerSpeed = 5;
let isGrounded = false;
let playerJumpForce = -7;
let gravityStrength = 10;
let ground;

function preload() {
	playerIdleAni = loadAni(
		"assets/idle.png",
		{ frameSize: [24, 24], frames: 3 }
	);
	playerIdleAni.frameDelay = 6;

	playerRunAni = loadAni(
		"assets/move.png",
		{ frameSize: [24, 24], frames: 6 }
	);
	playerRunAni.frameDelay = 6;
}

function setup() {
	new Canvas(800, 600);
	world.gravity.y = gravityStrength;

	player = createPlayer();
	ground = createGround();
}

function draw() {
	background('skyblue');

	playerController();
	console.log(player.joints[0]["spriteB"].overlapping(ground));
}

function createGround() {
	let ground = new Sprite();
	ground.x = width / 2;
	ground.y = height;
	ground.w = width;
	ground.h = 20;
	ground.collider = "static";
	ground.color = "green";
	return ground;
}

function createPlayer() {
	let player = new Sprite();

	player.x = width / 2;
	player.y = height - 24;

	player.w = 16;
	player.h = 16;

	let groundSensor = new Sprite();
	groundSensor.r = 8;
	groundSensor.collider = 'none';
	groundSensor.mass = 0.01;
	groundSensor.x = player.x
	groundSensor.y = player.y + 16;
	groundSensor.visible = false;

	let j = new GlueJoint(player, groundSensor);
	j.visible = false;

	player.anis["idle"] = playerIdleAni;
	player.anis["move"] = playerRunAni;
	player.changeAni("idle");

	player.rotationLock = true;
	player.scale = 2;
	// player.debug = true;
	return player;
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
		// if (isGrounded) {
		// 	isGrounded = false;
		player.vel.y = playerJumpForce;
		// }
	}

	inputVector.normalize().mult(playerSpeed);
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