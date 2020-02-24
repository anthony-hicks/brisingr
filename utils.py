import re
import sys
from string import Template

def first_index(iterable, condition=lambda x: True):
    return next(i for i, element in enumerate(iterable) if condition(element))

def first_comment_block(lines):
    stripped = [line.strip() for line in lines]
    # TODO: Consider the beginning of the file the beginning of the header? Other wise we won't remove leading blank lines...
    begin = first_index(stripped, lambda line: line.startswith('//'))
    end = begin + first_index(stripped[begin:], lambda line: line and not line.startswith('//'))
    return begin, end