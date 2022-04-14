#!/usr/bin/env python
# encoding: utf-8

import json


class JSONTable():
    def __init__(self, filename: str):
        assert filename.endswith(".json"), "path to file must ends .json"

        self.data = None
        self.filename = filename
        self.read_file()

    def set_filename(self, filename: str, with_reading=True):
        self.filename = filename
        if with_reading:
            self.read_file()

    def read_file(self):
        with open(self.filename) as file_input:
            self.data = json.load(file_input)
        self.check_data()

    def check_data(self):
        self.count_elements_in_list = None
        for el in self.data:
            assert type(self.data[el]) is list, f"key = <{el}> is not array"
            if self.count_elements_in_list is None:
                self.count_elements_in_list = len(self.data[el])
            assert self.count_elements_in_list == len(self.data[el]), \
                    f"array with key = <{el}> hasn't need len"

    def print(self):
        template_format = self.make_template_for_print()
        for key in self.data:
            print(template_format.format(key, *self.data[key]))

    def make_template_for_print(self):
        first_col_size, col_size = self._get_column_size()
        count_of_cols = self._get_count_of_columns()
        template_format = "{:>" + str(first_col_size) + "}"
        template_format += ("{:>" + str(col_size) + "}") * (count_of_cols)
        return template_format


    def _get_column_size(self) -> tuple:
        mx_col_size = 0
        mx_first_col_size = 0
        for row in self.data:
            mx_first_col_size = max(len(str(row)), mx_first_col_size)
            for el in self.data[row]:
                mx_col_size = max(len(str(el)), mx_col_size)
        # we are increasing this value, because need space with long el
        return (mx_first_col_size + 1, mx_col_size + 1)

    def _get_count_of_columns(self) -> int:
        return self.count_elements_in_list


if __name__ == '__main__':
    filename = input('Please, input path to json file: ')
    json_table = JSONTable(filename)
    print()
    json_table.print()

