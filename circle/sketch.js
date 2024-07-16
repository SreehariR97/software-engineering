/*
 * @name Simple Shapes
 * @arialabel Grey canvas with 4 pink shapes: a circle, a rectangle, a triangle, and a flower
 * @description This examples includes a circle, square, triangle, and a flower.
 */

x = 100
y = 100
dx = 1
dy = 1

function setup() {
}

function draw() {
  // Create the canvas
  createCanvas(720, 400);
  background(200);

  // Set colors
  fill(0, 101, 192, 127);
  stroke(127, 63, 120);

  // A rectangle
  rect(40, 120, 120, 40);
  // An ellipse
  ellipse(240, 240, 80, 80);
  // A triangle
  triangle(300, 100, 320, 100, 310, 80);

  // A design for a simple flower
  translate(580, 200);
  noStroke();
  for (let i = 0; i < 10; i ++) {
    ellipse(0, 30, 20, 80);
    rotate(PI/5);
  }

  // a circle
  ellipse(x, y, 200, 200);
  x = x + dx;
  y = y + dy;
  if (x > 300) {
    x = 0;
  }
  if (y > 300) {
    y = 0;
  }
}
