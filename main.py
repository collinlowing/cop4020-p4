# Student Name: Collin Lowing
# File Name: main.py
# Project 4
#
# Driving code. Calls other classes and functions

import sys
import parse
import fsa

fsa_filename = 'fsa.txt'
output_file = 'part2.lisp'
string_filename = ''
parser = parse.Parser(fsa_filename)
fsa = fsa.FSA()
tokens = []
alphabet = []
transitions = []
states = []
state_nodes = []
transition_nodes = []
input_string = ''
lisp_stream = ''

def parse_fsa():

    global tokens
    tokens = parser.read_tokens()

    if len(tokens) != 5:
        print('error: not proper FSA description in fsa.txt')
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
            print('alpha' + transition[-1] + 'is not defined')
        # else:
        #     print('matched alphabet with state')


def read_string():
    argc = len(sys.argv)

    if argc < 2:
        print('error: no commandline arguments')
        quit()

    input_filename = sys.argv[1]
    file = open(input_filename, 'r')
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
def generate_state(state):
    stream = ''
    state_num = state.get_number()
    state_transitions = fsa.FSA.get_possible_transitions(state, transition_nodes)

    stream += '(defun state' + state_num + '(strlist)\n'
    stream += '\t(if (= (length strlist) 0)\n'
    if state.is_accept_state():
        stream += '\t\t(return-from state' + state_num + ' 1))\n'
    else:
        stream += '\t\t(return-from state' + state_num + ' 0))\n'
    stream += '\t(let ((sublist strlist) (n 0))'
    stream += '\t\t(dolist (L strlist)\n'
    stream += '\t\t\t(cond\n'
    for s_transition in state_transitions:
        transition_char = s_transition.get_alpha()
        next_state = s_transition.get_end_state()
        if next_state.get_number() == state.get_number():
            stream += '\t\t\t\t((STRING-EQUAL L "' + transition_char + '") (setf n (+ n 1)))\n'
        else:
            stream += '\t\t\t\t((STRING-EQUAL L "' + transition_char + '") (return-from state' + state_num + ' (state' + next_state.get_number() + ' (subseq sublist (+ n 1) (length sublist)))))\n'
    stream += ')))\n'
    stream += '\t(return-from state' + state_num + ' 0))\n\n'

    return stream

def generate_states():
    stream = ''
    for state in state_nodes:
        stream += generate_state(state)

    return stream

def generate_check_alphabet():
    stream = ''
    stream += '(defun checkalphabet(str alphabet)\n'
    stream += '\t(dolist (c str)\n'
    stream += '\t\t(if (find c alphabet)\n'
    stream += '\t\t\t(return-from checkalphabet 1)\n'
    stream += '\t\t\t(return-from checkalphabet 0))))\n\n'
    return stream

def generate_demo():
    start_state_number = tokens[3]
    stream = ''
    stream += '(defun demo () "runs the fsa processing\n"'
    stream += '\t(setq file (open filename :direction :input))'
    stream += '\t(setq strlist (read file "done"))'
    stream += '\t(princ "processing ")'
    stream += '\t(terpri)'
    stream += '\t(setq current-state 0)'
    stream += '\t(setq accept 0)'
    stream += '\t(setq alphabet \'('
    # add the alphabet
    for a in alphabet:
        stream += a + ' '
    # cut the last space character out
    stream = stream[:len(stream)-1]
    stream += '))'
    stream += '\t(setq inalphabet (checkalphabet strlist alphabet))'
    stream += '\t(setq success (state' + start_state_number + ' strlist))'
    stream += '\t(if (and (= success 1) (= inalphabet 1))'
    stream += '\t\t(write "string is legal")'
    stream += '\t\t(write "string is illegal")))'

    return stream

def generate_lisp_code():
    global_var = '(defvar filename "theString.txt")\n\n'
    state_functions = generate_states()
    check = generate_check_alphabet()
    demo = generate_demo()

    lisp_stream = global_var + state_functions + check + demo

    output_file = open(output_filename, "w")


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
