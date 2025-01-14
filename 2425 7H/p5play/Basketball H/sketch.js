let player;
let playerIdleAnim;

function preload() {
	playerIdleAnim = loadAni(
		'assets/idle.png',
		{ frameSize: [24, 24], frames: 3 }
	)

	playerIdleAnim.frameDelay = 6;
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

	p.addAni('idle', playerIdleAnim);
	p.scale = 5;

	p.moveSpeed = 5;

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
}