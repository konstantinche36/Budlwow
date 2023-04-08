from DataModel import *


def def_lunch_time_in_budlwow_time(budlwow_start_time: datetime.time, budlwow_finish_time: datetime.time, lunch_start_time: datetime.time, lunch_finish_time: datetime.time) -> int:
    res = 0
    if (budlwow_start_time <= lunch_start_time and budlwow_finish_time <= lunch_start_time) or (budlwow_start_time >= lunch_finish_time and budlwow_finish_time >= lunch_finish_time):
        res = budlwow_finish_time - budlwow_finish_time
    elif budlwow_start_time <= lunch_start_time and budlwow_finish_time <= lunch_finish_time:
        res = budlwow_finish_time - lunch_start_time
    elif budlwow_start_time <= lunch_start_time and budlwow_finish_time >= lunch_finish_time:
        res = lunch_finish_time - lunch_start_time
    elif budlwow_start_time >= lunch_start_time and budlwow_finish_time > lunch_finish_time:
        res = lunch_finish_time - budlwow_start_time
    return (res.seconds//60)/60
