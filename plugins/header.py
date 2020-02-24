'''Fix the header.'''
import string
from pathlib import Path

import utils

def fix(lines, **kwargs):
    begin, end = utils.first_comment_block(lines)
    template = (Path(__file__).parents[1]/'templates'/'header.txt').read_text()

    mappings = {
        'FILE': kwargs['filename'],
        'YEAR': '2020'
    }

    header = string.Template(template).substitute(mappings).splitlines()

    return lines[:begin] + header + lines[end:]