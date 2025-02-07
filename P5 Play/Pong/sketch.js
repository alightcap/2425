// let startButtonUnpressed;
// let startButtonPressed;
// let fieldSheet;
// let goalTopLeftCorner;
// let goalLeftEdge;
// let goalBottomLeftCorner;
// let goalTopRightCorner;
// let goalRightEdge;
// let goalBottomRightCorner;
// let ballImg;
let tileWidth = 13;
let tileHeight = 9
let tileSize = 64;
let blueIceSheet;
let redIceSheet;
let blueIceTiles;
let redIceTiles;
let backgroundImg;
let elementSheet;


class StartMenuScene {
	constructor() {
	}

	enter() {
		this.title = new Sprite(width / 2, height / 2 - 40, 0, 0, 'none');
		this.title.textSize = 40;
		this.title.text = "Pong";

		this.startButton = new Sprite(width / 2, height / 2 + 40, 192 / 2, 64 / 2, 'static');
		// not sure why the width and height of this button asset needs to be halved...
		this.startButton.unpressedImg = startButtonUnpressed;
		this.startButton.pressedImg = startButtonPressed;
		this.startButton.img = this.startButton.unpressedImg;
		this.startButton.textSize = 25;
		this.startButton.text = "Start";
		this.startButton.resetButton = () => {
			this.startButton.img = this.startButton.unpressedImg;
			this.startButton.textColor = 'black';
		}
	}

	async interact() {
		if (this.startButton.mouse.hovering()) {
			mouse.cursor = 'grab';
		} else {
			mouse.cursor = 'default';
			this.startButton.resetButton();
		}

		if (this.startButton.mouse.pressing()) {
			this.startButton.img = this.startButton.pressedImg;
			this.startButton.textColor = 'white';
		}

		if (this.startButton.mouse.pressed()) {
			this.startButton.resetButton();
			await delay(250);
			this.exit();
		}
	}

	exit() {
		this.title.remove();
		this.startButton.remove();
		return 1;
	}
}

class GameScene {
	constructor() {
		this.tiles;
		this.makeGrassTiles();
		this.createPaddles();
		this.createBoundaries();
		this.createGoalSprites();
		this.createBall();
	}

	enter() {

	}

	interact() {
		this.drawGrass();
		this.drawGoals();
		this.leftPaddle.updatePaddle();
		this.rightPaddle.updatePaddle();
		this.ball.updateBall();
	}

	exit() {

	}

	createBall() {
		this.ball = new Sprite();

		this.ball.moveSpeed = 5;

		this.ball.x = width / 2;
		this.ball.y = height / 2;
		this.ball.img = ballImg;
		this.ball.r = 5;
		this.ball.scale = 3;
		this.ball.direction = random(360);
		this.ball.speed = this.ball.moveSpeed;
		this.ball.bounciess = 1;
		// this.ball.debug = true;

		this.ball.updateBall = () => {
			// this.ball.speed = this.ball.moveSpeed;
		}
	}

	createBoundaries() {
		let north = new Sprite();
		north.x = width / 2;
		north.y = 0;
		north.w = width;
		north.h = tileSize / 4;
		north.collider = 'static';
		north.visible = false;
		// north.bounciness = 1;
		// north.friction = 0;

		let south = new Sprite();
		south.x = width / 2;
		south.y = height;
		south.w = width;
		south.h = tileSize / 4;
		south.collider = 'static';
		south.visible = false;
		// south.bounciness = 1;
		// south.friction = 0;
	}

	createGoalSprites() {
		this.leftGoal = new Sprite();
		this.leftGoal.x = tileSize / 4;
		this.leftGoal.y = height / 2;
		this.leftGoal.w = tileSize / 2;
		this.leftGoal.height = height;
		this.leftGoal.collider = 'static';
		this.leftGoal.visible = false;
		// this.leftGoal.bounciness = 1;
		// this.leftGoal.friction = 0;

		this.rightGoal = new Sprite();
		this.rightGoal.x = width - tileSize / 4;
		this.rightGoal.y = height / 2;
		this.rightGoal.w = tileSize / 2;
		this.rightGoal.height = height;
		this.rightGoal.collider = 'static';
		this.rightGoal.visible = false;
		// this.rightGoal.bounciness = 1;
		// this.rightGoal.friction = 0;
	}

	createPaddles() {
		this.leftPaddle = new Sprite();
		this.leftPaddle.xPos = tileSize * 1.5;
		this.leftPaddle.x = this.leftPaddle.xPos;
		this.leftPaddle.y = height / 2;
		this.leftPaddle.w = tileSize / 3;
		this.leftPaddle.h = tileSize * 1.75;
		this.leftPaddle.color = '#6CABDD';
		this.leftPaddle.rotationLock = true;
		// this.leftPaddle.bounciness = 1;
		// this.leftPaddle.friction = 0;

		this.leftPaddle.moveSpeed = 3.5;

		this.leftPaddle.updatePaddle = () => {
			this.leftPaddle.x = this.leftPaddle.xPos;
			this.leftPaddle.vel.y = 0;
			if (kb.pressing('w')) {
				this.leftPaddle.vel.y = -this.leftPaddle.moveSpeed;
			}
			if (kb.pressing('s')) {
				this.leftPaddle.vel.y = this.leftPaddle.moveSpeed;
			}
		}

		this.rightPaddle = new Sprite();
		this.rightPaddle.xPos = width - tileSize * 1.5;
		this.rightPaddle.x = this.rightPaddle.xPos;
		this.rightPaddle.y = height / 2;
		this.rightPaddle.w = tileSize / 3;
		this.rightPaddle.h = tileSize * 1.75;
		this.rightPaddle.color = '#c8102E';
		this.rightPaddle.rotationLock = true;
		// this.rightPaddle.bounciness = 1;
		// this.rightPaddle.friction = 0;

		this.rightPaddle.moveSpeed = 3.5;

		this.rightPaddle.updatePaddle = () => {
			this.rightPaddle.x = this.rightPaddle.xPos;
			this.rightPaddle.vel.y = 0;
			if (kb.pressing('arrowUp')) {
				this.rightPaddle.vel.y = -this.rightPaddle.moveSpeed;
			}
			if (kb.pressing('arrowDown')) {
				this.rightPaddle.vel.y = this.rightPaddle.moveSpeed;
			}
		}
	}

	drawGrass() {
		for (let rowIdx = 0; rowIdx < tileHeight; rowIdx++) {
			for (let colIdx = 0; colIdx < tileWidth; colIdx++) {
				let x = colIdx * tileSize;
				let y = rowIdx * tileSize;

				let grass = this.field[rowIdx][colIdx];
				let img;
				switch (grass) {
					case 0:
						img = this.northWestCorner;
						break;
					case 1:
						img = this.northEdge;
						break;
					case 2:
						img = this.northEdgeCenterLine;
						break;
					case 3:
						img = this.northEastcorner;
						break;
					case 4:
						img = this.westEdge;
						break;
					case 5:
						img = this.emptyGrass;
						break;
					case 6:
						img = this.eastEdge;
						break;
					case 7:
						img = this.southWestCorner;
						break;
					case 8:
						img = this.southEdge;
						break;
					case 9:
						img = this.southEdgeCenterLine;
						break;
					case 10:
						img = this.southEastCorner;
						break;
					case 11:
						img = this.northWestCircle;
						break;
					case 12:
						img = this.northCircle;
						break;
					case 13:
						img = this.northEastCircle;
						break;
					case 14:
						img = this.westCircle;
						break;
					case 15:
						img = this.eastCircle;
						break;
					case 16:
						img = this.southWestCircle;
						break;
					case 17:
						img = this.southCircle;
						break;
					case 18:
						img = this.southEastCircle;
						break;
					case 19:
						img = this.centerLine;
						break;
				}
				image(img, x, y, tileSize);
			}
		}
	}

	drawGoals() {
		image(goalTopLeftCorner, 0, 0, tileSize, tileSize);
		image(goalTopRightCorner, width - tileSize, 0, tileSize, tileSize);
		for (let rowIdx = 1; rowIdx < height / tileSize - 1; rowIdx++) {
			image(goalLeftEdge, 0, rowIdx * tileSize, tileSize, tileSize);
			image(goalRightEdge, width - tileSize, rowIdx * tileSize, tileSize, tileSize);
		}
		image(goalBottomLeftCorner, 0, height - tileSize, tileSize, tileSize);
		image(goalBottomRightCorner, width - tileSize, height - tileSize, tileSize, tileSize);

	}

	makeGrassTiles() {
		this.tiles = [];
		for (let rowIdx = 0; rowIdx < 16; rowIdx++) {
			for (let colIdx = 0; colIdx < 13; colIdx++) {
				let tile = fieldSheet.get(colIdx * tileSize, rowIdx * tileSize, tileSize, tileSize);
				this.tiles.push(tile);
			}
		}

		this.emptyGrass = this.tiles[0];
		this.northWestCorner = this.tiles[1];
		this.northEdge = this.tiles[2];
		this.northEdgeCenterLine = this.tiles[3];
		this.northEastcorner = this.tiles[4];
		this.westEdge = this.tiles[14];
		this.centerLine = this.tiles[16];
		this.eastEdge = this.tiles[17];
		this.southWestCorner = this.tiles[13 * 3 + 1];
		this.southEdge = this.tiles[13 * 3 + 2];
		this.southEdgeCenterLine = this.tiles[13 * 3 + 3];
		this.southEastCorner = this.tiles[13 * 3 + 4];
		this.northWestCircle = this.tiles[7];
		this.northCircle = this.tiles[13 * 3 + 7];
		this.northEastCircle = this.tiles[9];
		this.westCircle = this.tiles[13 * 1 + 7];
		this.eastCircle = this.tiles[13 * 1 + 9];
		this.southWestCircle = this.tiles[13 * 2 + 7];
		this.southCircle = this.tiles[13 * 3 + 9];
		this.southEastCircle = this.tiles[13 * 2 + 9];

		this.field = [
			[0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3],
			[4, 5, 5, 5, 5, 5, 19, 5, 5, 5, 5, 5, 6],
			[4, 5, 5, 5, 5, 5, 19, 5, 5, 5, 5, 5, 6],
			[4, 5, 5, 5, 5, 11, 12, 13, 5, 5, 5, 5, 6],
			[4, 5, 5, 5, 5, 14, 19, 15, 5, 5, 5, 5, 6],
			[4, 5, 5, 5, 5, 16, 17, 18, 5, 5, 5, 5, 6],
			[4, 5, 5, 5, 5, 5, 19, 5, 5, 5, 5, 5, 6],
			[4, 5, 5, 5, 5, 5, 19, 5, 5, 5, 5, 5, 6],
			[7, 8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 10],
		]
	}

}


let startMenu;

function preload() {
	// startButtonUnpressed = 'assets/button_rectangle_depth_gradient.png';
	// startButtonPressed = 'assets/button_rectangle_gradient.png';
	// // font = loadFont('assets/Kenney Future.ttf');
	// fieldSheet = loadImage('assets/groundGrass_mown.png');
	// goalBottomLeftCorner = loadImage('assets/element (54).png');
	// goalBottomRightCorner = loadImage('assets/element (50).png');
	// goalLeftEdge = loadImage('assets/element (45).png');
	// goalRightEdge = loadImage('assets/element (41).png');
	// goalTopLeftCorner = loadImage('assets/element (36).png');
	// goalTopRightCorner = loadImage('assets/element (32).png');
	// ballImg = loadImage('assets/ball_soccer4.png');
	blueIceSheet = loadImage('assets/groundIce_blue.png');
	redIceSheet = loadImage('assets/groundIce_red.png');
	elementSheet = loadImage('assets/elements.png');
}

function setup() {
	new Canvas(tileWidth * tileSize, tileHeight * tileSize);
	displayMode('centered');

	backgroundImg = generateBackground();
	// startMenu = new StartMenuScene();
	// startMenu.enter();
	// game = new GameScene();
	// game.enter();
}

function draw() {
	background(backgroundImg);
	// startMenu.interact();
	// game.interact();
}

function generateBackground() {
	blueIceTiles = sliceSpriteSheet(blueIceSheet);
	redIceTiles = sliceSpriteSheet(redIceSheet);
	elementTiles = sliceSpriteSheet(elementSheet);

	let img = createImage(tileWidth * tileSize, tileHeight * tileSize);

	let tile = blueIceTiles[0];
	for (let rowIdx = 0; rowIdx < img.height / tileSize; rowIdx++) {
		for (let colIdx = 0; colIdx < img.width / tileSize; colIdx++) {
			img.set(colIdx * tileSize, rowIdx * tileSize, tile);
		}
	}
	img.updatePixels();

	return img;
}

function sliceSpriteSheet(img) {
	let tiles = [];

	for (let rowIdx = 0; rowIdx < (img.width / tileSize); rowIdx++) {
		for (let colIdx = 0; colIdx < (img.height / tileSize); colIdx++) {
			let tile = img.get(colIdx * tileSize, rowIdx * tileSize, tileSize, tileSize);
			tiles.push(tile)
		}
	}
	return tiles;
}
