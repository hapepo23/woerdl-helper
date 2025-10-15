# utils.py

from collections import OrderedDict
import re

def unique_str(s) -> str:
	return ''.join(OrderedDict.fromkeys(s).keys())

def remove_non_alpha(s) -> str:
	return re.sub(r'[^A-Z]', '', s)

