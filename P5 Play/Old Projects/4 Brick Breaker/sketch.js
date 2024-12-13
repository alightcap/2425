let backgroundImg;
let paddle;
let paddleSpeed;
let paddlePosY;
let ball;
let ballSpeed;
let walls;
let bricks;
let tiles;
let score = 0;
let scoreUI;
let endgameUI;
let isGameOver = false;

function preload() {
    backgroundImg = loadImage("assets/Space Background.png");
}

function setup() {
    new Canvas(800, 600);

    setupScoreUI();
    setupEndgameUI();
    setupWalls();
    setupPaddle();
    setupBricks();
    setupBall();
}

function draw() {
    background(backgroundImg);

    movePaddle();
    ball.speed = ballSpeed;

    if (ball.y > canvas.h) {
        isGameOver = true;
        gameOver("lose");
    }

    if (bricks.length < 1) {
        isGameOver = true;
        gameOver("win");
    }
}

function bounce(ball, paddle) {
    ball.direction += (ball.x - paddle.x);
}

function damageBrick(ball, brick) {
    // brick.hits -= 1;
    // brick.color = "blue";
    // if (brick.hits < 1) {
    //     brick.remove();
    // }
    brick.remove();
    score++;
    scoreUI.text = "Score: " + score;
}

function gameOver(result) {
    console.log("game over");
    if (result == "win") {
        endgameUI.text = "You Win!";
    }

    if (result == "lose") {
        endgameUI.text = "Game Over";
    }
    endgameUI.visible = true;
    noLoop();
}

function movePaddle() {
    paddle.moveTowards(mouse.x, paddlePosY, 1);
}

function setupBall() {
    ballSpeed = 7;
    ball = new Sprite(canvas.w / 2, canvas.h / 2, 20);
    ball.bounciness = 1;
    ball.friction = 0;
    ball.direction = 80;

    ball.speed = ballSpeed;

    ball.collides(paddle, bounce);
    ball.collides(bricks, damageBrick);
}

function setupBricks() {
    bricks = new Group();
    bricks.color = "green";
    bricks.collider = "static";
    bricks.w = 40;
    bricks.h = 20;
    // bricks.hits = 2;
    bricks.tile = "-";
    tiles = new Tiles(
        [
            "---------------",
            "-----.....-----",
            "---.........---",
            "-.............-",
            "---.........---",
            "-----.....-----",
            "---------------"
        ],
        90,
        100,
        bricks.w + 4,
        bricks.h + 4
    );
}

function setupEndgameUI() {
    endgameUI = new Sprite(canvas.w / 2, canvas.h / 2, 0, 0, "n");
    endgameUI.visible = false;
    endgameUI.textSize = 100;
    endgameUI.textColor = "white";
    endgameUI.layer = 10;
}

function setupPaddle() {
    paddlePosY = canvas.h - 50;
    paddle = new Sprite(canvas.w / 2, paddlePosY, 100, 20);
    paddle.color = "green";
    paddle.rotationLock = true;
}

function setupScoreUI() {
    scoreUI = new Sprite(125, 50, 0, 0, "n");
    scoreUI.text = "Score: " + score;
    scoreUI.textSize = 50;
    scoreUI.textColor = "white";
}

function setupWalls() {
    walls = new Group();
    walls.color = "green";
    walls.collider = "static";
    new walls.Sprite(0, height / 2, 20, height);
    new walls.Sprite(width, height / 2, 20, height);
    new walls.Sprite(width / 2, 0, width, 20);
}

