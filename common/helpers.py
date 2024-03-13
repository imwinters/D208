import pandas as pd
import math

class Helpers:

    @staticmethod
    def one_hot_encode(df: pd.DataFrame, column:str) -> pd.DataFrame:
        """
        This transforms a categorical variable to a dataframe of bit values, then merges that with the starting dataframe.
        Dropping the original column, leaving the bit columns.
        Use with caution: can have significant impact on dimensions of dataframe.
        """
        # Join the encoded df
        dummies = pd.get_dummies(df[column])
        dropped = df.drop(column, axis=1)
        return pd.concat([dropped, dummies], axis=1)


    @staticmethod
    def transform_yes_no_to_bit(value:str) -> int:
        """
        Transforms yes or no cells to 1 hot encoded.
        """
        try:
            if value.lower() == "yes":
                return 1
            return 0
        except Exception as ex:
            if math.isnan(value):
                return value
            return value

