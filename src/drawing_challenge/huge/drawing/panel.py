

panel = []
size = {
    'width': 0,
    'height': 0
}

def width():
    return size['width']

def height():
    return size['height']


def reset(width, height, color):
    size['width'] = width
    size['height'] = height
    panel.clear()
    for row in range(height):
        panel.append([color] * width)


def render(palette):
    border_top = ''.join([palette.top] * (size['width'] + 2))
    text = '\n'
    for row in panel:
        text += palette.side + ''.join(row) + palette.side
        text += '\n'

    text = border_top + text + border_top
    return text


def set(x, y, color):
    if y >= 0 and y < size['height'] and x >= 0 and x < size['width']:
        panel[y][x] = color
        return color
    else:
        return None


def get(x, y):
    if y >= 0 and y < size['height'] and x >= 0 and x < size['width']:
        return panel[y][x]
    else:
        return None


def swap(x, y, target, color):
    if get(x,y) == target:
        panel[y][x] = color
        return target
    else:
        return None
