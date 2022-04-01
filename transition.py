# Student Name: Collin Lowing
# File Name: transition.py
# Project 4
#
# Holds information about the transitions for the FSA

class Transition:
    __start_state = None
    __end_state = None
    __alpha = None

    def __init__(self, start_state, end_state, alpha):
        self.__start_state = start_state
        self.__end_state = end_state
        self.__alpha = alpha

    def get_start_state(self):
        return self.__start_state

    def get_end_state(self):
        return self.__end_state

    def get_alpha(self):
        return self.__alpha

    def print(self):
        print("Transition: " + self.__start_state.get_number() + " : "
              + self.__end_state.get_number() + " : "
              + self.__alpha)
