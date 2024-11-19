let dino;
let dinoIdle;
let dinoWalk;
let dinoSpeed = 5;
let coinAnimation;
let coin;
let gameOverSprite;
let maze = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
	[1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
	[1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
	[1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
];

function preload() {
	dinoIdle = loadAni(
		"assets/idle.png",
		{ frameSize: [24, 24], frames: 3 }
	);
	dinoIdle.frameDelay = 6;

	dinoWalk = loadAni(
		"assets/move.png",
		{ frameSize: [24, 24], frames: 6 }
	);
	dinoWalk.frameDelay = 6;

	coinAnimation = loadAni(
		"assets/red_coin.png",
		{ frameSize: [16, 16], frames: 5 }
	);
	coinAnimation.frameDelay = 12;
}

function setup() {
	new Canvas(768, 576);

	dino = createCharacter();
	coin = createCoin();
	coin.overlaps(dino);
	makeMaze(maze);
	gameOverSprite = createGameOverSprite();
}

function draw() {
	background('lightgray');

	characterController();
	updateCharacterVisuals();

	if (dino.overlaps(coin)) {
		coin.remove();
		gameOverSprite.visible = true;
	}
}

function characterController() {
	let inputVector = createVector(0, 0);

	if (kb.pressing('left')) {
		inputVector.x = -1;
	}

	if (kb.pressing('right')) {
		inputVector.x = 1;
	}

	if (kb.pressing('up')) {
		inputVector.y = -1;
	}

	if (kb.pressing('down')) {
		inputVector.y = 1;
	}

	inputVector.normalize().mult(dinoSpeed);
	dino.vel.x = inputVector.x;
	dino.vel.y = inputVector.y;
}

function createCharacter() {
	dino = new Sprite();
	dino.anis["idle"] = dinoIdle;
	dino.anis["walk"] = dinoWalk;
	dino.scale = 2;
	dino.changeAni("idle");
	dino.x = 48 + 24;
	dino.y = height / 2;
	dino.rotationLock = true;
	dino.w = 27;
	dino.h = 33;
	// dino.debug = true;
	return dino;
}

function createCoin() {
	let coin = new Sprite();
	coin.anis["idle"] = coinAnimation;
	coin.changeAni("idle");
	coin.w = 16;
	coin.h = 16;
	coin.x = width - 2 * 48 - 24;
	coin.y = 48 + 24;
	coin.rotationLock = true;
	coin.scale = 1.5;
	return coin;
}

function createGameOverSprite() {
	let s = new Sprite();
	s.collider = "none";
	s.text = "You Win!";
	s.textSize = 180;
	s.w = 0;
	s.h = 0;
	s.visible = false;
	return s
}

function makeMaze(maze) {
	for (let i = 0; i < maze.length; i++) {
		for (let j = 0; j < maze[0].length; j++) {
			if (maze[i][j] == 1) {
				let wall = new Sprite();
				wall.width = 48;
				wall.height = 48;
				wall.collider = 'static';
				wall.color = 'green';
				wall.x = j * 48 + 24;
				wall.y = i * 48 + 24;
			}
		}
	}
}

function updateCharacterVisuals() {
	if (dino.vel.x < 0) {
		dino.mirror.x = true;
	}

	if (dino.vel.x > 0) {
		dino.mirror.x = false;
	}

	if (dino.isMoving) {
		dino.changeAni("walk");
	} else {
		dino.changeAni("idle");
	}
}