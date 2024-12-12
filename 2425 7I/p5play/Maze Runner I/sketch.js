let dino;
let dinoIdle;
let dinoWalk;

function preload() {
    dinoIdle = loadAni(
        'assets/idle.png',
        { frameSize: [24, 24], frames: 3}
    );
    dinoIdle.frameDelay = 6;

    dinoWalk = loadAni(
        'assets/move.png',
        { frameSize: [24, 24], frames: 6 }
    );
    dinoWalk.frameDelay = 6;
}

function setup() {
    new Canvas(768, 576);

    dino = new Sprite();
    dino.addAni('idle', dinoIdle);
    dino.addAni('walk', dinoWalk);
    dino.scale = 2;
}

function draw() {
    background('skyblue');
}