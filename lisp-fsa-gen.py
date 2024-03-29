# Student Name: Collin Lowing
# File Name: lisp-fsa-gen.py
# Project 4
#
# Generates lisp code with fsa.txt
import sys

import fsa
import parse

output_filename = 'part2.lisp'
string_filename = 'theString.txt'
fsa = fsa.FSA()
tokens = []
alphabet = []
transitions = []
states = []
accept_states = []
state_nodes = []
transition_nodes = []
input_string = ''


def parse_fsa():
    argc = len(sys.argv)

    if argc < 2:
        print("error: no commandline arguments")
        quit()

    fsa_filename = sys.argv[1]

    # initiate parser
    parser = parse.Parser(fsa_filename)

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

    global accept_states
    accept_states = parser.parse_comma(tokens[4])


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
    file = open(string_filename, 'r')
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
    state_transitions = fsa.get_possible_transitions(state, transition_nodes)

    stream += '(defun state' + state_num + '(stringlist)\n'
    stream += '\t(if (= (length stringlist) 0)\n'
    if state.is_accept_state():
        stream += '\t\t(return-from state' + state_num + ' 1))\n'
    else:
        stream += '\t\t(return-from state' + state_num + ' 0))\n'
    stream += '\t(let ((sublist stringlist) (n 0))\n'
    stream += '\t\t(dolist (char stringlist)\n'
    stream += '\t\t\t(cond\n'
    for s_transition in state_transitions:
        transition_char = s_transition.get_alpha()
        next_state = s_transition.get_end_state()
        if next_state.get_number() == state.get_number():
            stream += '\t\t\t\t((STRING-EQUAL char "' + transition_char + '") (setf n (+ n 1)))\n'
        else:
            stream += '\t\t\t\t((STRING-EQUAL char "' + transition_char + '") (return-from state' + state_num + ' (state' + next_state.get_number() + ' (subseq sublist (+ n 1) (length sublist)))))\n'
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
    stream += '(defun demo ()\n'
    stream += '\t(setq file (open filename :direction :input))\n'
    stream += '\t(setq stringlist (read file "done"))\n'
    stream += '\t(princ "processing ")\n'
    stream += '\t(terpri)\n'
    stream += '\t(setq current-state 0)\n'
    stream += '\t(setq accept 0)\n'
    stream += '\t(setq alphabet \'('
    # add the alphabet
    for a in alphabet:
        stream += a + ' '
    # cut the last space character out
    stream = stream[:len(stream) - 1]
    stream += '))\n'
    stream += '\t(setq inalphabet (checkalphabet stringlist alphabet))\n'
    stream += '\t(setq success (state' + start_state_number + ' stringlist))\n'
    stream += '\t(if (and (= success 1) (= inalphabet 1))\n'
    stream += '\t\t(princ "string is legal")\n'
    stream += '\t\t(princ "string is illegal")))\n'

    return stream


def generate_lisp_code():
    global_var = '(defvar filename "theString.txt")\n\n'
    state_functions = generate_states()
    check = generate_check_alphabet()
    demo = generate_demo()

    lisp_stream = global_var + state_functions + check + demo

    output_file = open(output_filename, "w")

    output_file.write(lisp_stream)
    output_file.close()


parse_fsa()
check_fsa()
read_string()
load_fsa()
generate_lisp_code()
