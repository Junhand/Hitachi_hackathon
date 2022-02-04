import matplotlib.pyplot as plt
import seaborn as sns

def visualize(df):
    #分布の確認
    column = "age"
    sns.displot(df[column], kde=True)
    plt.savefig("./Visualize_data/{0}_dis.png".format(column))

    #箱ひげ図の確認
    plt.clf()
    column = "age"
    sns.boxplot(x=column, data=df)
    plt.savefig("./Visualize_data/{0}_box.png".format(column))

    #関係散布図
    plt.clf()
    sns.scatterplot(x=column, y="y", data=df)
    plt.savefig("./Visualize_data/{0}_scatter.png".format(column))

    #回数の確認
    plt.clf()
    column="job"
    plt.figure(figsize=(16, 16))
    sns.countplot(x=column, hue="y", data=df)
    plt.xticks(rotation=90)
    plt.savefig("./Visualize_data/{0}_count.png".format(column))

    #バーの確認
    plt.clf()
    column="balance"
    plt.figure(figsize=(12, 12))
    sns.barplot(y=column, x="y", data=df)
    plt.savefig("./Visualize_data/{0}_bar.png".format(column))
    return

def hist(df, name):
    #ヒストグラムの確認
    plt.figure(figsize=(12, 12))
    sns.histplot(data=df, x="utc_timestamp")
    plt.savefig("./Analysis_data/hist{}.png".format(name))
