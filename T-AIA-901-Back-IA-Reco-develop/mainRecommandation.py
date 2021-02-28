from flask import Flask
from flask import request

from CreateModel import *
from ExtractData import *
from TrainData import *
from findPath import *

app = Flask(__name__)
data = extract_data("timetables.csv")
model = create_model("Jdd_Path.csv", ",")
nlp = nlp_with_entity_recognizer(model)
nlp = train_nlp(nlp, model)


@app.route('/')
def index():
    return "CE N'EST PAS LA BONNE ROUTE BOLOSSE"


@app.route('/recommender', methods=['POST'])
def recommanderapi():
    dataRequest = request.get_json(force=True)
    text = capitalize_string(dataRequest.get('textToRecommande'))
    destinations = get_destination(nlp, text)
    departs = get_depart(nlp, text)
    destination = destinations[0] if len(destinations) > 0 else ""
    depart = departs[0] if len(departs) > 0 else "Paris"
    if destination != "":
        string = ' '
        string = string.join(find_path(data, depart, destination))
        return string, 200
    else:
        return "Oups : Aucun trajet n'a pu être déterminé, veuillez entrer votre texte", 400


def capitalize_string(string):
    # Split the string based on space delimiter
    list_string = string.split(' ')
    result_string = ""
    for s in list_string:
        result_string = result_string + ' ' + s.capitalize().strip()

    return result_string


if __name__ == '__main__':
    app.run(debug=True)


