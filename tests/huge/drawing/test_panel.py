#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from drawing_challenge import huge

import os
import sys

import filecmp

@pytest.fixture
def test_panel_empty():
    assert huge.drawing.panel.width() == 0
    assert huge.drawing.panel.height() == 0
    assert len(huge.drawing.panel.panel) == 0
    assert huge.drawing.panel.set(5, 5, 't') == None
    assert huge.drawing.panel.get(5, 5) == None
    assert huge.drawing.panel.swap(5, 5, 't', 'c') == None


def test_panel_canvas_3x3():
    huge.drawing.panel.reset(3,3,' ')
    assert huge.drawing.panel.width() == 3
    assert huge.drawing.panel.height() == 3
    assert len(huge.drawing.panel.panel) == 3
    assert huge.drawing.panel.set(0, 0, 'x') == 'x'
    assert huge.drawing.panel.set(1, 1, 'x') == 'x'
    assert huge.drawing.panel.set(2, 2, 'x') == 'x'
    assert huge.drawing.panel.set(3, 3, 'x') == None

    panel_3x3_render = huge.drawing.panel.render(huge.drawing.palette)
    f = open('files/assert/panel_3x3_final.txt',"r")
    panel_3x3_file = f.read()
    f.close()
    assert panel_3x3_render == panel_3x3_file

