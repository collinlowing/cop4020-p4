# Student Name: Collin Lowing
# File Name: state.py
# Project 4
#
# Holds state on each state in the FSA

class State:
    __number = None
    __accept = False
    __in_chars = []
    __out_chars = []

    def __init__(self, number, accept):
        self.__number = number
        self.__accept = accept

    def get_number(self):
        return self.__number

    def is_accept_state(self):
        return self.__accept

    def print(self):
        if self.__accept:
            print("State " + self.__number + " is accept state")
        else:
            print("State " + self.__number + " is not accept state")

    def set_in_characters(self, in_chars):
        self.__in_chars = in_chars

    def get_in_characters(self):
        return self.__in_chars

    def set_out_characters(self, out_chars):
        self.__out_chars = out_chars

    def get_out_characters(self):
        return self.__out_chars
