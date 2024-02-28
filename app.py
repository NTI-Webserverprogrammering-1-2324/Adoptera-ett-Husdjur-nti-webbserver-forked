from flask import Flask
from helper import pets

app = Flask(__name__)



@app.route('/')
def index():
  return '''<h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p><ul>
  <li>
  <a href="/animals/dogs"</a>Dogs</li>
  <li>
  <a href="/animals/cats"</a>Cats</li>
  <li>
  <a href="/animals/rabbits"</a>Rabbits</li>
</ul>                                  
  '''


@app.route('/animals/<pet_type>')
def animals(pet_type):
  pet_list = pets.get(pet_type, [])
  html = f'<h1>List of {pet_type}</h1><ul>'
  for pet_id, pet in enumerate(pet_list):
    html += f'<li><a href="/animals/{pet_type}/{pet_id}">{pet["name"]}</a></li>'
  html += '</ul>'
  return html


@app.route('/animals/<pet_type>/<int:pet_id>/')
def pet(pet_type, pet_id):
  pet_list = pets.get(pet_type, [])
  if pet_id < 0 or pet_id >= len(pet_list):
    return 'Pet not found', 404

  pet = pet_list[pet_id]
  return f'''
   <h1>{pet["name"]}</h1>
   <img src="{pet["url"]} alt="{pet["name"]}">
   <p>{pet["description"]}</p>
   <ul> 
        <li>Breed: {pet["breed"]}</li>
        <li>Age: {pet["age"]}</li>
   </ul>
'''


if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")

