import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def scatter_vis(x,y, name):
    sns.scatterplot(x,y)
    plt.savefig("./Result/scatter.png")
    return

def roc_vis(fpr, tpr):
    plt.plot(fpr, tpr,)
    plt.plot(np.arrange(0,1.05,0.05), np.arrange(0,1.05,0.05))
    plt.xlabel("FPR: False Positive Rate")
    plt.ylabel("TPR: True Positive Rate")
    plt.grid()
    plt.savefig("./Result/roc_curve.png")
    return