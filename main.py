# Student Name: Collin Lowing
# File Name: main.py
# Project 4
#
# Driving code. Calls other classes and functions

import sys
import parse
import fsa

fsa_filename = 'fsa.txt'
parser = parse.Parser(fsa_filename)
fsa = fsa.FSA()
tokens = []
alphabet = []
transitions = []
states = []
state_nodes = []
transition_nodes = []
input_string = ''

def parse_fsa():

    global tokens
    tokens = parser.read_tokens()

    if len(tokens) != 5:
        print("error: not proper FSA description in fsa.txt")
        quit()
    global alphabet
    alphabet = parser.parse_comma(tokens[1])

    # # for testing
    # print(alphabet)
    global transitions
    transitions = parser.parse_transitions(tokens[2])

    # # for testing
    # print(transitions)


def check_fsa():
    # checks if transitions are defined in alphabet
    for transition in transitions:

        # # for testing
        # print(transition[-1])

        if transition[-1] not in alphabet:
            print("alpha" + transition[-1] + "is not defined")
        # else:
        #     print("matched alphabet with state")


def read_string():
    argc = len(sys.argv)

    if argc < 2:
        print("error: no commandline arguments")
        quit()

    input_filename = sys.argv[1]
    file = open(input_filename, "r")
    global input_string
    input_string = file.readline()

    # # for testing
    # print(input_string)

    file.close()


def load_fsa():

    for transition in transitions:
        if transition[0] not in states:
            states.append(transition[0])
        if transition[1] not in states:
            states.append(transition[1])

    # # for testing
    # print(states)
    accept_states = parser.parse_comma(tokens[4])

    # # for testing
    # print(accept_states)

    for state in states:
        if state in accept_states:
            state_nodes.append(fsa.create_state(state, True))
        else:
            state_nodes.append(fsa.create_state(state, False))

    # # for testing
    # for state_node in state_nodes:
    #     state_node.print()

    for transition in transitions:
        start_state = fsa.search_state(state_nodes, transition[0])
        end_state = fsa.search_state(state_nodes, transition[1])
        transition_nodes.append(fsa.create_transition(start_state, end_state, transition[2]))

    # # print transitions for testing
    # for transition_node in transition_nodes:
    #     transition_node.print()

def generate_lisp_code():
    

# def check_valid_string():
#     start_state_number = tokens[3]
#
#     start_state = fsa.search_state(state_nodes, start_state_number)
#     end_state = fsa.traverse_fsa(start_state, transition_nodes, input_string)
#
#     # end_state.print()
#
#     if end_state.is_accept_state():
#         print("input string is legal for given FSA")
#     else:
#         print("input string is illegal for given FSA")


parse_fsa()
check_fsa()
read_string()
load_fsa()
generate_lisp_code()
