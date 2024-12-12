let dots = [];
let numDots = 3;
let colors = ["red", "green", "blue"];

function preload() {

}

function setup() {
    new Canvas(800, 600);

    for (let i = 0; i < numDots; i++) {
        let dot = new Sprite();
        dot.radius = 25;
        dot.x = width / 2;
        dot.y = height / 2;
        dot.vel = p5.Vector.random2D();
        dot.speed = random(5, 8);
        dot.overlaps(allSprites);
        dot.color = colors[i];
        dots.push(dot);
    }
}

function draw() {
    background(180);

    for (let i = 0; i < dots.length; i++) {
        if (dots[i].x < 0 + dots[i].radius) {
            dots[i].vel.x *= -1;
        }

        if (dots[i].x > width - dots[i].radius) {
            dots[i].vel.x *= -1;
        }

        if (dots[i].y < 0 + dots[i].radius) {
            dots[i].vel.y *= -1;
        }

        if (dots[i].y > height - dots[i].radius) {
            dots[i].vel.y *= -1;
        }
    }
}

function mouseClicked() {
    let dot = new Sprite();
    dot.radius = 25;
    dot.x = width / 2;
    dot.y = height / 2;
    dot.vel = p5.Vector.random2D();
    dot.speed = random(5, 8);
    dot.overlaps(allSprites);
    dot.color = random(colors);
    dots.push(dot);
}