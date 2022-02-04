import pandas as pd

def load_data():
    df_ABC = pd.read_csv("./Data/ABC_forUser.csv")
    df_D = pd.read_csv("./Data/D_forUser.csv")
    return df_ABC, df_D

