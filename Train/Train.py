from Train.Model import liner_stat, liner_reg, logistic_reg


def train(x, y):
    models = []
    #ls_model, result = liner_stat(x, y)
    #lr_model = liner_reg(x,y)
    lo_model = logistic_reg(x,y)
    models.add(lo_model)


    #Prediction
    #liner_reg_pred(lr_model,x,y)
    #logistic_reg_pred(lo_model,x,y)
    
    return models