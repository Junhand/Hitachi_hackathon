import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.metrics import auc, accuracy_score, roc_auc_score, roc_curve, classification_report, confusion_matrix
from Analysis.PredictionAnalysis import roc_vis

def evaluation(y, y_pred, y_pred_score):
    r2 = r2_score(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    fpr, tpr, threshold = roc_curve(y, y_pred_score)
    roc_vis(fpr, tpr)
    roc_auc = roc_auc_score(y,y_pred_score)
    accuracy = accuracy_score(y,y_pred)

    print("Liner Regressiion r2:",r2)
    print("Liner Regressiion mse:",mse)
    print("ROC AUC:",roc_auc)
    print("ROC AUC:",accuracy)
    return

    cm = confusion_matrix(Y_test, Pred)
    print(cm)
    print(classification_report(Y_test, Pred))

    #ヒートマップの作成
    class_names = ["died", "survived"]
    df = pd.DataFrame(cm, index=class_names, columns=class_names)
    sns.heatmap(df,annot=True,cbar=None,cmap="Blues")

    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.ylabel("True Class")
    plt.xlabel("Predicted Class")
    plt.gcf().set_size_inches(12, 12)
    plt.savefig('matrix.png')

