from extractData import *
from createModel import *
from trainData import *
from findPath import *


def capitalize_string(string):
    # Split the string based on space delimiter
    list_string = string.split(' ')
    result_string = ""
    for s in list_string:
        result_string = result_string + ' ' + s.capitalize().strip()

    return result_string


# run main
data = extract_data("timetables.csv")
model = create_model("Jdd_Path.csv", ",")

nlp = nlp_with_entity_recognizer(model)
nlp = train_nlp(nlp, model)
while True:
    text = input("Enter your text: ")
    print(text)
    text = capitalize_string(text)

    destinations = get_destination(nlp, text)
    departs = get_depart(nlp, text)
    destination = destinations[0] if len(destinations) > 0 else ""
    depart = departs[0] if len(departs) > 0 else "Paris"
    if destination != "":
        find_path(data, depart, destination)
    else:
        print("Oups : Aucun trajet n'a pu être déterminé, veuillez entrer votre texte")
