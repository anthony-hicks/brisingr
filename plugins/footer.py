'''Fix the footer.'''
import sys
from pathlib import Path

import utils

def fix(lines, **kwargs):
    reverse = lines[::-1]  # [::-1] is more efficient than list(reversed())

    begin, end = utils.first_comment_block(reverse)
    template = (Path(__file__).parents[1]/'templates'/'footer.txt').read_text().splitlines()

    footer = (reverse[:begin] + template[::-1] + reverse[end:])[::-1]

    return footer
