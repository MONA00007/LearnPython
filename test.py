#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'


class Student():

    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def print_score(self):
        print(self.__name + ' : ' + self.score)

    def get_name(self):
        return self.__name


chen = Student('chen', '90')
print(chen.get_name())
chen.print_score()
