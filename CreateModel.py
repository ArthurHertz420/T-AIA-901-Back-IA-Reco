import pandas as pd
import spacy

nlp = spacy.load("fr_core_news_sm")

# create_model
def create_model(path, sep, destination="DESTINATION", depart="DEPART", error="ERROR"):
    csv = pd.read_csv(path, sep=sep)
    model = []
    index = 0
    for expression in csv.EXPRESSION:
        tmp = {}
        tmp['entities'] = []

        if expression.find(csv[depart][index]) != -1:
            if (csv[error][index] == "FALSE" or csv[error][index] == "FAUX"):
                positionDestination = expression.find(csv[destination][index]), expression.find(csv[destination][index]) + len(
                    csv[destination][index]), 'destination'
                tmp['entities'].append(positionDestination)
            elif csv[depart][index] != "none":
                positionDepart = expression.find(csv[depart][index]), expression.find(csv[depart][index]) + len(
                    csv[depart][index]), "depart"
                tmp['entities'].append(positionDepart)

        cell = expression, tmp
        model.append(cell)
        index += 1
    return model

# create_pipeline
def nlp_with_entity_recognizer(train_data):
    nlp = spacy.blank('fr')
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)

    for _, annotations in train_data:
        # Here we are only interested in label to be added (depart, destination)
        for _s, _e, label in annotations.get('entities', []):
            ner.add_label(label)
    return nlp