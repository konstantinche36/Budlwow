import unittest
from DataView import def_lunch_time_in_budlwow_time
from DataModel import *


class TestRemoveBudlowLunchTime(unittest.TestCase):

    def test_budlow_time_less_lunch_time(self):
        budlow_start_time = datetime.strptime('10:00', '%H:%M')
        budlow_finish_time = datetime.strptime('12:00', '%H:%M')
        lunch_start_time = datetime.strptime('13:00', '%H:%M')
        lunch_finish_time = datetime.strptime('14:00', '%H:%M')
        self.assertEqual(def_lunch_time_in_budlwow_time(
            budlow_start_time, budlow_finish_time, lunch_start_time, lunch_finish_time), 0)

    def test_budlow_time_finish_time_in_lunch_time(self):
        budlow_start_time = datetime.strptime('10:00', '%H:%M')
        budlow_finish_time = datetime.strptime('13:30', '%H:%M')
        lunch_start_time = datetime.strptime('13:00', '%H:%M')
        lunch_finish_time = datetime.strptime('14:00', '%H:%M')
        self.assertEqual(def_lunch_time_in_budlwow_time(
            budlow_start_time, budlow_finish_time, lunch_start_time, lunch_finish_time), 0.5)

    def test_budlow_time_start_time_in_lunch_time(self):
        budlow_start_time = datetime.strptime('13:30', '%H:%M')
        budlow_finish_time = datetime.strptime('15:00', '%H:%M')
        lunch_start_time = datetime.strptime('13:00', '%H:%M')
        lunch_finish_time = datetime.strptime('14:00', '%H:%M')
        self.assertEqual(def_lunch_time_in_budlwow_time(
            budlow_start_time, budlow_finish_time, lunch_start_time, lunch_finish_time), 0.5)

    def test_budlow_time_cover_lunch_time(self):
        budlow_start_time = datetime.strptime('12:30', '%H:%M')
        budlow_finish_time = datetime.strptime('15:30', '%H:%M')
        lunch_start_time = datetime.strptime('13:00', '%H:%M')
        lunch_finish_time = datetime.strptime('14:00', '%H:%M')
        self.assertEqual(def_lunch_time_in_budlwow_time(
            budlow_start_time, budlow_finish_time, lunch_start_time, lunch_finish_time), 1.0)

    def test_budlow_time_start_time_less_lunch_time(self):
        budlow_start_time = datetime.strptime('14:30', '%H:%M')
        budlow_finish_time = datetime.strptime('15:30', '%H:%M')
        lunch_start_time = datetime.strptime('13:00', '%H:%M')
        lunch_finish_time = datetime.strptime('14:00', '%H:%M')
        self.assertEqual(def_lunch_time_in_budlwow_time(
            budlow_start_time, budlow_finish_time, lunch_start_time, lunch_finish_time), 0.0)
        
    def test_budlow_time_start_time_less_lunch_time(self):
        budlow_start_time = datetime.strptime('00:00', '%H:%M')
        budlow_finish_time = datetime.strptime('06:00', '%H:%M')
        lunch_start_time = datetime.strptime('00:00', '%H:%M')
        lunch_finish_time = datetime.strptime('01:00', '%H:%M')
        self.assertEqual(def_lunch_time_in_budlwow_time(
            budlow_start_time, budlow_finish_time, lunch_start_time, lunch_finish_time), 1.0)


if __name__ == '__main__':
    unittest.main()
