import pandas as pd


def combine_features():
    mateusz_features = pd.read_csv("../features/mateusz-features.csv")
    olek_features = pd.read_csv("../features/olek-features.csv")
    combined = pd.merge(olek_features, mateusz_features, on="Area")
    return combined


def read_data(path):
    data = pd.read_csv(path)
    df = pd.merge(data, combine_features(), on="ID")
    df = df.drop(
        columns=["start_date", "end_date", "horizon_lower", "horizon_upper", "Country", "electrical_conductivity"],
        errors="ignore"
    )
    target_cols = [
        "Al",
        "B",
        "Ca",
        "C_organic",
        "C_total",
        "Cu",
        "Fe",
        "Mg",
        "Mn",
        "N",
        "P",
        "K",
        "Na",
        "S",
        "Zn",
    ]
    other_cols = [col for col in df.columns if col not in target_cols]
    new_columns = other_cols + target_cols
    df = df[new_columns]
    return df
