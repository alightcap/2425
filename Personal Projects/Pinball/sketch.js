let ball;
let pegs;
let pegLayout = [
	[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
	[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
	[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
];

let pegSpacing;
let leftBound;
let rightBound;


function setup() {
	new Canvas(600, 800);
	displayMode('centered');
	world.gravity.y = 10;

	pegSpacing = width / (pegLayout[0].length + 1);

	ball = createBall();
	pegs = setupPegs();
	
	for (let i = 0; i < pegLayout.length; i++) {
		for (let j = 0; j < pegLayout[0].length; j++) {
			if (pegLayout[i][j] == 1) {
				let peg = new pegs.Sprite();
				peg.x = pegSpacing + j * pegSpacing;
				peg.y = height / 2 + i * pegSpacing;
			}
		}
	}

	leftBound = new Sprite();
	leftBound.x = pegs[10].x - pegSpacing;
	leftBound.y = pegs[10].y - 2 * pegSpacing;
	leftBound.collider = 'static';
	leftBound.rotation = 45;
	leftBound.height = 400;
	leftBound.color = 'gold';
	leftBound.bounciness = 1;

	rightBound = new Sprite();
	rightBound.x = pegs[14].x + pegSpacing;
	rightBound.y = pegs[14].y - 2 * pegSpacing; 
	rightBound.collider = 'static';
	rightBound.rotation = -45;
	rightBound.height = 400;
	rightBound.color = 'gold';
	rightBound.bounciness = 1;
}

function draw() {
	background('skyblue');

	if (mouse.pressed()) {
		createBall();
	}
}

function createBall() {
	let ball = new Sprite();
	ball.x = width / 2 + random([-2, -1, 1, 2]);
	ball.y = 50;
	ball.radius = 15;
	ball.color = 'green';
	ball.bounciness = .5;
	return ball;
}

function setupPegs() {
	pegs = new Group();
	pegs.radius = 5;
	pegs.color = "yellow";
	pegs.collider = "static";
	pegs.bounciness = 1;
	return pegs;
}
