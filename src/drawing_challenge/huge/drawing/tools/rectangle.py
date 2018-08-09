
import os 
import re
import logging
_logger = logging.getLogger(__name__)

from . import line

label = 'Rectangle'

key = 'R'

def parse(args):
    args_regexp = r'^' + key + r'((\s+\d+){4})\s*$'
    match = re.search(args_regexp, args)

    if match:
        match = match.group(1).split()
        return int(match[0])-1, int(match[1])-1, int(match[2])-1, int(match[3])-1

    return None, None, None, None


def render(panel, palette, args):
    # If panel has not been initialized, ignore command
    if not panel.width():
        return False

    x1, y1, x2, y2 = parse(args)

    if x1 == None:
        _logger.error("{} - Error parsing parameters: {}".format(label, args))
        return False

    line.trace(panel, palette, (x1, y1), (x2, y1))
    line.trace(panel, palette, (x2, y1), (x2, y2))
    line.trace(panel, palette, (x2, y2), (x1, y2))
    line.trace(panel, palette, (x1, y2), (x1, y1))

    return True
