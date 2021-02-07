#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Hesamaldin Firouznia
# Created Date: Saturday February 02 2021
# =============================================================================
"""The Module Has Been Build for record temperature value in a JSON file, to get min , max or mean of all of them"""

# =============================================================================
# Imports
# =============================================================================
import json


class TempTracker(object):
    """This is a class for recording temperature value, and return min, max or average of them.
    """

    def __init__(self, temperature=None):
        self.record_data = {}
        self.temperature = temperature
        self.json_file = open("my_json.json", "a")
        self.line_number = self.read_json()

    def insert(self, temperature):
        """Write input value in Json file.

        :type: temperature: int
        :param temperature: Amount of temperature value.
        :rtype: int
        :return:
        """
        # Raise error, if input value is not between 0 and 110.
        if not -1 < temperature < 111:
            print("Please put the value between 0 to 110")
            raise ValueError

        if self.line_number < 10:
            counter = '00'
        elif self.line_number < 100:
            counter = '0'
        else:
            counter = ''

        # Put new line in JSON file.
        self.json_file.write(str('{}"{}{}": "{}"{}'.format('{', counter, self.read_json(), temperature, '}')))
        self.json_file.write("\n")
        self.json_file.close()
        return self.json_file

    def get_max(self):
        """Get maximum of all the recorded temperature.

        :rtype: int
        :return: Maximum of all the recorded temperature.
        """
        super_dict = {}
        with open("my_json.json") as file:
            for line in file:
                super_dict.update(json.loads(line))
            maximum = min(super_dict, key=super_dict.get)
            return int(super_dict[maximum])

    def get_min(self):
        """Get minimum of all the recorded temperature.

        :rtype: int
        :return: Minimum of all the recorded temperature.
        """
        super_dict = {}
        with open("my_json.json") as file:
            for line in file:
                super_dict.update(json.loads(line))
            minimum = max(super_dict, key=super_dict.get)
            return int(super_dict[minimum])

    def get_mean(self):
        """Get average of all the temperature recorded.

        :rtype: float
        :return: Average of all the temperature recorded.
        """
        numbers = []
        super_dict = {}
        with open("my_json.json") as file:
            for line in file:
                super_dict.update(json.loads(line))
            for i in super_dict.values():
                numbers.append(int(i))
            numbers_sum = float(sum(numbers))
            return numbers_sum

    def read_json(self):
        """Return last line number of JSON.

        :rtype: int
        :return: Last line number of JSON.
        """
        with open("my_json.json", "r") as file:
            line_numbers = 0
            for _ in file:
                line_numbers += 1
            return line_numbers + 1

###########################
# tracker_01 = TempTracker()

# tracker_01.insert(48)
# print("Minimum is: {}".format(tracker_01.get_min()))
# print("Maximum is: {}".format(tracker_01.get_max()))
# print("Average is: {}".format(tracker_01.get_mean()))
