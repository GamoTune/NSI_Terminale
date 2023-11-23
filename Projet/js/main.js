import { GameManager } from "./gameManager.js";


window.onload = function(){init()};

var mainGameManager;

function init(){
    mainGameManager = new GameManager();
    main_loop();
}

function main_loop(){
    mainGameManager.update(mainGameManager);
    window.requestAnimationFrame(function(){main_loop()});
}