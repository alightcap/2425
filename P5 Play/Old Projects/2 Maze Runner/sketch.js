let dino;
let dinoImg;
let dinoSpeed;
let gemImg;
let isGameOver = false;
let gameOverText;

function preload() {
    dinoImg = "assets/static_dino.png";
    gemImg = "assets/green gem.png";
}

function setup() {
    new Canvas(800, 600);
    setupPlayer();

    makeBoundary();
    makeWalls();
    gem = new Sprite();
    gem.img = gemImg;
    gem.x = width - 50;
    gem.y = height / 2;

    gameOverText = new Sprite();
    gameOverText.visible = false;
    gameOverText.text = "You Win!";
    gameOverText.x = width / 2;
    gameOverText.y = height / 2;
    gameOverText.width = 0;
    gameOverText.height = 0;
    gameOverText.textSize = 100;
    gameOverText.textStroke = "black";
    gameOverText.textColor = "white";
    gameOverText.textStrokeWeight = 6;
    gameOverText.collider = "none";

}

function draw() {
    background(180);

    playerControl();

    if (dino.overlaps(gem)) {
        gem.remove();
        gameOver();
    }
}

function gameOver() {
    isGameOver = true;
    gameOverText.visible = true;
}


function makeWalls() {
    for (let i = 0; i < 4; i++) {
        wall = new Sprite();
        wall.width = 20;
        wall.height = height - 200;
        wall.x = 200 * i + 100;
        wall.y = height / 2;
        wall.color = "blue";
        wall.collider = "static";
    }

    for (let i = 0; i < 3; i++) {
        wall = new Sprite();
        wall.width = 20;
        wall.height = height / 2 - 100;
        wall.x = 200 * i + 200;
        wall.y = 100;
        wall.color = "blue";
        wall.collider = "static";

        wall = new Sprite();
        wall.width = 20;
        wall.height = height / 2 - 100;
        wall.x = 200 * i + 200;
        wall.y = height - 100;
        wall.color = "blue";
        wall.collider = "static";
    }

    wall = new Sprite();
    wall.width = 100;
    wall.height = 20;
    wall.x = 50;
    wall.y = 100;
    wall.color = "blue";
    wall.collider = "static";

    wall = new Sprite();
    wall.width = 100;
    wall.height = 20;
    wall.x = 50 * 5;
    wall.y = 400;
    wall.color = "blue";
    wall.collider = "static";

    wall = new Sprite();
    wall.width = 100;
    wall.height = 20;
    wall.x = 50 * 9;
    wall.y = 200;
    wall.color = "blue";
    wall.collider = "static";

    wall = new Sprite();
    wall.width = 100;
    wall.height = 20;
    wall.x = 50 * 15;
    wall.y = 500;
    wall.color = "blue";
    wall.collider = "static";
}

function makeBoundary() {
    bottomBoundary = new Sprite();
    bottomBoundary.width = width;
    bottomBoundary.height = 20;
    bottomBoundary.x = width / 2;
    bottomBoundary.y = height;
    bottomBoundary.color = "blue";
    bottomBoundary.collider = "static";

    topBoundary = new Sprite();
    topBoundary.width = width;
    topBoundary.height = 20;
    topBoundary.x = width / 2;
    topBoundary.y = 0;
    topBoundary.color = "blue";
    topBoundary.collider = "static";

    leftBoundary = new Sprite();
    leftBoundary.width = 20;
    leftBoundary.height = height;
    leftBoundary.x = 0;
    leftBoundary.y = height / 2;
    leftBoundary.color = "blue";
    leftBoundary.collider = "static";

    rightBoundary = new Sprite();
    rightBoundary.width = 20;
    rightBoundary.height = height;
    rightBoundary.x = width;
    rightBoundary.y = height / 2;
    rightBoundary.color = "blue";
    rightBoundary.collider = "static";
}

function setupPlayer() {
    dino = new Sprite();
    dino.img = dinoImg;
    dino.scale = 2;
    dinoSpeed = 5;
    dino.x = 24;
    dino.y = height / 2;
    dino.width = 24;
    dino.height = 24;
    dino.rotationLock = true;
    dino.friction = 0;
    // dino.debug = true;
}

function playerControl() {
    if (isGameOver) {
        dino.vel = new p5.Vector(0, 0);
        return;
    }

    let inputVector = new p5.Vector(0, 0);

    if (kb.pressing('right')) {
        inputVector.x = 1;
    }

    if (kb.pressing('left')) {
        inputVector.x = -1;
    }

    if (kb.pressing('down')) {
        inputVector.y = 1;
    }

    if (kb.pressing('up')) {
        inputVector.y = -1;
    }

    inputVector.normalize();
    dino.vel = inputVector.mult(dinoSpeed);
    if (dino.vel.x < 0) {
        dino.mirror.x = true;
    }

    if (dino.vel.x > 0) {
        dino.mirror.x = false;
    }
}