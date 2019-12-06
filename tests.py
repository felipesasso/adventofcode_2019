import unittest

from utils import get_int_list_from_file
from day1 import (
get_rocket_fuel_requirements,
get_total_fuel_requirements,
get_total_fuel_requirements_from_file,
get_total_fuel_fuel_requirements_from_file,
get_total_fuel_fuel_requirements,
get_fuel_fuel_requirements)

from day2 import restore_gravity_assist_program, find_noun_verb

class DayOneTest(unittest.TestCase):

    def test_day_one_1(self):
        filename = 'day1_input.txt'
        result = get_total_fuel_requirements_from_file(filename)
        self.assertEqual(result, 3327415)

    def test_day_one_2(self):
        masses = (12, 14, 1969, 100756)
        results = (2, 2, 654, 33583)
        for mass, result in zip(masses, results):
            self.assertEqual(result, get_rocket_fuel_requirements(mass))

    def test_day_one_3(self):
        filename = 'day1_input.txt'
        mass_list = get_int_list_from_file(filename)
        result = get_total_fuel_requirements(mass_list)
        self.assertEqual(result, 3327415)

    def test_day_one_4(self):
        masses = (14, 1969, 100756)
        results = (2, 966, 50346)
        for mass, result in zip(masses, results):
            self.assertEqual(result, get_fuel_fuel_requirements(mass))

    def test_day_one_5(self):
        filename = 'day1_input.txt'
        result = get_total_fuel_fuel_requirements_from_file(filename)
        self.assertEqual(result, 4988257)

    def test_day_one_5(self):
        filename = 'day1_input.txt'
        mass_list = get_int_list_from_file(filename)
        result = get_total_fuel_fuel_requirements(mass_list)
        self.assertEqual(result, 4988257)

class DayTwoTest(unittest.TestCase):
    def test_day_two_1(self):
        codes_list = get_int_list_from_file(filename='day2_input.txt', sep=',')
        result = restore_gravity_assist_program(12, 2, codes_list)
        self.assertEqual(result, 6730673)

    def test_day_two_2(self):
        codes_list = get_int_list_from_file(filename='day2_input.txt', sep=',')
        result = find_noun_verb(codes_list, 19690720)
        self.assertEqual(result, (37, 49))



if __name__ == "__main__":
     unittest.main()
