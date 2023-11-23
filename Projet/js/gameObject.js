//Class pour les objets du jeu
export class GameObject{
    constructor(x,y,img,size=1){
        this.img = new Image();
        this.img.src = img;
        this.xMap = x;
        this.yMap = y;
        this.xEcran = 0;
        this.yEcran = 0;
        this.size = size;
        this.img.onload = () => {
            this.w = this.img.width;
            this.h = this.img.height;
        }
    }

    update(){
        this.w = this.img.width*this.size;
        this.h = this.img.height*this.size;
    }

    display(camera){
        this.xEcran = 0.5*window.innerWidth+(this.xMap-this.w*0.5-camera.x)*camera.zoomEcran;
        this.yEcran = 0.5*window.innerHeight+(this.yMap-this.h*0.5-camera.y)*camera.zoomEcran;
        camera.ctx.drawImage(this.img, this.xEcran, this.yEcran, this.w*camera.zoomEcran, this.h*camera.zoomEcran);
    }
};

export class ScreenObject{
    constructor(x,y,img,size=1){
        this.img = new Image();
        this.img.src = img;
        this.xEcran = x;
        this.yEcran = y;
        this.size = size;
        this.img.onload = () => {
            this.w = this.img.width;
            this.h = this.img.height;
        }
    }

    update(){
        this.w = this.img.width*this.size;
        this.h = this.img.height*this.size;
    }

    display(camera){
        camera.ctx.drawImage(this.img, this.xEcran, this.yEcran, this.w, this.h);
    }
};