from flask import Flask, request, jsonify
from http import HTTPStatus

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Doro Wot',
        'description': "lorem ipsum dolor sit amet, consectetur adipiscing elit"
    },
    {
        'id': 2,
        'name': 'Ye Beg Tibs',
        'description': "lorem ipsum dolor sit amet, consectetur adipiscing elit"
    }
]

@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify({'data': recipes}), HTTPStatus.FOUND


@app.route("/recipes/<int:recipe_id>", methods=['GET'])
def get_recipe(recipe_id):
    recipe = next(
        (recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if recipe:
        return jsonify(recipe), HTTPStatus.FOUND
    else:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

@app.route("/recipes", methods=["POST"])
def create_recipe():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    id = len(recipes) + 1

    recipe={
        'name':name,
        'description':description,
        'id':id
    }
    recipes.append(recipe)
    return jsonify(recipe), HTTPStatus.CREATED

@app.route("/recipes/<int:recipe_id>", methods=["PUT"])
def update_recipe(recipe_id):
    recipe = next(
       (recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
    data=request.get_json()
    name = data.get('name')
    description = data.get('description')
    recipe.update({
        'name':name,
        'description':description
    })
    return jsonify(recipe), HTTPStatus.OK

@app.route("/recipes/<int:recipe_id>", methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = next(
        (recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if not recipe:
        return jsonify({'message':'recipe not found'}), HTTPStatus.NOT_FOUND
    else:
        recipes.remove(recipe)
        return jsonify(recipe),HTTPStatus.NO_CONTENT
    return

if __name__ == '__main__':
    app.run(debug=True)
