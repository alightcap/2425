
let asteroids;
let asteroidAnis = [];
let backgroundImg;
let bulletAni;
let bullets;
let engine;
let explosionSheet;
let isGameActive;
let level = 0;
let playButton;
let playButtonImg;
let playButtonAni;
let planet;
let shipImg;
let ship;
let score;
let scoreUI;


function preload() {
    backgroundImg = loadImage('assets/dark space.png');
    shipImg = loadImage('assets/ship.png');
    bulletAni = loadAni('assets/bolt1.png', 4);
    explosionSheet = loadImage('assets/explosion sheet.png');
    asteroidAnis.push(loadAni('assets/asteroid1.gif'));
    asteroidAnis.push(loadAni('assets/asteroid2.gif'));
    asteroidAnis.push(loadAni('assets/asteroid3.gif'));
    playButtonImg = loadImage('assets/play01.png');
    playButtonAni = loadAni('assets/play01.png', 5);
    playButtonAni.noLoop();
}

function setup() {
    new Canvas(800, 600);

    isGameActive = false;

    planet = new Sprite(canvas.w / 2, canvas.h / 2, "n");
    planet.ani = 'assets/planet.gif';

    setupShip();
    setupBullets();
    setupAsteroids();
    setupPlayButton();
    setupScoreUI();

    score = 0;
}

function draw() {
    background(backgroundImg);

    if (!isGameActive) {
        playButton.visible = true;
        if (playButton.mouse.pressed()) {
            playButton.addAni(playButtonAni);
            setTimeout(() => {
                playButton.visible = false;
                newGame();
            }, 600);
        }
    }

    if (isGameActive) {
        updateGame();
    }
}

function newGame() {
    asteroids.removeAll();
    level = 0;
    score = 0;
    updateScore(0);
    isGameActive = true;
    resetShip();
    ship.visible = true;

    setTimeout(() => {
        if (ship.vel.mag() == 0) {
            ship.applyForce(5);
        }
    }, 1000);

}

function damageAsteroid(asteroid, bullet) {
    spawnExplosion(asteroid.x, asteroid.y);
    bullet.remove();
    asteroid.hits--;

    if (asteroid.hits > 0) {
        a1 = new asteroids.Sprite(asteroid.x, asteroid.y);
        a1.rotation = asteroid.rotation + 90;
        a1.direction = a1.rotation;
        a1.ani = asteroidAnis[asteroid.hits - 1];
        a1.scale = 0.25 + 0.25 * asteroid.hits;
        a1.speed = 3;
        a1.hits = asteroid.hits;

        a2 = new asteroids.Sprite(asteroid.x, asteroid.y);
        a2.rotation = asteroid.rotation - 90;
        a2.direction = a2.rotation;
        a2.ani = asteroidAnis[asteroid.hits - 1];
        a2.scale = 0.25 + 0.25 * asteroid.hits;
        a2.speed = 3;
        a2.hits = asteroid.hits;
    }

    updateScore(3 - asteroid.hits)
    asteroid.remove();
}

function endGame() {
    isGameActive = false;
    spawnExplosion(ship.x, ship.y);
    ship.visible = false;
}

function resetShip() {
    ship.x = canvas.w / 2;
    ship.y = canvas.h / 2;
    ship.vel.x = 0;
    ship.vel.y = 0;
    ship.rotation = 90;
    ship.rotationSpeed = 0;
    ship.visible = true;
}

function setupAsteroids() {
    asteroids = new Group();
    asteroids.hits = 3;
    asteroids.ani = asteroidAnis[2];
    asteroids.overlaps(asteroids);
    asteroids.collides(ship, endGame);
    asteroids.collides(bullets, damageAsteroid);
    asteroids.layer = 2;
}

function setupBullets() {
    bullets = new Group();
    bullets.scale = 0.75;
    bullets.ani = bulletAni;
    bullets.diameter = 15;
    bullets.life = 200;
    bullets.overlaps(ship);
    bullets.overlaps(bullets);
    bullets.layer = 2;
}

function setupShip() {
    ship = new Sprite(canvas.w / 2, canvas.h / 2, 10);
    ship.rotation = 90;
    ship.img = shipImg;
    ship.scale = 2.5;
    ship.drag = 0.05;
    ship.rotationDrag = 10;
    ship.visible = false;

    engine = new Sprite(ship.x - 20, ship.y, 10, 10);
    engine.ani = 'assets/thruster.gif';
    engine.rotation = 90;
    engine.scale = 1.5;
    engine.visible = false;
    engine.mass = 0.001;
    engine.overlaps(allSprites);
    let j = new GlueJoint(ship, engine);
    j.visible = false;
    ship.layer = 2;
    engine.layer = 2;
}

function shipMovement() {
    if (!isGameActive) {
        return;
    }

    if (kb.pressing('up')) {
        ship.bearing = ship.rotation - 90;
        engine.visible = true;
        ship.applyForce(1);
    } else {
        engine.visible = false;
    }

    if (kb.pressing('left')) {
        // ship.applyTorque(-0.01);
        ship.rotationSpeed -= 1;
    }

    if (kb.pressing('right')) {
        ship.rotationSpeed += 1;
        // ship.applyTorque(0.01);
    }

    if (kb.presses('space')) {
        shoot();
    }

    if (ship.x > canvas.w) {
        ship.x = 0;
    }

    if (ship.x < 0) {
        ship.x = canvas.w;
    }

    if (ship.y > canvas.h) {
        ship.y = 0;
    }

    if (ship.y < 0) {
        ship.y = canvas.h;
    }
}

function shoot() {
    let b = new bullets.Sprite();
    b.removeColliders();
    b.addCollider(-10, 0, 12);
    b.x = ship.x;
    b.y = ship.y;
    b.rotation = ship.rotation + 90;
    b.direction = b.rotation;
    b.speed = -10;
}

function setupPlayButton() {
    playButton = new Sprite();
    playButton.collider = "none";
    playButton.img = playButtonImg;
    playButton.w = 128;
}

function setupScoreUI() {
    scoreUI = new Sprite(125, 50, 0, 0, "n");
    scoreUI.textSize = 50;
    scoreUI.textColor = "white";
    scoreUI.text = "Score: 0";
    scoreUI.layer = 1;
    textAlign(LEFT);
}

function spawnAsteroid() {
    let shipPos = createVector(ship.x, ship.y);
    a = new asteroids.Sprite();
    a.x = random(0, canvas.w);
    a.y = random(0, canvas.h);
    let aPos = createVector(a.x, a.y);
    while (shipPos.dist(aPos) < 100) {
        a.x = random(0, canvas.w);
        a.y = random(0, canvas.h);
        aPos = createVector(a.x, a.y);
    }
    a.rotation = random(0, 360);
    a.speed = 2;
}

function spawnExplosion(x, y) {
    explosion = new Sprite(x, y, 64, 64, "n");
    explosion.life = 100;
    explosion.spriteSheet = explosionSheet;
    explosion.addAnis({ run: { row: 10, frames: 8 } });
    explosion.anis['run'].noLoop();
    explosion.changeAni('run');
}

function updateGame() {
    shipMovement();
    wrapAsteroids();

    if (asteroids.length == 0) {
        level++;
        for (let i = 0; i < level; i++) {
            spawnAsteroid();
        }
        if (level > 1) {
            updateScore((level - 1) * 10);
        }
    }
}

function updateScore(scoreToAdd) {
    score += scoreToAdd;
    scoreUI.text = "Score: " + score;
}

function wrapAsteroids() {
    for (let a of asteroids) {
        if (a.x < 0) {
            a.x = canvas.w;
        }

        if (a.x > canvas.w) {
            a.x = 0;
        }

        if (a.y < 0) {
            a.y = canvas.h;
        }

        if (a.y > canvas.h) {
            a.y = 0;
        }
    }
}