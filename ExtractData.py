import pandas as pd


# extract_data
def extract_data(file):
    csv = pd.read_csv(file, delimiter="\t", header='infer')
    new = csv["trajet"].str.split(" - ", n=1, expand=True)
    csv["start"] = new[0].str.strip()
    csv["destination"] = new[1].str.strip()
    csv.drop(columns=["trajet"], inplace=True)
    return csv
