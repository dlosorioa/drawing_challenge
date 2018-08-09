
from . import canvas, line, rectangle, bucket

__all__ = [canvas, line, rectangle, bucket]

map = {}
keys = []
for tool in __all__:
	map[tool.key] = tool
	keys.append(tool.key)

keys = r'^([' + '|'.join(keys) + r'])(\s+\S*)*$'