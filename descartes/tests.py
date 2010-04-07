from shapely.geometry import *
import unittest

from descartes.patch import PolygonPatch

class PolygonTestCase(unittest.TestCase):
    polygon = Point(0, 0).buffer(10.0).difference(
                MultiPoint([(-5, 0), (5, 0)]).buffer(3.0))
    def test_patch(self):
        patch = PolygonPatch(self.polygon)
        self.failUnlessEqual(str(type(patch)), 
            "<class 'matplotlib.patches.PathPatch'>")
