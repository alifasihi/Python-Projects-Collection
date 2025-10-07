from datetime import datetime
from dataclasses import dataclass

@dataclass
class Habit:
    name:str
    time_since:str
    remaining_days:str
    minutes_saves:float
    money_saved:str


def track_habit(name,start,cost,minutes_used):
    goal=60  #days
    hourly_wage=10 #dollars
    time_elapsed=(datetime.now()-start).total_seconds()


    hours=round(time_elapsed/60/60,1)
    days=round(hours/24,2)

    money_saved=cost*days
    minutes_used=round(days*minutes_used)
    total_money_saved=f'${round(money_saved +(minutes_used/60 * hourly_wage),2)}'


    days_to_go=round(goal - days)


    remaining_days='cleared!' if days_to_go <= 0 else f'{days_to_go}'
    time_since=f'{days}' if hours > 72 else f'{hours} hours'

    return Habit(
        name=name,
        time_since=time_since,
        remaining_days=remaining_days,
        minutes_saves=minutes_used,
        money_saved=total_money_saved,


    )
