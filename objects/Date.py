#!/usr/bin/env python3

from modules.dateomatic import dateomatic
from .Transformable import Transformable


class Date(Transformable):

    def __init__(self, day=1, month=1, year=1):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 0:
            raise ValueError
        self.day = day
        self.month = month
        self.year = year
        self.months_dictionary = dateomatic.default_months_dictionary
        self.schemas_list = dateomatic.default_schemas_list
        self.separators = dateomatic.default_separators

    def set_months_dictionary(self, dictionary):
        self.months_dictionary = dictionary

    def set_schemas_list(self, schemas_list):
        self.schemas_list = schemas_list

    def set_separators(self, separators):
        self.separators = separators

    def get_transformations(self):
        yield from dateomatic.dateomatic(day=self.day, month=self.month, year=self.year,
                                         months_dictionary=self.months_dictionary,
                                         schemas_list=self.schemas_list,
                                         separators=self.separators)

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year
