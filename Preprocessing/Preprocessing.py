import pandas as pd
def split_data(df_energy, df_weather):
   #説明変数
   exp_energy_cols = ['utc_timestamp', 'DE_KN_industrial1_grid_import', 'DE_KN_industrial1_pv_1', 'DE_KN_industrial1_pv_2',
      'DE_KN_industrial2_grid_import', 'DE_KN_industrial2_pv', 'DE_KN_industrial2_storage_charge', 'DE_KN_industrial2_storage_decharge',
      'DE_KN_industrial3_area_offices', 'DE_KN_industrial3_area_room_1', 'DE_KN_industrial3_area_room_2', 
      'DE_KN_industrial3_area_room_3', 'DE_KN_industrial3_area_room_4', 'DE_KN_industrial3_compressor', 'DE_KN_industrial3_cooling_aggregate', 
      'DE_KN_industrial3_cooling_pumps', 'DE_KN_industrial3_dishwasher', 'DE_KN_industrial3_ev', 'DE_KN_industrial3_grid_import',
      'DE_KN_industrial3_machine_1', 'DE_KN_industrial3_machine_2', 'DE_KN_industrial3_machine_3', 'DE_KN_industrial3_machine_4', 'DE_KN_industrial3_machine_5',
      'DE_KN_industrial3_pv_facade', 'DE_KN_industrial3_pv_roof', 'DE_KN_industrial3_refrigerator', 'DE_KN_industrial3_ventilation', 
      'DE_KN_public1_grid_import','DE_KN_public2_grid_import',
      'DE_KN_residential1_dishwasher', 'DE_KN_residential1_freezer', 'DE_KN_residential1_grid_import',
      'DE_KN_residential1_heat_pump', 'DE_KN_residential1_pv', 'DE_KN_residential1_washing_machine', 
      'DE_KN_residential2_circulation_pump', 'DE_KN_residential2_dishwasher', 'DE_KN_residential2_freezer', 
      'DE_KN_residential2_grid_import', 'DE_KN_residential2_washing_machine',
      'DE_KN_residential3_circulation_pump', 'DE_KN_residential3_dishwasher', 'DE_KN_residential3_freezer', 
      'DE_KN_residential3_grid_export', 'DE_KN_residential3_grid_import', 
      'DE_KN_residential3_pv', 'DE_KN_residential3_refrigerator', 'DE_KN_residential3_washing_machine',
      'DE_KN_residential4_dishwasher', 'DE_KN_residential4_ev', 'DE_KN_residential4_freezer', 
      'DE_KN_residential4_grid_export', 'DE_KN_residential4_grid_import', 'DE_KN_residential4_heat_pump',
      'DE_KN_residential4_pv', 'DE_KN_residential4_refrigerator', 'DE_KN_residential4_washing_machine', 
      'DE_KN_residential5_dishwasher', 'DE_KN_residential5_grid_import', 'DE_KN_residential5_refrigerator', 'DE_KN_residential5_washing_machine', 
      'DE_KN_residential6_circulation_pump', 'DE_KN_residential6_dishwasher', 'DE_KN_residential6_freezer', 'DE_KN_residential6_grid_export',
      'DE_KN_residential6_grid_import', 'DE_KN_residential6_pv', 'DE_KN_residential6_washing_machine',
      'DE_load_actual_entsoe_transparency', 'DE_load_forecast_entsoe_transparency', 'DE_solar_capacity',
      'DE_solar_generation_actual', 'DE_solar_profile', 'DE_wind_capacity', 'DE_wind_generation_actual', 'DE_wind_profile',
      'DE_wind_offshore_capacity', 'DE_wind_offshore_generation_actual', 'DE_wind_offshore_profile', 
      'DE_wind_onshore_capacity', 'DE_wind_onshore_generation_actual', 'DE_wind_onshore_profile',
      'DE_temperature', 'wether_date']
   
   exp_weather_col = ['utc_timestamp', 'P0', 'V_N', 'V_TE002', 'F', 'D', 'FX_911', 'R1',
       'SD_SO', 'TT_TU', 'RF_TU', 'whether_date']

   #目的変数
   target_energy_col = ['utc_timestamp', 'P0', 'V_N', 'V_TE002', 'F', 'D', 'FX_911', 'R1',
       'SD_SO', 'TT_TU', 'RF_TU', 'whether_date']

   target_weather_col = ['utc_timestamp', 'P0', 'V_N', 'V_TE002', 'F', 'D', 'FX_911', 'R1',
       'SD_SO', 'TT_TU', 'RF_TU', 'whether_date']

   df_energy_x = df_energy[exp_energy_cols]
   df_energy_y = df_energy[target_energy_col]

   df_weather_x = df_weather[exp_weather_col]
   df_weather_y = df_weather[target_weather_col]

   return df_energy_x, df_energy_y, df_weather_x, df_weather_y 


def preprocessing(df_energy, df_weather):
   df_energy[df_energy['name'].str.contains('li')]
   df_weather
   #カラムの削除
   #drop_df = df.drop([],axis=1)

   #欠損値の削除
   #comp_df = df.dropna(subset=["job","education"])

   #One-Hot Encoding
   #dummies = pd.get_dummies(comp_df['job', 'marital', 'education', 'housing', 'loan'], drop_first=True)
   #oneHot_df = pd.merge(comp_df.drop(['job', 'marital', 'education', 'housing', 'loan']), dummies)

   #利用するdf
   #df = oneHot_df
   return df
  


