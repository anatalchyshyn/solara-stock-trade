import solara
import pandas as pd
import solara.express as solara_px
import solara.lab
from typing import Optional, cast
import os

class Stock:
    info = solara.reactive("")
    text = solara.reactive("")
    tick_df = solara.reactive(cast(Optional[pd.DataFrame], None))
    
    period = solara.reactive("1y")
    bb_box = solara.reactive(True)
    rsi_box = solara.reactive(True)
    macd_box = solara.reactive(True)
    adx_box = solara.reactive(True)
    
    wrong_ticker = solara.reactive(False)
    
    @staticmethod
    def stock_init():
        Stock.info = solara.reactive("")
        Stock.text = solara.reactive("")
        Stock.tick_df = solara.reactive(cast(Optional[pd.DataFrame], None))

        Stock.period = solara.reactive("1y")
        Stock.bb_box = solara.reactive(True)
        Stock.rsi_box = solara.reactive(True)
        Stock.macd_box = solara.reactive(True)
        Stock.adx_box = solara.reactive(True)

        Stock.wrong_ticker = solara.reactive(False)
    
    def slice_period(tick_df_full):
        if Stock.period.value == '1y':
            tick_df = tick_df_full.iloc[-252:]
        elif Stock.period.value == '6m':
            tick_df = tick_df_full.iloc[-126:]
        elif Stock.period.value == '3m':
            tick_df = tick_df_full.iloc[-63:]
        elif Stock.period.value == "1m":
            tick_df = tick_df_full.iloc[-21:]
        elif Stock.period.value == '1w':
            tick_df = tick_df_full.iloc[-6:]
            
        return tick_df

    @staticmethod
    def show_graph(): 
        try:
            frame = pd.read_csv("indicators/" + str(Stock.text.value) + ".csv")     
            Stock.tick_df.value = frame
            Stock.wrong_ticker.value = False
        except:
            Stock.wrong_ticker.value = True

        info_path = 'info/' + str(Stock.text.value) + '.json'
        
        if os.path.exists(info_path):

            ticker_info = pd.read_json(info_path)
            Stock.info.value = """
             **Name:** {}\n
             **Sector:** {}\n
             **Industry:** {}\n
             **Description:** {}\n
             **Trailing PE:** {}\n
             **Forward PE:** {}\n
             **PEG Ratio:** {}\n
            """.format(ticker_info['longName'][0], ticker_info['sector'][0], ticker_info['industry'][0], ticker_info['longBusinessSummary'][0], ticker_info['trailingPE'][0], ticker_info['forwardPE'][0],ticker_info['pegRatio'][0])
        
        else:
           
            data = YFinance3(Stock.text.value)
            with open(info_path, 'w') as file:
                json.dump(data.info, file)

            ticker_info = pd.read_json(info_path)
            Stock.info.value = """
             **Name:** {}\n
             **Sector:** {}\n
             **Industry:** {}\n
             **Description:** {}\n
             **Trailing PE:** {}\n
             **Forward PE:** {}\n
             **PEG Ratio:** {}\n
            """.format(ticker_info['longName'][0], ticker_info['sector'][0], ticker_info['industry'][0], ticker_info['longBusinessSummary'][0], ticker_info['trailingPE'][0], ticker_info['forwardPE'][0],ticker_info['pegRatio'][0])
            
    @solara.component
    def stock_menu():
        
        solara.Markdown("**Tickers graph**")
        with solara.Columns([1, 1, 2, 1, 1, 1, 7]):

            solara.InputText("Ticker", value=Stock.text)
            solara.Select(label="Period", value=Stock.period, values=["1y", "6m", "3m", "1m", "1w"])
            solara.Checkbox(label="Bollinger Bands", value=Stock.bb_box)
            solara.Checkbox(label="RSI", value=Stock.rsi_box)
            solara.Checkbox(label="MACD", value=Stock.macd_box)
            solara.Checkbox(label="ADX", value=Stock.adx_box)

            solara.Button("Show", outlined=False, on_click=Stock.show_graph, color="primary")
