import solara
import pandas as pd
import solara.express as solara_px
import solara.lab
from typing import Optional, cast

class Fund:
    df = solara.reactive(None)
    df_full = solara.reactive(None)
    mean_value = solara.reactive(None)
    fund_value = solara.reactive("MyFund")  
    rsi_range = solara.reactive((0, 100))
    adx_range = solara.reactive((0, 100))
    adx_up = solara.reactive(False)
    macd_range = solara.reactive("None")
    close_ema = solara.reactive("None")
    close_bb = solara.reactive("None")    

    @staticmethod
    def fund_init():
        Fund.df = solara.reactive(None)
        Fund.df_full = solara.reactive(None)
        Fund.mean_value = solara.reactive(None)
        Fund.fund_value = solara.reactive("MyFund")  
        Fund.rsi_range = solara.reactive((0, 100))
        Fund.adx_range = solara.reactive((0, 100))
        Fund.adx_up = solara.reactive(False)
        Fund.macd_range = solara.reactive("None")
        Fund.close_ema = solara.reactive("None")
        Fund.close_bb = solara.reactive("None")    
    
    @staticmethod
    def load_fund_values():
        
        df = pd.read_csv("funds/" + str(Fund.fund_value.value) + ".csv")
        df = df.round(2)
        df = df[(df["RSI_14"]>=Fund.rsi_range.value[0]) & (df["RSI_14"]<=Fund.rsi_range.value[1]) &
               (df["ADX_14"]>=Fund.adx_range.value[0]) & (df["ADX_14"]<=Fund.adx_range.value[1])]
        
        if Fund.adx_up.value:
            df = df[(df['adx_slope'] > 0)]
        
        if Fund.macd_range.value != 'None':
            df = df[(df['macd_status'] == Fund.macd_range.value)]

        if Fund.close_ema.value != 'None':
            df = df[(df['sma_status'] == Fund.close_ema.value)]
                
        
        if Fund.close_bb.value != 'None': 
            df = df[(df['bb_status'] == Fund.close_bb.value)]
        
        sectors = pd.read_json("sectors_2_14.json")
        df = pd.merge(df, sectors, on='Symbol', how='left')
        
        Fund.df_full.value = df

        df = df[["Symbol", "Name", "Sector", "RSI_14", "rsi_slope", "SMA_20", "EMA_50", "ADX_14", "DMP_14", "DMN_14", "adx_slope", "52_weeks", "Day", "Week", "Month", "Close"]]
        
        df_sliced = df[['Sector', 'Day', 'Week', 'Month']]
        grouped = df_sliced.groupby('Sector')
        mean_value = grouped.mean()
        
        Fund.df.value = df
        Fund.mean_value.value = mean_value
        
        
    @staticmethod
    def on_action_column_high(column):
        df = Fund.df.value
        df = df.sort_values(by=[column], ascending=False)
        Fund.df.value = df

    @staticmethod
    def on_action_column_low(column):
        df = Fund.df.value
        df = df.sort_values(by=[column], ascending=True)
        Fund.df.value = df
