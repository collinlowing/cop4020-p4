# Student Name: Collin Lowing
# File Name: parse.py
# Project 4
#
# Reads and parses files

class Parser:
    def __init__(self, filename):
        self.filename = filename

    def read_tokens(self):
        file = open(self.filename, "r")
        lines = file.readlines()

        # split lines into tokens delimited by ';'
        for line in lines:
            tokens = line.split(";")

        # remove newline char strings in list
        while "\n" in tokens:
            tokens.remove("\n")

        # remove whitespace
        for i in range(len(tokens)):
            tokens[i] = "".join(tokens[i].split())

        file.close()

        return tokens

    def parse_comma(self, string):
        string_list = string.split(',')

        return string_list

    def parse_transitions(self, string):
        string_list = string.split(',')
        list_length = len(string_list)

        double_list = [[]] * list_length

        for i in range(list_length):
            string_list[i] = string_list[i].replace('(', '')
            string_list[i] = string_list[i].replace(')', '')
            double_list[i] = string_list[i].split(':')

        return double_list
