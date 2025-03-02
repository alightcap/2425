let playerTowerImg;
let enemyTowerImg;
let neutralTowerImg;
let playerSoldierImg;

let playerStartTower;
let enemyStartTower;
let neutralTower1;
let neutralTower2;

function preload() {
	playerTowerImg = loadImage('assets/tower-round-build-b.png');
	enemyTowerImg = loadImage('assets/tower-square-build-a.png');
	neutralTowerImg = loadImage('assets/tower-round-top-a.png');

	playerSoldierImg = loadImage('assets/enemy-ufo-a.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	playerStartTower = createTower(playerTowerImg);
	playerStartTower.x = 200;
	playerStartTower.y = height / 2;
	newPlayerTower(playerStartTower);

	enemyStartTower = createTower(enemyTowerImg);
	enemyStartTower.x = width - 200;
	enemyStartTower.y = height / 2;

	neutralTower1 = createTower(neutralTowerImg);
	neutralTower1.x = width / 2 - 50;
	neutralTower1.y = height / 2 - 50;

	neutralTower2 = createTower(neutralTowerImg);
	neutralTower2.x = width / 2 + 50;
	neutralTower2.y = height / 2 + 50;

	playerStartTower.setTarget(neutralTower1);
}

function draw() {
	background('skyblue');

}

function createTower(towerImg) {
	let t = new Sprite();
	t.scale = 2;
	t.img = towerImg;

	return t;
}

function newPlayerTower(tower) {
	tower.img = playerTowerImg;

	tower.numSoldiers = 0;
	tower.maxSoldiers = 20;

	tower.soliderRefreshRate = 1000;
	tower.refreshTimer = 0;

	tower.soldierSendRate = 2000;
	tower.sendTimer = 0;

	tower.textSize = 20;
	tower.textColor = 'white';
	tower.textStroke = 'black';
	tower.text = tower.numSoldiers;

	tower.target = null;

	tower.update = () => {
		tower.addSolider();
		tower.sendSoldier();
	}

	tower.addSolider = () => {
		tower.refreshTimer += deltaTime;
		if (tower.refreshTimer > tower.soliderRefreshRate) {
			if (tower.numSoldiers < tower.maxSoldiers) {
				tower.refreshTimer = 0;
				tower.numSoldiers += 1;
				tower.text = tower.numSoldiers;
			}
		}
	}

	tower.sendSoldier = () => {
		tower.sendTimer += deltaTime;
		if (tower.target != null) {
			if (tower.sendTimer > tower.soldierSendRate) {
				if (tower.numSoldiers > 0) {
					let s = newSoldier(playerSoldierImg, tower.pos, tower.target.pos);
					// create a soldier with the same target to move to
					tower.sendTimer = 0;
					tower.numSoldiers -= 1;
					tower.text = tower.numSoldiers;

				}
			}
		}
	}

	tower.setTarget = (targetTower) => {
		tower.target = targetTower;
	}
}

function newSoldier(soldierImg, startPos, targetPos) {
	let s = new Sprite();
	s.img = soldierImg;
	s.pos = startPos;
	s.targetPos = targetPos;
	s.collider = 'none';

	s.update = () => {
		s.moveTo(s.targetPos.x, s.targetPos.y);
	}
}

