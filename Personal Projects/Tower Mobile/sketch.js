let playerTowerImg;
let enemyTowerImg;
let neutralTowerImg;
let playerSoldierImg;
let enemySoldierImg;
let selectedImg;

let playerStartTower;
let enemyStartTower;
let enemyTowers = [];

let towers;
let soldiers;
let indicator;
let selectedTower = null;

function preload() {
	playerTowerImg = loadImage('assets/tower-round-build-b.png');
	enemyTowerImg = loadImage('assets/tower-square-build-a.png');
	neutralTowerImg = loadImage('assets/tower-round-top-a.png');

	playerSoldierImg = loadImage('assets/enemy-ufo-a.png');
	enemySoldierImg = loadImage('assets/enemy-ufo-c.png');

	selectedImg = loadImage('assets/tile_0009.png');
}

function setup() {
	new Canvas(800, 600);
	displayMode('centered');

	towers = createTowerGroup();
	soldiers = createSoldierGroup();

	let pos = new Vector(200, height / 2);
	playerStartTower = newPlayerTower(pos);

	pos = new Vector(width - 200, height / 2);
	enemyStartTower = newEnemyTower(pos);
	enemyTowers.push(enemyStartTower);

	for (let x = 0; x < 300; x += 100) {
		for (let y = 0; y < 300; y += 100) {
			let pos = new Vector(x + 300, y + 200);
			newNeutralTower(pos);
		}
	}

	// pos = new Vector(width / 2 - 50, height / 2 - 50);
	// neutralTower1 = newNeutralTower(pos);

	// pos = new Vector(width / 2 + 50, height / 2 + 50);
	// neutralTower2 = newNeutralTower(pos);

	indicator = new Sprite();
	indicator.rotation = 45;
	indicator.collider = 'none';
	indicator.visible = false;
	indicator.img = selectedImg;
	indicator.scale = 3;
	indicator.layer = 1;

	soldiers.overlaps(
		towers,
		(soldier, tower) => {
			tower.receiveSoldier(soldier);
		}
	)
	soldiers.overlapped(
		towers,
		(soldier, tower) => {
			soldier.toggleReceivable();
		}
	)
}

function draw() {
	background('skyblue');

	for (let tower of towers) {
		for (let target of tower.targets) {
			strokeWeight(5);
			stroke('black');
			line(tower.x, tower.y, target.x, target.y);
			strokeWeight(2);
			stroke('white')
			line(tower.x, tower.y, target.x, target.y);
		}
	}

	updateComputer();
}

function createSoldier(soldierImg, startPos, targetPos, owner) {
	let s = new soldiers.Sprite();
	s.img = soldierImg;
	s.pos = startPos;
	s.targetPos = targetPos;
	s.collider = 'none';
	s.owner = owner;
	s.receivable = false;

	s.w = 5;
	s.h = 5;
	// s.debug = true;

	s.moveTo(s.targetPos.x, s.targetPos.y);

	s.toggleReceivable = () => {
		s.receivable = true;
	}
}

function createSoldierGroup() {
	let g = new Group();

	return g;
}

function createTowerGroup() {
	let g = new Group();

	return g;
}

function newEnemyTower(pos) {
	let tower = newTower();
	tower.pos = pos;

	tower.owner = 'enemy';
	tower.img = enemyTowerImg;
	tower.soldierImg = enemySoldierImg;

	tower.maxSoldiers = 20;
	tower.refreshRate = 1000;
	tower.sendRate = 750;

	enemyTowers.push(tower);

	return tower;
}

function newPlayerTower(pos) {
	let tower = newTower();
	tower.pos = pos;

	tower.owner = 'player';
	tower.img = playerTowerImg;
	tower.soldierImg = playerSoldierImg;

	tower.maxSoldiers = 20;
	tower.refreshRate = 1000;
	tower.sendRate = 750;

	return tower;
}

function newTower() {
	let t = new towers.Sprite();
	t.owner = '';
	t.soldierImg = null;
	t.scale = 2;
	t.w = 15;
	t.h = 15;
	// t.debug = true;
	t.layer = 2;

	t.numSoldiers = 0;
	t.maxSoldiers = 0;

	t.refreshRate = 0;
	t.refreshTimer = 0;

	t.sendRate = 0;
	t.sendTimer = 0;

	t.selected = false;

	t.textSize = 20;
	t.textColor = 'white';
	t.textStroke = 'black';
	t.text = t.numSoldiers;

	t.targets = [];
	t.targetIndex = 0;

	t.update = () => {
		t.addSoldier();
		t.sendSoldier();

		if (t.mouse.pressed()) {
			towerClicked(t);
		}

		t.text = t.numSoldiers;
	}

	t.addSoldier = () => {
		t.refreshTimer += deltaTime;
		if (t.refreshTimer > t.refreshRate) {
			if (t.numSoldiers < t.maxSoldiers) {
				t.refreshTimer = 0;
				t.numSoldiers += 1;
			}
		}
	}

	t.receiveSoldier = (soldier) => {
		if (soldier.receivable) {
			if (soldier.owner == t.owner) {
				t.numSoldiers += 1;
			} else {
				t.numSoldiers -= 1;
				if (t.numSoldiers == 0) {
					if (t.owner == '') {
						if (soldier.owner == 'player') {
							t.remove();
							t = newPlayerTower(t.pos);
						} else {
							t.remove();
							t = newEnemyTower(t.pos);
						}
					} else {
						t.remove();
						t = newNeutralTower(t.pos);
						if (t.owner == 'enemy') {
							idx = enemyTowers.indexOf(t);
							enemyTowers.splice(idx, 1);
						}
					}

				}
			}
			soldier.remove();
		}
	}

	t.sendSoldier = () => {
		t.sendTimer += deltaTime;
		if (t.targets.length > 0) {
			if (t.sendTimer > t.sendRate) {
				if (t.numSoldiers > 0) {
					t.sendTimer = 0;
					createSoldier(t.soldierImg, t.pos, t.targets[t.targetIndex].pos, t.owner);
					t.targetIndex = (t.targetIndex + 1) % t.targets.length;
					t.numSoldiers -= 1;
				}
			}
		}
	}

	t.addTarget = (targetTower) => {
		t.targets.push(targetTower);
	}

	t.removeTarget = (targetTower) => {
		let idx = t.targets.indexOf(targetTower);
		t.targets.splice(idx, 1);
	}

	return t;
}

function newNeutralTower(pos) {
	let tower = newTower();
	tower.pos = pos;
	tower.img = neutralTowerImg;
	tower.numSoldiers = 10;

	return tower;
}

function towerClicked(tower) {
	// nothing already selected -> if this tower is mine, select it
	// something already selected 
	//     -> if this tower is already selected, un-select it
	//     -> different tower, close enough, add it to targets of selected tower
	// this feels gross, not sure how to clean it up.
	if (selectedTower == null) {
		if (tower.owner == 'player') {
			selectedTower = tower;
		}
	} else {
		if (selectedTower == tower) {
			selectedTower = null;
		} else {
			let idx = selectedTower.targets.indexOf(tower);
			if (idx > -1) {
				selectedTower.targets.splice(idx, 1);
				selectedTower = null;
			} else {
				if (dist(selectedTower.x, selectedTower.y, tower.x, tower.y) < 200) {
					selectedTower.targets.push(tower);
					selectedTower = null;
				}
			}
		}
	}

	if (selectedTower == null) {
		indicator.visible = false;
	} else {
		indicator.visible = true;
		indicator.x = selectedTower.x;
		indicator.y = selectedTower.y;
	}
}

let enemyCooldown = 2000;
let enemyTimer = 0;
function updateComputer() {
	enemyTimer += deltaTime;
	if (enemyTimer > enemyCooldown) {
		for (let tower of enemyTowers) {
			if (tower.targets.length == 0) {
				if (tower.numSoldiers > 5) {
					let targets = [];
					for (let target of towers) {
						if (isValidEnemyTarget(tower, target)) {
							targets.push(target);
						}
					}
					if (targets.length > 0) {
						tower.addTarget(random(targets));
						enemyTimer = 0;
					}
				}
			}
		}
	}
}

function isValidEnemyTarget(tower, target) {
	if (tower == target) {
		return false;
	}

	if (tower.targets.indexOf(target) >= 0) {
		return false;
	}

	if (target.targets.indexOf(tower) >= 0) {
		return false;
	}

	if (target.x > tower.x) {
		return false;
	}

	if (dist(tower.x, tower.y, target.x, target.y) >= 200) {
		return false;
	}

	return true;
}
