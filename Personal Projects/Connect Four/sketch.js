let boardSprite;

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	boardSprite = setupBoard();
}

function draw() {
	background('skyblue');

}

function setupBoard() {
	b = new Sprite();
	b.board = new Board();
	b.cellSize = 50;

	b.x = 100;
	b.y = 100;

	b.draw = () => {
		for (let r = 0; r < 2; r++) {
			for (let c = 0; c < 2; c++) {
				rect(b.y + c * b.cellSize, b.x + r * b.cellSize, b.cellSize);
			}
		}
	}

	return b;
}