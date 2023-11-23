//Fichier pour l'éditeur de niveau
import {GameObject, ScreenObject} from "./gameObject.js";
import {config} from "./config.js";

export class Editor{
    constructor(){
        this.tiles = []; //Liste des tuiles
        this.index_tile = 0; //Index de la tuile sélectionnée
        this.tiles_type_list = []; //Liste des types de tuiles
        for (let i in config.module){ 
            this.tiles_type_list.push(i); //Liste des types de tuiles
        };
        this.tile_selected = this.tiles_type_list[this.index_tile]; //Tuile sélectionnée
        this.tile_preview = null;
        this.config = config;
    }
    select_tile(scroll){
        this.index_tile += scroll;
        if (this.index_tile > 11){
            this.index_tile = 0;
        }
        else if (this.index_tile < 0){
            this.index_tile = 11;
        }
        this.tile_selected = this.tiles_type_list[this.index_tile];
        this.change_preview_tile();
    }

    //Fonction pour créer une tuile de prévisualisation
    create_preview_tile(x,y){ //Faut changer ça, faut plusieurs fonctions (comme vu en cours) pour changer de tuile, placer une tuile, etc...
        if (this.tile_preview == null){
            this.tile_preview = new Tile(x,y,config.module[this.tile_selected].path_opatity,1);
        }
    }

    //Fonction pour déplacer la tuile de prévisualisation
    move_preview_tile(x,y){
        if (this.tile_preview != null){
            this.tile_preview.xEcran = x;
            this.tile_preview.yEcran = y;
        }
    }
    
    //Fonction pour changer la tuile de prévisualisation
    change_preview_tile(){
        if (this.tile_preview != null){
            this.tile_preview.img.src = config.module[this.tile_selected].path_opatity;
        }
    }


    place_tile(x,y){
        let tile = new Tile(x,y,config.module[this.tile_selected].path,1);
        this.tiles.push(tile);
    }

    remove_tile(x,y){
        for (let i = 0; i < this.tiles.length; i++){
            if (this.tiles[i].x == x && this.tiles[i].y == y){
                this.tiles.splice(i,1);
            }
        }
    }



}


//Tuile class :
class Tile extends GameObject{
    constructor(x,y,img,size=1){
        super(x,y,img,size);
    }
};
