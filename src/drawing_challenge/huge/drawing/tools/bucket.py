
import os 
import re
import logging
_logger = logging.getLogger(__name__)

label = 'Bucket'

key = 'B'

def parse(args):
    args_regexp = r'^' + key + r'((\s+\d+){2}(\s+\S))\s*$'
    match = re.search(args_regexp, args)

    if (match):
        match = match.group(1).split()
        return int(match[0])-1, int(match[1])-1, match[2]

    return None, None, None


def fill(panel, x, y, target, color):
    if panel.swap(x, y, target, color):
        fill(panel, x+1, y, target, color)
        fill(panel, x, y+1, target, color)
        fill(panel, x-1, y, target, color)
        fill(panel, x, y-1, target, color)


def render(panel, palette, args):
    # If panel has not been initialized, ignore command
    if not panel.width():
        return False

    x, y, color = parse(args)

    target = panel.get(x, y)
    if target:
        fill(panel, x, y, target, color)

    return True
