"""
This is the entry point for the 249 converter. Before you start poking around
make sure you read the available documentation! Don't assume anything!
"""
import collections
import copy
import enum
import os
import re
import sys
from typing import Any, Dict, List, Optional, Tuple, Union

import bpy

from io_xplane2blender import xplane_constants, xplane_helpers
from io_xplane2blender.tests import test_creation_helpers
from io_xplane2blender.xplane_249_converter import xplane_249_dataref_decoder, xplane_249_manip_decoder


_runs = 0
def do_249_conversion():
    # TODO: Create log, similar to updater log

    #TODO: When we integrate with the updater, (adding 2.49 as a legacy version)
    # We can use that. Until then, we have this hack to keep unit testing going
    global _runs
    if _runs > 0:
        return
    _runs += 1

    #if bpy.data.version[1] > 49:
    #    return

    # Global settings
    bpy.context.scene.xplane.debug = True
    # TODO: How will names be assaigned with root objects mode?
    # TODO: What about those using layers as LODs?
    filename = os.path.split(bpy.data.filepath)[1]
    bpy.context.scene.xplane.layers[0].name = filename[: filename.index(".")]

    # TODO: Remove clean up workspace as best as possible,
    # remove areas with no space data and change to best
    # defaults like Action Editor to Dope Sheet

    # Make the default material for new objects to be assaigned
    for armature in filter(lambda obj: obj.type == "ARMATURE", bpy.data.objects):
        xplane_249_dataref_decoder.convert_armature_animations(armature)
	
	# TODO: Since most objects aren't manipulators (duh)
	# this may be very inefficient on large aircraft. Perhaps some
	# hueristics or better search algorithm can improve this if need be
    for obj in filter(lambda obj: obj.type == "MESH", bpy.data.objects):
        xplane_249_manip_decoder.convert_manipulators(obj)
