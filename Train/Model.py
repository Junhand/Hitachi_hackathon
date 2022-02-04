import imp
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression, LogisticRegression
import pandas as pd

def liner_stat(x, y):
    data_x = sm.add_constant(x)
    model = sm.OLS(y, data_x)
    result = model.fit()
    with open("./Result/result.txt", "w") as f:
        print(result.summary(),file=f)
    return model, result

def liner_reg(x, y):
    lr = LinearRegression()
    lr.fit(x,y)
    #print(lr.coef_)
    return lr

def logistic_reg(x, y):
    lr = LogisticRegression()
    lr.fit(x,y)
    print(pd.DataFrame(lr.conf_,columns=x.columns.values).T)
    return lr