import {config} from "./config.js"
import {Editor} from "./create.js"


//Camera and keyboard classes :
class Keyboard{
    constructor(disable=true){
        this.keys={};
        this.disable = disable;
        addEventListener("keydown", (e) => {if(!this.disable){this.keys[e.key]=true}});
        addEventListener("keyup", (e) => {if(!this.disable){this.keys[e.key]=false}});
    }
}

class Camera{
    constructor(ctx){
        this.ctx = ctx;
        this.x = 0;
        this.y = 0;
        this.z = 0;
        this.zoom = 1;
        this.zoomEcran = 1;
        this.move = false;
    }

    moveTo(x,y){
        this.x = x;
        this.y = y;
    }

};


//Game Manager class :
export class GameManager{
    constructor(){
        this.canvas = document.getElementById('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.ctx.canvas.width  = window.innerWidth;
        this.ctx.canvas.height = window.innerHeight;
        this.opacity = 1;


        this.ratioEcran = this.ctx.canvas.width / this.ctx.canvas.height;
        this.refEcran = 2873;
        this.diagonalEcran = Math.sqrt((-this.ctx.canvas.width)**2+(-this.ctx.canvas.height)**2);
        this.camRatio = (this.diagonalEcran/this.refEcran);

        this.camera = new Camera(this.ctx);
        this.keyBoard = new Keyboard(false);
        this.editor = new Editor();

        this.gameState = "editor";

        this.mouseX = 0;
        this.mouseY = 0;

        this.grid = 49;

        console.log(this.editor.tiles_type_list); 

        this.editor.create_preview_tile(0,0);

        addEventListener("resize", (e) => {
            this.ctx.canvas.width = window.innerWidth;
            this.ctx.canvas.height = window.innerHeight;

            this.ratioEcran = this.ctx.canvas.width / this.ctx.canvas.height;

            this.diagonalEcran = Math.sqrt((-this.ctx.canvas.width)**2+(-this.ctx.canvas.height)**2);
            this.camRatio = (this.diagonalEcran/this.refEcran);

            this.camera.zoomEcran = this.camera.zoom * this.camRatio;
        });
        addEventListener('mousemove', this.mouse_move.bind(this)); //Ecouteur d'évènement pour la souris
        addEventListener('mousedown', this.mouse_down.bind(this)); //Ecouteur d'évènement pour la souris
        addEventListener('wheel', this.mouse_wheel.bind(this)); //Ecouteur d'évènement pour la souris
    }

    mouse_move(e){
        this.mouseX = e.clientX;
        this.mouseY = e.clientY;
        this.mouseX = Math.round(this.mouseX/this.grid)*this.grid;
        this.mouseY = Math.round(this.mouseY/this.grid)*this.grid;
        Math.round(this.mouseX/this.grid),Math.round(this.mouseY/this.grid)
        if (this.gameState == "editor"){
            this.editor.move_preview_tile(this.mouseX-this.grid/2,this.mouseY-this.grid/2);
            }
    }

    mouse_down(e){
        if (this.gameState == "editor"){
            let mouseX_world = (this.mouseX / this.camera.zoomEcran) - (0.5 * window.innerWidth / this.camera.zoomEcran);
            let mouseY_world = (this.mouseY / this.camera.zoomEcran) - (0.5 * window.innerHeight / this.camera.zoomEcran);
    
            let tileX = Math.floor(mouseX_world / this.grid)*this.grid;
            let tileY = Math.floor(mouseY_world / this.grid)*this.grid;

            Math.round(this.tileX/this.grid)-this.grid*0.5,Math.round(this.tileY/this.grid)-this.grid*0.5;

            if (e.button == 0){
                this.editor.place_tile(tileX, tileY);
            }
            else if (e.button == 1){
                this.editor.remove_tile(tileX, tileY);
            }
        }
    }
    

    mouse_wheel(e){
        if (this.gameState == "editor"){
            if (e.deltaY < 0){
                this.editor.change_preview_tile(1);
            }
            else if (e.deltaY > 0){
                this.editor.change_preview_tile(-1);
            }
        }
    }

    update(){
        this.ctx.canvas.width = window.innerWidth;
        this.ctx.canvas.height = window.innerHeight;
        this.ctx.globalAlpha = this.opacity;
        this.camera.zoomEcran = this.camera.zoom * this.camRatio;

        if (this.keyBoard.keys["z"]){this.camera.y -= 2; console.log(this.camera.y);}
        if (this.keyBoard.keys["s"]){this.camera.y += 2; console.log(this.camera.y);}
        if (this.keyBoard.keys["q"]){this.camera.x -= 2; console.log(this.camera.x);}
        if (this.keyBoard.keys["d"]){this.camera.x += 2; console.log(this.camera.x);}





        this.display(this.camera);
    }

    display(camera){
        this.ctx.clearRect(0,0,this.ctx.canvas.width, this.ctx.canvas.height);

        if (this.gameState == "editor"){
            if (this.editor.tiles.length > 0){
                for (let i = 0; i < this.editor.tiles.length; i++){
                    this.editor.tiles[i].display(camera);
                }
            }
            if (this.editor.tile_preview != null){
                this.editor.tile_preview.display(camera);
            }
        }

    }

}