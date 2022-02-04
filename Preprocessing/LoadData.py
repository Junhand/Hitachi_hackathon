import pandas as pd

def load_data():
    excel_data = pd.read_excel("./Data/boston_housing.xlsx")
    csv_data = pd.read_csv("./Data/train.csv")
    return csv_data

