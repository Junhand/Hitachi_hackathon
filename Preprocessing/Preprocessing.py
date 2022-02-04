import pandas as pd
def split_data(df):
   #説明変数
   exp_cols = ['id', 'age', 'job', 'marital', 'education', 'default', 'balance',
      'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign',
      'pdays', 'previous', 'poutcome']

   #目的変数
   target_col = ['y']

   data_x = df[exp_cols]
   data_y = df[target_col]

   return data_x, data_y


def preprocessing(df):
   #カラムの削除
   #drop_df = df.drop([],axis=1)

   #欠損値の削除
   comp_df = df.dropna(subset=["job","education"])

   #One-Hot Encoding
   dummies = pd.get_dummies(comp_df['job', 'marital', 'education', 'housing', 'loan'], drop_first=True)
   oneHot_df = pd.merge(comp_df.drop(['job', 'marital', 'education', 'housing', 'loan']), dummies)

   #利用するdf
   df = oneHot_df
   return df
  


