from flask import (Blueprint, request, redirect)
from . import models

bp = Blueprint("animal", __name__, url_prefix="/animals")

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        common_name = request.form["common_name"]
        scientific_name = request.form["scientific_name"]
        conservation_status = request.form["conservation_status"]
        native_habitat = request.form["native_habitat"]
        fun_fact = request.form["fun_fact"]

        new_animal = models.Animal(common_name=common_name, scientific_name=scientific_name, conservation_status=conservation_status, native_habitat=native_habitat, fun_fact=fun_fact)

        models.db.session.add(new_animal)
        models.db.session.commit()

        return redirect("/animals")
    
    animals_dict = {
        "animals": [],
    }
    animals = models.Animal.query.all()
    if len(animals) > 0:
        for animal in animals:
            dict = {"common_name": animal.common_name, "scientific_name": animal.scientific_name, "conservation_status": animal.conservation_status, "native_habitat": animal.native_habitat, "fun_fact": animal.fun_fact}
            animals_dict["animals"].append(dict)
    else:
        animals_dict = {"message": "No animals registered!"}

    return animals_dict

@bp.route("/<int:id>")
def show(id):
    animal = models.Animal.query.get(id)
    if not animal:
        animal_dict = {"message": "No animal found!"}
    else:
        animal_dict = {
            "common_name": animal.common_name,
            "scientific_name": animal.scientific_name,
            "conservation_status": animal.conservation_status,
            "native_habitat": animal.native_habitat,
            "fun_fact": animal.fun_fact
        }

    return animal_dict