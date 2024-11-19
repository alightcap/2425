let board;
let boardSprite;

function setup() {
	new Canvas(500, 500);
	displayMode('centered');

	board = new DotsBoard(4, 7);
	let margin = 50;
	let xStart = margin;
	let yStart = 150;
	let boardWidth = width - 2 * margin;
	let boardHeight = height - (margin + yStart);

	boardSprite = new DotsBoardSprite(board, xStart, yStart, boardWidth, boardHeight);
}

function draw() {
	background('skyblue');
	boardSprite.displayBoard();
}
