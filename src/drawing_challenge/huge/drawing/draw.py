
import os 
import re
import sys

import logging

from . import tools
from . import palette
from . import panel

_logger = logging.getLogger(__name__)

def load(input_file, output_file):
    if not os.path.isfile(input_file):
        _logger.error("Input file does not exist : {}".format(input_file))
        sys.exit()

    print("Input file : {}".format(input_file))
    print("Output file : {}".format(output_file))
    output_text = []
     # Open file and process lines
    file = open(input_file, 'rU')
    for command in file:
        match = re.search(tools.keys, command)

        if match:
            tool = tools.map[match.group(1)]
            if tool.render(panel, palette, command):
                # Render Output
                rendered_text = panel.render(palette)
                print(rendered_text)
                output_text.append(rendered_text)
        else:
            _logger.warning("Unknown command : {}".format(command))

    # Close file
    file.close()

    file = open(output_file, 'w')
    file.write('\n'.join(output_text))
    file.close()