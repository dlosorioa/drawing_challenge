#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from drawing_challenge import huge

import os
import sys

import filecmp

# Drawing load input file not existent
@pytest.fixture
def test_load_input_file_non_existent(mocker):
    print('test_load')
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            huge.drawing.draw.load('input.txt', 'output.txt')
    assert pytest_wrapped_e.type == SystemExit


inputFiles = 'files/input/'
outputFiles = 'files/output/'
assertFiles = 'files/assert/'

def test_load_draw_without_canvas(mocker):
    huge.drawing.draw.load(inputFiles + 'no_canvas.txt', outputFiles + 'no_canvas.txt')
    assert filecmp.cmp(outputFiles + 'no_canvas.txt', assertFiles + 'no_canvas.txt') == True

def test_load_canvas(mocker):
    huge.drawing.draw.load(inputFiles + 'canvas.txt', outputFiles + 'canvas.txt')
    assert filecmp.cmp(outputFiles + 'canvas.txt', assertFiles + 'canvas.txt') == True

def test_load_canvas(mocker):
    huge.drawing.draw.load(inputFiles + 'default.txt', outputFiles + 'default.txt')
    assert filecmp.cmp(outputFiles + 'default.txt', assertFiles + 'default.txt') == True

def test_load_canvas_3x3(mocker):
    huge.drawing.draw.load(inputFiles + 'panel_3x3.txt', outputFiles + 'panel_3x3.txt')
    assert filecmp.cmp(outputFiles + 'panel_3x3.txt', assertFiles + 'panel_3x3.txt') == True
