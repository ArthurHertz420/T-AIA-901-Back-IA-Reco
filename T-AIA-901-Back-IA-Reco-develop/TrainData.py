import random


# train data
def train_nlp(nlp, model):
    n_iter = 16
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        # Start training here
        # optimizer function to update the model's weights.
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            # At each iteration, the training data is shuffled to ensure the model
            # doesn't make any generalisations based on the je order of examples
            random.shuffle(model)
            losses = {}
            for text, annotations in model:
                # "drop" is to improve the learning results, rate at which to randomly
                # "drop" individual features and representations, making the model to
                # memorise the training data
                # sgd = Stochastic Gradient Descent
                nlp.update([text], [annotations], sgd=optimizer, drop=0.35, losses=losses)
            print('losses -', losses)
    return nlp


def get_destination(nlp, text):
    doc = nlp(text)
    return [word.text for word in doc.ents if word.label_ == "destination"]


def get_depart(nlp, text):
    doc = nlp(text)
    return [word.text for word in doc.ents if word.label_ == "depart"]
