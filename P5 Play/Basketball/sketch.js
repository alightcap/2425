let player;
let playerIdleAni;
let playerRunAni;
let playerSpeed = 5;
let gravityStrength = 10;
let ground;
let basketball;
let basketballImg;


function preload() {
	playerIdleAni = loadAni(
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
}

function draw() {
	background('skyblue');

	playerController();
	// console.log(player.joints[0]["spriteB"].overlapping(ground));
}

function createBasketball() {
	let basketball = new Sprite();
	// basketball.debug = true;
	basketball.img = basketballImg;
	basketball.radius = 10;
	basketball.bounciness = 0.67;
	basketball.overlaps(player);
	basketball.x = width / 2 + 50;

	return basketball;
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

	player.jumpForce = -6;
	player.shotForce = createVector(3, -6);
	player.bounciness = 0;
	player.isShooting = false;

	let groundSensor = new Sprite();
	groundSensor.r = 8;
	groundSensor.collider = 'none';
	groundSensor.mass = 0.01;
	groundSensor.x = player.x
	groundSensor.y = player.y + player.height;
	groundSensor.visible = false;
	player.groundSensor = groundSensor;

	let j = new GlueJoint(player, player.groundSensor);
	j.visible = false;

	player.anis["idle"] = playerIdleAni;
	player.anis["move"] = playerRunAni;
	player.changeAni("idle");

	player.rotationLock = true;
	player.scale = 2;
	// player.debug = true;

	player.isGrounded = true;

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
		if (player.isGrounded) {
			player.isGrounded = false;
			player.vel.y = player.jumpForce;
		}
	}

	if (player.groundSensor.overlapping(ground)) {
		if (player.vel.y > 0) {
			player.isGrounded = true;
		}
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
			basketball.vel = player.shotForce;
		}
	}

	if (player.overlapped(basketball) && player.isShooting) {
		player.isShooting = false;
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