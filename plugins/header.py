'''Fix the header.'''
import string
from pathlib import Path

import brisingr
from plugins import utils

@brisingr.action
def fix(lines, **kwargs):
    token = utils.first_non_comment(lines)
    begin, end = utils.first_comment_block(lines)

    exists = token > begin

    mappings = {
        'FILE': kwargs['filename'],
        'YEAR': '2020'
    }
    
    template = (Path(__file__).parents[1]/'templates'/'header.txt').read_text()
    header = string.Template(template).substitute(mappings).splitlines()

    if not exists:
        modified = header + lines
    else:
        modified = lines[:begin] + header + lines[end:]

    return modified