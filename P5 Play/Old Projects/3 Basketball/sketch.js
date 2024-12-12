let dino;
let ground;
let groundSensor;
let basketball;
let backboard;
let frontRim;
let shooting = false;
let score = 0;
let scoreUI;
let targetX;
let targetY;

function preload() {

}

function setup() {
    new Canvas(800, 600);
    world.gravity.y = 10;
    textAlign(CENTER);

    setupPlayer();
    setupGoal();
    setupEnvironment();

    scoreUI = new Sprite();
    scoreUI.width = 0;
    scoreUI.height = 0;
    scoreUI.collider = "none";
    scoreUI.x = 150;
    scoreUI.y = 100;
    scoreUI.textSize = 50;
    scoreUI.layer = 100;
    scoreUI.text = "Score: " + score;


    basketball = new Sprite();
    basketball.x = 615;
    basketball.y = 50;
    basketball.img = "assets/basketball.png";
    basketball.diameter = 16;
    basketball.bounciness = 0.5;
    basketball.layer = 2;
    basketball.overlaps(dino);
    basketball.overlaps(backboard);
    basketball.overlaps(frontRim);
    // basketball.debug = true;
}

function draw() {
    background(180);

    playerController();

    updateGoal();

    if (basketball.overlapped(frontRim)) {
        if (basketball.vel.y > 0) {
            updateScore();
            moveGoal();
        }
    }
}

function updateScore() {
    score += 1;
    scoreUI.textSize *= 1.2;
    setTimeout(() => { scoreUI.textSize /= 1.2 }, 100);
    scoreUI.text = "Score: " + score;
}

function updateGoal() {
    if (abs(backboard.x - targetX) < 1) {
        backboard.x = targetX;
        backboard.vel.x = 0;
    }

    if (abs(backboard.y - targetY) < 1) {
        backboard.y = targetY;
        backboard.vel.y = 0;
    }
}

function moveGoal() {
    targetX = random(150, width - 150);
    targetY = random(height / 4 + 100, height / 2 - 100);
    backboard.moveTowards(targetX, targetY, 0.1);
}

function playerController() {
    dino.vel.x = 0;
    if (kb.pressing('left')) {
        dino.vel.x = -5;
        dino.mirror.x = true;
    }

    if (kb.pressing('right')) {
        dino.vel.x = 5;
        dino.mirror.x = false;
    }

    if (groundSensor.overlapping(ground)) {
        if (kb.presses('up')) {
            dino.vel.y = -7;
        }
    }

    if (dino.overlaps(basketball) && !shooting) {
        basketball.x = dino.x;
        basketball.y = dino.y;
        new GlueJoint(dino, basketball);
    }

    if (kb.pressing(' ')) {
        shooting = true;
        setTimeout(() => { shooting = false }, 1000);
        if (dino.joints[1]) {
            dino.joints[1].remove();
            basketball.vel.y = -10;
            if (dino.mirror.x) {
                basketball.vel.x = -3 + dino.vel.x;
                basketball.applyTorque(1);
            } else {
                basketball.vel.x = 3 + dino.vel.x;
                basketball.applyTorque(-1);
            }

        }
    }
}

function setupEnvironment() {
    ground = new Sprite();
    ground.width = width;
    ground.height = 20;
    ground.x = width / 2;
    ground.y = height;
    ground.color = "black";
    ground.collider = "static";

    leftWall = new Sprite();
    leftWall.width = 20;
    leftWall.height = height;
    leftWall.x = 0;
    leftWall.y = height / 2;
    leftWall.collider = "static";
    leftWall.visible = false;

    rightWall = new Sprite();
    rightWall.width = 20;
    rightWall.height = height;
    rightWall.x = width;
    rightWall.y = height / 2;
    rightWall.collider = "static";
    rightWall.visible = false;
}

function setupGoal() {
    backboard = new Sprite();
    backboard.width = 150;
    backboard.height = 100;
    backboard.x = 600;
    backboard.y = height / 2;
    backboard.layer = 1;
    backboard.color = "white";
    backboard.collider = "kinematic";

    leftRim = new Sprite();
    leftRim.width = 5;
    leftRim.height = 5;
    leftRim.x = backboard.x - 20;
    leftRim.y = backboard.y + backboard.hh / 2;
    leftRim.color = "orange";
    leftRim.layer = 3;
    let j = new GlueJoint(leftRim, backboard);
    j.visible = false;

    rightRim = new Sprite();
    rightRim.width = 5;
    rightRim.height = 5;
    rightRim.x = backboard.x + 20;
    rightRim.y = backboard.y + backboard.hh / 2;
    rightRim.color = "orange";
    rightRim.layer = 3;
    let j2 = new GlueJoint(rightRim, backboard);
    j2.visible = false;

    frontRim = new Sprite();
    frontRim.width = 40;
    frontRim.height = 5;
    frontRim.x = backboard.x;
    frontRim.y = backboard.y + backboard.hh / 2;
    frontRim.color = "orange";
    frontRim.layer = 4;
    let j3 = new GlueJoint(frontRim, backboard);
    j3.visible = false;

}

function setupPlayer() {
    dino = new Sprite();
    dino.image = "assets/static_dino2.png";
    dino.scale = 3;
    // dino.debug = true;
    dino.width = 12 * 3;
    dino.height = 12 * 3 + 15;
    dino.rotationLock = true;
    dino.friction = 0;

    groundSensor = new Sprite();
    groundSensor.x = dino.x;
    groundSensor.y = dino.y + dino.halfWidth + 10;
    groundSensor.width = dino.width;
    groundSensor.height = 20;
    groundSensor.collider = "none";
    groundSensor.visible = false;

    let j = new GlueJoint(dino, groundSensor);
    j.visible = false;
}
