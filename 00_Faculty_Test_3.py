"""
Solve this problem in Python. Use comments in the code to clearly describe the steps and why each step is taken.
"""
import unittest
import numpy as np
import pandas as pd


def solution(files):
    """
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here
    """

    output_nested_list = []

    dataframes = {}

    for file in files:
        df = pd.read_csv(file)
        df["date"] = pd.to_datetime(df["date"])
        dataframes[file] = df

    for df_name in dataframes:
        cur_list = []
        # Get max volume df
        df = dataframes[df_name]
        df["year"] = df["date"].dt.year
        idx = df.groupby("year")["vol"].idxmax()
        max_vol_df = df.loc[idx, ["date", "vol"]]
        cur_list.append(max_vol_df)

        max_yearly_close = df.groupby('year')['close'].max()
        max_close_df = df[df.apply(lambda row: row['close'] == max_yearly_close[row['year']], axis=1)][['date', 'close']]
        cur_list.append(max_close_df)

        output_nested_list.append(cur_list)

    return output_nested_list


files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv", "./data/hoilled.csv",
         "./data/plent.csv", "./data/throwsh.csv", "./data/twerche.csv", "./data/veeme.csv"]

class TestExercise(unittest.TestCase):
    """
    example: example test
    one_triple: three elements
    simple1: simple tests
    simple2: simple tests
    small_random: random small, length=100
    medium_range: -1000, -999,...,1000, length 1000 = 999000000
    medium_random: length ~10000
    large_random: random large, length 100000
    large_range: 2000 * (-10..10) + [-1000, 500, -1] = 5000000
    extreme_large: (-2, .., -2, 1, .., 1) and (MAX_INT)...(MAX_INT), length ~100000
    """
    def test_example(self):
        self.assertEqual(solution(files=files), 60)

