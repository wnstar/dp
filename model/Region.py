# encoding: utf-8


"""
@author: Wnstar
@time: 2017/12/14 21:44
"""
from model import BaseModel, add_model


@add_model(0x82b9)
class Region(BaseModel):
    field_map = {
        'a': 'regionSearchKey',
        'b': 'iD',
        'c': 'name',
        'd': 'parentID',
        'e': 'lat',
        'f': 'lng',
        'g': 'firstChar',
        'h': 'enName',
        'i': 'parentEnName',
        'j': 'count',
        'k': 'regionType',
    }

    def j_flag_2633(self):
        """
        0xa49 -> :sswitch_0
        :return:
        """
        self.result[self.field_map.get('isPresent', 'isPresent')] = self.archive_d_b()

    def j_flag_27715(self):
        """
        0x6c43 -> :sswitch_1
        :return:
        """
        self.result[self.field_map.get('k', 'k')] = self.archive_d_c()

    def j_flag_25355(self):
        """
        0x630b -> :sswitch_2
        :return:
        """
        self.result[self.field_map.get('j', 'j')] = self.archive_d_c()

    def j_flag_4315(self):
        """
        0x10db -> :sswitch_3
        :return:
        """
        self.result[self.field_map.get('i', 'i')] = self.archive_d_g()

    def j_flag_4357(self):
        """
        0x1105 -> :sswitch_4
        :return:
        """
        self.result[self.field_map.get('h', 'h')] = self.archive_d_g()

    def j_flag_23902(self):
        """
        0x5d5e -> :sswitch_5
        :return:
        """
        self.result[self.field_map.get('g', 'g')] = self.archive_d_c()

    def j_flag_11012(self):
        """
        0x2b04 -> :sswitch_6
        :return:
        """
        self.result[self.field_map.get('f', 'f')] = self.archive_d_e()

    def j_flag_10622(self):
        """
        0x297e -> :sswitch_7
        :return:
        """
        self.result[self.field_map.get('e', 'e')] = self.archive_d_e()

    def j_flag_47744(self):
        """
        0xba80 -> :sswitch_8
        :return:
        """
        self.result[self.field_map.get('d', 'd')] = self.archive_d_c()

    def j_flag_61071(self):
        """
        0xee8f -> :sswitch_9
        :return:
        """
        self.result[self.field_map.get('c', 'c')] = self.archive_d_g()

    def j_flag_2331(self):
        """
        0x91b -> :sswitch_a
        :return:
        """
        self.result[self.field_map.get('b', 'b')] = self.archive_d_c()

    def j_flag_10599(self):
        """
        0x2967 -> :sswitch_b
        :return:
        """
        self.result[self.field_map.get('a', 'a')] = self.archive_d_g()
