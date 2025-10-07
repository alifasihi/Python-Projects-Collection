import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit


def main():
    habits=[
        track_habit('coffee',datetime(2025,10,7),cost=1,minutes_used=3),
        track_habit('cigarette',datetime(2021,12,25),cost=0.5,minutes_used=5)

    ]

    df=pd.DataFrame(habits)

    print(tabulate(df,headers='keys',tablefmt='pipe'))


if __name__=='__main__':
    main()
