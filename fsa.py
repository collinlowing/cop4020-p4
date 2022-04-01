# Student Name: Collin Lowing
# File Name: fsa.py
# Project 4
#
# Handle FSA related operations and create objects for state and transitions

import re
import state
import transition


class FSA:
    def check_string(self, pattern, string):
        match = re.search(pattern, string)

        if match:
            print("string is legal")
        else:
            print("string is illegal")

        return match

    def create_state(self, number, accept):
        new_state = state.State(number, accept)
        return new_state

    def create_transition(self, start_state, end_state, alpha):
        new_transition = transition.Transition(start_state, end_state, alpha)
        return new_transition

    def search_state(self, states: list[state.State], number: str):
        for s in states:
            if s.get_number() == number:
                return s

    def traverse_fsa(self, starting_state: state.State, transitions: list[transition.Transition], string: str):
        current_state = starting_state

        possible_transitions = self.__get_possible_transitions(current_state, transitions)

        for char in string:
            for p_transition in possible_transitions:
                if p_transition.get_alpha() == char:
                    current_state = p_transition.get_end_state()
                    possible_transitions = self.__get_possible_transitions(current_state, transitions)
        return current_state

    def __get_possible_transitions(self, s: state.State, transitions: list[transition.Transition]):
        possible_transitions = []
        for t in transitions:
            if s == t.get_start_state():
                possible_transitions.append(t)
        return possible_transitions
