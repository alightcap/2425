class DotsBoxSprite {
    constructor(box, boxData) {
        this.sprite = new Sprite();

    }
}

class DotsBoardSprite {
    constructor(board, x, y, w, h) {
        this.board = board;
        this.xPos = x;
        this.yPos = y;

        this.boxSizeX = w / board.numBoxCols;
        this.boxSizeY = h / board.numBoxRows;

        this.dots = this.getDotPositions();
        // this.edges = this.makeEdges();
        // this.boxes = this.makeBoxes();
    }

    displayBoard() {
        this.drawDots();

    }

    drawDots() {
        for (let dot of this.dots) {
            fill(0);
            noStroke();
            ellipse(dot[0], dot[1], 10);
        }
    }

    getDotPositions() {
        let dotPositions = [];

        for (let dotRow = 0; dotRow < this.board.numDotRows; dotRow++) {
            for (let dotCol = 0; dotCol < this.board.numDotCols; dotCol++) {
                let xPos = this.xPos + dotCol * this.boxSizeX;
                let yPos = this.yPos + dotRow * this.boxSizeY;

                dotPositions.push([xPos, yPos]);
            }
        }

        return dotPositions;
    }


}