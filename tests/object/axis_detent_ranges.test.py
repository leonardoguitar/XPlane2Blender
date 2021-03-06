import bpy
import os
import inspect
import sys

from io_xplane2blender.tests import *
from io_xplane2blender import xplane_config

__dirname__ = os.path.dirname(__file__)

def filterLines(line):
    return isinstance(line[0],str) and\
            ("ANIM" in line[0] or\
             "ATTR_axis" in line[0] or\
             "ATTR_manip" in line[0])
    
class TestAxisDetentRanges(XPlaneTestCase):
    def test_1_gen_range_list_not_start_at_v1_min(self):
        out  = self.exportLayer(0)
        self.assertLoggerErrors(1)

    def test_2_gen_range_list_not_end_at_v1_max(self):
        out  = self.exportLayer(1)
        self.assertLoggerErrors(1)

    def test_3_gen_range_list_has_gap(self):
        out  = self.exportLayer(2)
        self.assertLoggerErrors(1)

    def test_4_gen_range_start_greater_than_end(self):
        out  = self.exportLayer(3)
        self.assertLoggerErrors(1)

    def test_5_gen_range_height_greater_than_max_lift(self):
        out  = self.exportLayer(4)
        self.assertLoggerErrors(1)

    def test_6_pit_list_of_one_cannot_be_stop_pit(self):
        out  = self.exportLayer(5)
        self.assertLoggerErrors(1)

    def test_7_pit_stop_pit_taller_than_neighbors(self):
        out  = self.exportLayer(6)
        self.assertLoggerErrors(1)

    def test_8_known_good_test(self):
        filename = inspect.stack()[0][3]
        self.assertLayerExportEqualsFixture(
            7, os.path.join(__dirname__, 'fixtures', filename + '.obj'),
            filename,
            filterLines
        )

runTestCases([TestAxisDetentRanges])
