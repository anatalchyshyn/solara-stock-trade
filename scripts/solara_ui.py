import solara
import pandas as pd
import solara.express as solara_px
import solara.lab
from typing import Optional, cast


@solara.component
def win_and_los_ui(df):
    with solara.lab.Tabs():
        with solara.lab.Tab("Winners", icon_name="mdi-cat"):
            with solara.lab.Tabs():

                with solara.lab.Tab("day", icon_name="mdi-calendar-today"):
                    with solara.Card():
                        df_week = df.sort_values(by='Day')
                        df_week = df_week[['Symbol', 'Day']]
                        df_week = df_week.iloc[-10:]
                        df_week = df_week.iloc[::-1]
                        dataframe = solara.DataFrame(df_week, items_per_page=20)

                with solara.lab.Tab("week", icon_name="mdi-calendar-week"):
                    with solara.Card():
                        df_week = df.sort_values(by='Week')
                        df_week = df_week[['Symbol', 'Week']]
                        df_week = df_week.iloc[-10:]
                        df_week = df_week.iloc[::-1]
                        dataframe = solara.DataFrame(df_week, items_per_page=20)

                with solara.lab.Tab("month", icon_name="mdi-calendar-month"):
                    with solara.Card():
                        df_week = df.sort_values(by='Month')
                        df_week = df_week[['Symbol', 'Month']]
                        df_week = df_week.iloc[-10:]
                        df_week = df_week.iloc[::-1]
                        dataframe = solara.DataFrame(df_week, items_per_page=20)

        with solara.lab.Tab("Lossers", icon_name="mdi-dog-side"):
            with solara.lab.Tabs():

                with solara.lab.Tab("day", icon_name="mdi-calendar-today"):
                    with solara.Card():
                        df_week = df.sort_values(by='Day')
                        df_week = df_week[['Symbol', 'Day']]
                        df_week = df_week.iloc[:10]
                        df_week = df_week.iloc[::-1]
                        dataframe = solara.DataFrame(df_week, items_per_page=20)

                with solara.lab.Tab("week", icon_name="mdi-calendar-week"):
                    with solara.Card():
                        df_week = df.sort_values(by='Week')
                        df_week = df_week[['Symbol', 'Week']]
                        df_week = df_week.iloc[:10]
                        df_week = df_week.iloc[::-1]
                        dataframe = solara.DataFrame(df_week, items_per_page=20)

                with solara.lab.Tab("month", icon_name="mdi-calendar-month"):
                    with solara.Card():
                        df_week = df.sort_values(by='Month')
                        df_week = df_week[['Symbol', 'Month']]
                        df_week = df_week.iloc[:10]
                        df_week = df_week.iloc[::-1]
                        dataframe = solara.DataFrame(df_week, items_per_page=20)
