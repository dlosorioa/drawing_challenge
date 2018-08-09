
import os 
import re
import logging
_logger = logging.getLogger(__name__)

label = 'Canvas'

key = 'C'

def parse(args):
    args_regexp = r'^' + key + r'((\s+\d+){2})\s*$'
    match = re.search(args_regexp, args)

    if (match):
        match = match.group(1).split()
        return int(match[0]), int(match[1])

    return None, None


def render(panel, palette, args):
    width, height = parse(args)

    if width == None:
        _logger.error("{} - Error parsing parameters: {}".format(label, args))
        return False

    panel.reset(width, height, palette.background)

    return True
