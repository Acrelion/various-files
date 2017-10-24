// Example of canvas animation. Originally it used setInterval, but I've changed it
// to use requestAnimationFrame.
// CONTENT: It creates a simple solar system animation.

var star = new Image();
var moon = new Image();
var earth = new Image();

function setupContext(ctx) {
    ctx.globalCompositeOperation = "destination-over";
    ctx.clearRect(0, 0, 300, 300);

    ctx.fillStyle = "rgba(0, 0, 0, 0.4)";
    ctx.strokeStyle = "rgba(0, 153, 255, 0.4)";
    ctx.save();
    ctx.translate(150, 150);
}

function drawEarth(ctx, time){
    ctx.rotate( ((2 * Math.PI) / 60) * time.getSeconds()  +
        ((2 * Math.PI) / 60000) * time.getMilliseconds() );
    ctx.translate(105, 0);
    ctx.fillRect(9, -12, 50, 24);
    ctx.drawImage(earth, -12, -12);
}

function drawMoon(ctx, time) {
    ctx.rotate( ((2*Math.PI) / 6) * time.getSeconds() +
        ((2 * Math.PI)/ 6000)* time.getMilliseconds() );
    ctx.translate(0, 28.5);
    ctx.drawImage(moon, -3.5, -3.5);
    ctx.restore();
}

function drawOrbit(ctx) {
    ctx.beginPath();
    ctx.arc(150, 150, 105, 0, Math.PI * 2, false); // earth orbit
    ctx.stroke();
}

function drawPlanet() {
    var ctx = document.getElementById("tutorial").getContext("2d");

    setupContext(ctx);

    var time = new Date();
    //Earth
    drawEarth(ctx, time);

    //Moon
    ctx.save();
    drawMoon(ctx, time);

    ctx.restore();

    drawOrbit(ctx);

    ctx.drawImage(star, 0, 0, 300, 300);

    requestAnimationFrame(drawPlanet);
}

function init() {
    star.src = "https://mdn.mozillademos.org/files/1456/Canvas_sun.png";
    moon.src = "https://mdn.mozillademos.org/files/1443/Canvas_moon.png";
    earth.src = "https://mdn.mozillademos.org/files/1429/Canvas_earth.png";

    drawPlanet();
}

init();






