
import os 
import re
import logging
_logger = logging.getLogger(__name__)

label = 'Line'

key = 'L'

def parse(args):
    args_regexp = r'^' + key + r'((\s+\d+){4})\s*$'
    match = re.search(args_regexp, args)

    if match:
        match = match.group(1).split()
        return (int(match[0])-1, int(match[1])-1, int(match[2])-1, int(match[3])-1)

    return None, None, None, None


def trace(panel, palette, p0, p1):
    # Starting point
    y0 = min(p0[1], p1[1], panel.height())
    x0 = min(p0[0], p1[0], panel.width())

    # Ending point
    y1 = min(abs(p1[1] - p0[1]), panel.height() - y0) + 1
    x1 = min(abs(p1[0] - p0[0]), panel.width() - x0) + 1
    for y in range(y1):
        for x in range(x1):
            # adjust to [0, n-1]
            yn = y0 + y
            xn = x0 + x
            panel.set(xn, yn, palette.stroke)


def render(panel, palette, args):
    # If panel has not been initialized, ignore command
    if not panel.width():
        return False

    x1, y1, x2, y2 = parse(args)

    if x1 == None:
        _logger.error("{} - Error parsing parameters: {}".format(label, args))
        return False

    if x1 != x2 and y1 != y2:
        _logger.warning("{} - Only horizontal or vertical lines: {}".format(label, args))
        return False


    trace(panel, palette, (x1, y1), (x2, y2))

    return True
