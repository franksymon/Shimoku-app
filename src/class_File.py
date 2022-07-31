from itertools import groupby

import pandas as pd


class OpenFile:
    @classmethod
    def open_file_csv(cls, root_path: str) -> pd.DataFrame:
        csv = pd.read_csv(root_path)
        df = pd.DataFrame(csv)
        return df


class ProccesFile:
    def bar_chart_data(
        self,
        df: pd.DataFrame,
        x_serie_df: str,
        y_serie_df: list[int],
        bar_serie_df: str,
    ) -> list[dict]:

        data_frame = df.groupby([f"{x_serie_df}", f"{bar_serie_df}"])[
            f"{y_serie_df}"
        ].sum()

        lis_data = []
        lis = []
        for i in data_frame.items():
            obj = {"name": i[0][0], f"{i[0][1]}": i[1]}
            lis.append(obj)
            pass

        def order(list: list[dict]):
            obj = {}
            for i in list:
                obj.update(i)
            return obj

        lis.sort(key=lambda x: x["name"])
        for k, sl in groupby(lis, key=lambda x: x["name"]):
            data = order(sl)
            lis_data.append(data)
        return lis_data

    def chart_pie_data(self, df: pd.DataFrame, serie_df: str) -> list[dict]:

        value = df[f"{serie_df}"].value_counts()
        data = []
        for i in value.items():
            obj = {"name": f"{i[0]} {int(i[1])//10}%", "value": i[1]}
            data.append(obj)
        return data

    @classmethod
    def df_store(cls, df: pd.DataFrame):
        df_store = df.sort_values(by=["Date"]).copy()
        df_store["yyyy"] = pd.to_datetime(df_store["Date"]).dt.year
        df_store["mm"] = pd.to_datetime(df_store["Date"]).dt.month
        df_store["date_mon"] = (
            df_store["yyyy"].astype(str) + "-" + df_store["mm"].astype(str)
        )
        df_store["day"] = pd.to_datetime(df_store["Date"]).dt.day_name()
        df_store["hour"] = pd.to_datetime(df_store["Time"]).dt.hour
        df_store["month"] = df_store["mm"].apply(
            lambda x: "January" if x == 1 else ("February" if x == 2 else "March")
        )
        return df_store
