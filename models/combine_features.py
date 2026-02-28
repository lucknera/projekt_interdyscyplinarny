import pandas as pd


def combine_features():
    mateusz_features = pd.read_csv("../features/mateusz-features.csv")
    olek_features = pd.read_csv("../features/olek-features.csv")
    combined = pd.merge(olek_features, mateusz_features, on="Area")
    return combined
