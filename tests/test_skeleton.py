#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from drawing_challenge.skeleton import main
from drawing_challenge import huge

__author__ = "Diego Osorio"
__copyright__ = "Diego Osorio"
__license__ = "mit"



def test_main(mocker):
	mocker.patch.object(huge.drawing.draw, 'load') 
	main(['-in', 'input.txt', '-out', 'output.txt'])
	huge.drawing.draw.load.assert_called_with('input.txt', 'output.txt')