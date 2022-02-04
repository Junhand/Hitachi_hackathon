import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv

def data_info(df):
    #データ型・欠損値の確認
    with open("./Analysis_data/info.txt", "w") as f:
        df.info(buf=f)
    
    #基本統計量の確認
    df.describe(include='all').round(4).to_csv("./Analysis_data/describe.csv")
    with open("./Analysis_data/describe.csv", "a") as f:
        writer = csv.writer(f)
        var = np.append("分散", df.var().round(4).values)
        skew = np.append("歪度", df.skew().round(4).values)
        kurt = np.append("尖度",df.kurt().round(4).values)
        writer.writerow(var)
        writer.writerow(skew)
        writer.writerow(kurt)
        
    #相関関係の確認
    df.corr().round(4).to_csv("./Analysis_data/corr.csv")
    df_corr = df.corr()
    fig, ax = plt.subplots(figsize=(16, 16)) 
    sns.heatmap(df_corr, vmax=1, vmin=-1, center=0, annot=True, cmap="coolwarm")
    plt.savefig("./Analysis_data/corr.png")

    #ヒストグラムの確認
    fig, ax = plt.subplots(3,3, figsize=(16, 16))
    df.hist(ax=ax)
    fig.savefig("./Analysis_data/hist.png")

    #散布図の確認
    plt.clf()
    sns.pairplot(df, hue="y", kind="reg", diag_kind="hist")
    plt.savefig("./Analysis_data/pair.png")
    return