EMPTY = 0;

HORIZONTAL = 0;
VERTICAL = 1;

PLAYER_ONE_ITEM = 1;
PLAYER_TWO_ITEM = 2;

class DotsBox {
    constructor(index, row, col) {
        this.index = index;
        this.rowNum = row;
        this.colNum = col;
        this.item = EMPTY;
    }

    placeItem(item) {
        this.item = item;
    }
}

class DotsEdge {
    constructor(orientation, index, row, col) {
        this.orientation = orientation;
        this.index = index;
        this.rowNum = row;
        this.colNum = col;
        this.item = EMPTY;
    }

    placeItem(item) {
        this.item = item;
    }
}

class DotsBoard {
    constructor(numDotRows, numDotCols) {
        this.numDotRows = numDotRows;
        this.numDotCols = numDotCols;

        this.numBoxRows = this.numDotRows - 1;
        this.numBoxCols = this.numDotCols - 1;

        this.numHorizontalEdgeRows = this.numDotRows;
        this.numHorizontalEdgecols = this.numDotCols - 1;

        this.numVerticalEdgeRows = this.numDotRows - 1;
        this.numVerticalEdgeCols = this.numDotCols;

        this.boxes = this.makeBoxes();
        this.horizontalEdges = this.makeHorizontalEdges();
        this.verticalEdges = this.makeVerticalEdges();
    }

    getBox(rowNum, colNum) {
        for (let box of this.boxes) {
            if (box.rowNum == rowNum && box.colNum == colNum) {
                return box;
            }
        }
    }

    getBoxes(edge) {
        let boxes = [];
        if (edge.orientation == HORIZONTAL) {
            // i am the south edge
            if (edge.rowNum > 0) {
                let westEdge = this.getEdge(VERTICAL, edge.rowNum - 1, edge.colNum);
                let northEdge = this.getEdge(HORIZONTAL, edge.rowNum - 1, edge.colNum);
                let eastEdge = this.getEdge(VERTICAL, edge.rowNum - 1, edge.colNum + 1);
                if (westEdge.item * northEdge.item * eastEdge.item == 1) {
                    boxes.push(this.getBox(edge.rowNum - 1, edge.colNum));
                }
            }
            // look down
            if (edge.rowNum < this.numHorizontalEdgeRows - 1) {
                // i am the north edge
                let westEdge = this.getEdge(VERTICAL, edge.rowNum, edge.colNum);
                let southEdge = this.getEdge(HORIZONTAL, edge.rowNum + 1, edge.colNum);
                let eastEdge = this.getEdge(VERTICAL, edge.rowNum, edge.colNum + 1);
                if (westEdge.item * southEdge.item * eastEdge.item == 1) {
                    boxes.push(this.getBox(edge.rowNum, edge.colNum));
                }
            }
        }

        if (edge.orientation == VERTICAL) {
            // look left
            if (edge.colNum > 0) {
                let westEdge = this.getEdge(VERTICAL, edge.rowNum, edge.colNum - 1);
                let northEdge = this.getEdge(HORIZONTAL, edge.rowNum, edge.colNum - 1);
                let southEdge = this.getEdge(HORIZONTAL, edge.rowNum + 1, edge.colNum - 1);
                if (westEdge.item * northEdge.item * southEdge.item == 1) {
                    boxes.push(this.getBox(edge.rowNum, edge.colNum - 1));
                }
            }
            // look right
            if (edge.colNum < this.numVerticalEdgeCols - 1) {
                let eastEdge = this.getEdge(VERTICAL, edge.rowNum, edge.colNum + 1);
                let northEdge = this.getEdge(HORIZONTAL, edge.rowNum, edge.colNum);
                let southEdge = this.getEdge(HORIZONTAL, edge.rowNum + 1, edge.colNum);
                if (eastEdge.item * northEdge.item * southEdge.item == 1) {
                    boxes.push(this.getBox(edge.rowNum, edge.colNum));
                }
            }
        }
        return boxes;
    }

    getEdge(orientation, rowNum, colNum) {
        let edges;
        if (orientation == HORIZONTAL) {
            edges = this.horizontalEdges;
        }
        if (orientation == VERTICAL) {
            edges = this.verticalEdges;
        }

        for (let edge of edges) {
            if (edge.rowNum == rowNum && edge.colNum == colNum) {
                return edge;
            }
        }
    }

    getWinner() {
        let itemOne = this.boxes[0].item;
        let itemTwo;
        let itemOneCount = 0;
        let itemTwoCount = 0;

        for (let box of this.boxes) {
            if (box.item == itemOne) {
                itemOneCount++;
            } else {
                if (!itemTwo) {
                    itemTwo = box.item;
                }
                itemTwoCount++;
            }
        }

        if (itemOneCount > itemTwoCount) {
            console.log("box1 wins", itemOne);
            return itemOne;
        } else if (itemTwoCount > itemOneCount) {
            console.log("box1 does not win", itemTwo)
            return itemTwo;
        } else {
            console.log("it's a tie");
            return "tie";
        }
    }

    isFull() {
        for (let edge of this.horizontalEdges) {
            if (edge.item == EMPTY) {
                return false;
            }
        }
        for (let edge of this.verticalEdges) {
            if (edge.item == EMPTY) {
                return false;
            }
        }
        return true;
    }

    makeBoxes() {
        let boxes = [];
        let index = 0;

        for (let rowNum = 0; rowNum < this.numBoxRows; rowNum++) {
            for (let colNum = 0; colNum < this.numBoxCols; colNum++) {
                let box = new DotsBox(index, rowNum, colNum);
                boxes.push(box);
                index++;
            }
        }
        return boxes;
    }

    makeHorizontalEdges() {
        let horizontalEdges = [];
        let index = 0;

        for (let edgeRow = 0; edgeRow < this.numHorizontalEdgeRows; edgeRow++) {
            for (let edgeCol = 0; edgeCol < this.numHorizontalEdgeCols; edgeCol++) {
                let edge = new DotsEdge(HORIZONTAL, index, edgeRow, edgeCol);
                horizontalEdges.push(edge);
                index++;
            }
        }
        return horizontalEdges;
    }

    makeVerticalEdges() {
        let verticalEdges = [];
        let index = 0;

        for (let edgeRow = 0; edgeRow < this.numVerticalEdgeRows; edgeRow++) {
            for (let edgeCol = 0; edgeCol < this.numVerticalEdgeCols; edgeCol++) {
                let edge = new DotsEdge(VERTICAL, index, edgeRow, edgeCol);
                verticalEdges.push(edge);
                index++;
            }
        }
        return verticalEdges;
    }

    placeBox(rowNum, colNum, item) {
        // rowNum and colNum should be in box coords
        let index = (rowNum * this.numBoxCols) + colNum;
        this.boxes[index] = item;
    }

    placeHorizontalEdge(rowNum, colNum, item) {
        let index = (rowNum * this.numHorizontalEdgeCols) + colNum;
        this.horizontalEdges[index] = item;
    }

    placeVerticalEdge(rowNum, colNum, item) {
        let index = (rowNum * this.numVerticalEdgeCols) + colNum;
        this.verticalEdges[index] = item;
    }
}