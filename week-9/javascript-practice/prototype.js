'use script';

function PowerRanger(color) {
  this.color = color;
}

function Fighter() {
  this.isPowerfull = true;
}

var proto = {isPowerfull: true};
PowerRanger.prototype = new Fighter;

var yellowRanger = new PowerRanger('yellow');

console.log(yellowRanger.isPowerfull);
console.log(yellowRanger.color);
