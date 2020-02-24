'''Fix the footer.'''
import sys
from pathlib import Path

import utils

def fix(lines, **kwargs):
    reverse = lines[::-1]  # [::-1] is more efficient than list(reversed())

    token = utils.first_non_comment(reverse)
    begin, end = utils.first_comment_block(reverse)
    exists = token > begin
    
    template = (Path(__file__).parents[1]/'templates'/'footer.txt').read_text().splitlines()

    if not exists:
        modified = (template[::-1] + reverse)[::-1]
    else:
        modified = (reverse[:begin] + template[::-1] + reverse[end:])[::-1]

    return modified
