import pandas as pd

class Dataframe:
    def __init__(self, dataframe):
        self.df = dataframe
        pass

    def df_shape(self):
        return f'The dataframe has {self.df.shape[0]} rows and {self.df.shape[1]} columns'

    def display_ten_rows(self):
        return self.df.head(10)

    def display_cols_with_null_per_cent(self):
        dict_per_cent = {}
        for col in self.df.columns:
            dict_per_cent[col] = round((self.df[col].isnull().sum() / self.df.shape[0]) * 100, 1)
        df = pd.DataFrame(list(dict_per_cent.items()),columns = ['df_column','per_cent_null(%)']).sort_values(by='per_cent_null(%)', ascending=False) 
        return df