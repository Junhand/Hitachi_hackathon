from Preprocessing.LoadData import load_data
from Preprocessing.Preprocessing import preprocessing, split_data
from Train.Train import train
from Train.Evaluation import evaluation
from Analysis.StatisticAnalysis import data_info
from Analysis.Visualize import visualize
from Analysis.PredictionAnalysis import scatter_vis
from sklearn.model_selection import train_test_split
import pandas_profiling as pdp

if __name__ == '__main__':
    df_energy, df_weather = load_data()
    print(df_energy.shape, df_weather.shape)
    print(df_energy.columns, df_weather.columns)

    #df_energy2, df_weather2 = preprocessing(df_energy, df_weather)
    
    profile = pdp.ProfileReport(df_energy)
    profile.to_file("./Analysis_data/analysis_energy1.html")
    profile = pdp.ProfileReport(df_weather)
    profile.to_file("./Analysis_data/analysis_weather1.html")
    '''
    #data_info(data)
    visualize(data)
    

    data_x, data_y = split_data(fixed_data)
    X_train, X_test, Y_train, Y_test = train_test_split(data_x, data_y, test_size=0.2,random_state=42)
    X_val, X_test, Y_val, Y_test = train_test_split(X_test, Y_test, test_size=0.5,random_state=42)
    
    models = train(data_x, data_y)
    for model in models:
        y_pred_score = model.predict_proba(X_test)[:,1]
        y_pred = model.predict(X_test)
        #y_pred = np.where(y_pred > 0.5, 1, 0)
        
        evaluation(Y_test, y_pred, y_pred_score)
        #scatter_vis(Y_test.values.flatten(), y_pred.flatten(), "Liner_Reg")
        

    #print(data.head(10))
    '''