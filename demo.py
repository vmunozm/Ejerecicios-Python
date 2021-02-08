import requests
import json 
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
app = Flask(__name__)

@app.route("/directorio")
def server_info():
 
 idpok = request.args.get("id")
 url="https://pokeapi.co/api/v2/pokemon/"+idpok  
 
 headers={}
 response=requests.request("GET",url,headers=headers)
 #estoy trayendo el nombre del pokemon:
 json_object=json.loads(str((response.text)))
 name = json_object["name"]
 print(name)
 #tarea traer imagen: "dream_world": {
 #    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/1.svg",
 var2={"nombre_pokemon": name, "url_pokemon": "pendiente"}
 #return(name)
 return(var2)
 
if __name__=="__main__":
    app.run()


