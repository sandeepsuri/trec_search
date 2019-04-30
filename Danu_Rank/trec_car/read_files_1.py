import read_data
import format_runs
import mmap
import re
import nltk
import sys
import math
import random
import collections
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

intro_msg = "Welcome to the Text REtrieval Program\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
user_prompts = [
    "Choose One:\n",
    "(1) Pages (List pageIDs of Page files)\n",
    "(2) Paragraphs (Show/save text of Paragraph files)\n",
    "(3) Insert Seperator to textfile\n"
]

pages = ["train.pages.cbor", "train.test200.cbor", "train.test200.fold0.cbor"]
paragraphs = ["train.pages.cbor", "train.test200.cbor", "train.test200.fold0.cbor"]

print(intro_msg)
query_choice = int(input(str(user_prompts[0] + user_prompts[1] + user_prompts[2] + user_prompts[3]) + ">> "))

while True:
    if query_choice == 1:

        print("The following Pages are available:\n" + str(pages))
        page_choice = int(input("Which Page would you like to see?\n>> "))

        while True:
            if page_choice == 1:
                for page in read_data.iter_annotations(open(pages[0], 'rb')):
                    print(page.page_id)
                break

            if page_choice == 2:
                for page in read_data.iter_annotations(open(pages[1], 'rb')):
                    print(page.page_id)
                break

            if page_choice == 3:
                for page in read_data.iter_annotations(open(pages[2], 'rb')):
                    print(page.page_id)
                break

            else:
                print("That's an invalid choice, try again.")
        break

    if query_choice == 2:

        print("The following Paragraphs are available:\n" + str(paragraphs))
        paragraph_choice = int(input("Which Paragraphs would you like to see?\n>> "))

        while True:
            if paragraph_choice == 1:
                for para in read_data.iter_pages(open(paragraphs[0], 'rb')):
                    # print(para.get_text())
                    contents = para.get_text()
                    file = open("textfile_1.txt", "w", encoding=("utf-8"))
                    file.write(contents)
                    file.close()
                break

            if paragraph_choice == 2:
                for para in read_data.iter_pages(open(paragraphs[1], 'rb')):
                    # print(para.get_text())
                    contents = para.get_text()
                    file = open("textfile_2.txt", "w", encoding=("utf-8"))
                    file.write(contents)
                    file.close()
                break

            if paragraph_choice == 3:
                for para in read_data.iter_pages(open(paragraphs[2], 'rb')):
                    # print(para.get_text())
                    contents = para.get_text()
                    file = open("textfile_3.txt", "w", encoding=("utf-8"))
                    file.write(contents)
                    file.close()
                break

            else:
                print("That's an invalid choice, try again.")
        break

    else:
        print("That's an invalid choice, try again.")

class Paragraphs:
    def __init__(self, fileobj, separator='\n'):
        # self.seq: the underlying line-sequence
        # self.line_num: current index into self.seq (line number)
        # self.para_num: current index into self (paragraph number)
        try:
            self.seq = fileobj
        except AttributeError:
            self.seq = fileobj
        self.line_num = 0
        self.para_num = 0
        # allow for optional passing of separator-function
        if separator is '\n':
            def separator(line):
                return line == '\n'
        elif not callable(separator):
            raise TypeError("separator argument must be callable")
        self.separator = separator

    def __getitem__(self, index):
        if index != self.para_num:
            raise TypeError("Only sequential access supported")
        self.para_num += 1
        # start where we left off, and skip 0+ separator lines
        i = self.line_num
        while 1:
            # note: if this raises IndexError, it's OK to propagate
            # it, since we're also a finished-sequence in this case
            line = self.seq[i]
            i += 1
            if not self.separator(line): break
        # accumulate 1+ non-blank lines into list result
        result = [line]
        while 1:
            # here we must intercept IndexError, since we're not
            # finished, even when the underlying sequence is --
            # we have one or more lines in result to be returned
            try:
                line = self.seq[i]
            except IndexError:
                break
            i += 1
            if self.separator(line): break
            result.append(line)
        # update self state, return string result
        self.line_num = i
        return ''.join(result)

def show_paragraphs(filename, numpars=5):
    pp = Paragraphs(open(filename).readlines())
    for p in pp:
        print("Par#%d, line# %d: %s" % (pp.para_num, pp.line_num, repr(p)))
        if pp.para_num > numpars: break

        file = open('para.txt', 'w')
        file.write(p)
        file.close()

show_paragraphs('textfile_3.txt')