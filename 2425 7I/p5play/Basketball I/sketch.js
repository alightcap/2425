let player;
let playerIdleAnimation;
let playerRunAnimation;

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

	player = createPlayer();
}

function draw() {
	background('skyblue');

	playerController();
}

function createPlayer() {
	let p = new Sprite();

	p.moveSpeed = 5;

	p.scale = 5;
	p.addAni('run', playerRunAnimation);
	p.addAni('idle', playerIdleAnimation);

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

	player.vel.x = inputX * player.moveSpeed;

	playerVisuals();
}

function playerVisuals() {
	if (player.isMoving) {
		player.changeAni('run');
	} else {
		player.changeAni('idle');
	}
}
