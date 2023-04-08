from datetime import datetime, date, time
from typing import List
from collections import namedtuple
# 38247260004211759477522033956479266	03-АПР-2023 10:00	04-АПР-2023 16:00	№15
# 184891597963363647166294428360641643	03-АПР-2023 06:00	03-АПР-2023 13:30	№10
# 194022806080761641413949052449406597	03-АПР-2023 06:00	03-АПР-2023 13:00	№4
# 490701709251363276509867631068931393	03-АПР-2023 14:00	04-АПР-2023 13:15	№10
# 1058420796670952070934608929355800329	04-АПР-2023 02:00	04-АПР-2023 13:00	№4

# FIRST_DINNER_TIME = [datetime.strptime('13:00', '%H:%M').time(),datetime.strptime('14:00', '%H:%M').time()]
# SECOND_DINNER_TIME = [datetime.strptime('00:00', '%H:%M').time(),datetime.strptime('01:00', '%H:%M').time()]

LunchTime = namedtuple('LunchTime','start_date finish_date')
FIRST_LUNCH_TIME_T = LunchTime(datetime.strptime('13:00', '%H:%M').time(),datetime.strptime('14:00', '%H:%M').time())
SECOND_LUNCH_TIME_T = LunchTime(datetime.strptime('00:00', '%H:%M').time(),datetime.strptime('01:00', '%H:%M').time())

class Budlwow:
    def __init__(self, budlwow_id: int, start_date: datetime, finish_date: datetime, brigad_name: str, budlwow_hour: int) -> None:
        self.budlwow_id = budlwow_id
        self.start_date = start_date
        self.finish_date = finish_date
        self.brigad_name = brigad_name
        self.budlwow_hour = budlwow_hour

    def __str__(self) -> str:
        return f'budlwow_id {self.budlwow_id},\nstart_date {self.start_date},\nfinish_date {self.finish_date},\nbrigad_name {self.brigad_name},\nbudlwow_hour{self.budlwow_hour}'

def create_budlows():
    list_of_budlow = [
        Budlwow(38247260004211759477522033956479266, datetime.strptime('03-apr-2023 10:00',
                '%d-%b-%Y %H:%M'), datetime.strptime('03-apr-2023 12:00', '%d-%b-%Y %H:%M'), '#15', 2),
        Budlwow(38247260004211759477522033956479266, datetime.strptime('03-apr-2023 10:00',
                '%d-%b-%Y %H:%M'), datetime.strptime('04-apr-2023 16:00', '%d-%b-%Y %H:%M'), '#15', 10),
        Budlwow(184891597963363647166294428360641643, datetime.strptime('03-apr-2023 06:00',
                '%d-%b-%Y %H:%M'), datetime.strptime('03-apr-2023 13:30', '%d-%b-%Y %H:%M'), '#10', 7.5),
        Budlwow(194022806080761641413949052449406597, datetime.strptime('03-apr-2023 06:00',
                '%d-%b-%Y %H:%M'), datetime.strptime('03-apr-2023 13:00', '%d-%b-%Y %H:%M'), '#4', 7),
        Budlwow(490701709251363276509867631068931393, datetime.strptime('03-apr-2023 14:00',
                '%d-%b-%Y %H:%M'), datetime.strptime('04-apr-2023 13:15', '%d-%b-%Y %H:%M'), '#10', 16),
        Budlwow(1058420796670952070934608929355800329, datetime.strptime('04-apr-2023 02:00',
                '%d-%b-%Y %H:%M'), datetime.strptime('04-apr-2023 13:00', '%d-%b-%Y %H:%M'), '#4', 4),
    ]
    return list_of_budlow


def print_list_of_budlow(budlow_list):
    print(*budlow_list,
          sep='\n============================================================\n')
    
def get_budlow_info(budlow: Budlwow, spec_comm: str='Default info'):
    return f'{spec_comm} start_date = [{budlow.start_date}], finish_date = [{budlow.finish_date}]'