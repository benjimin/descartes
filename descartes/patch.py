from matplotlib.patches import PathPatch
from matplotlib.path import Path
from numpy import asarray, concatenate, ones


class Polygon(object):
    # Adapt Shapely or GeoJSON/geo_interface polygons to a common interface
    def __init__(self, context):
        self.context = context
    @property
    def geom_type(self):
        return (getattr(self.context, 'geom_type', None) 
                or self.context['type'])
    @property
    def exterior(self):
        return (getattr(self.context, 'exterior', None) 
                or self.context['coordinates'][0])
    @property
    def interiors(self):
        return (getattr(self.context, 'interiors', [])
                or self.context['coordinates'][1:])


def PolygonPath(polygon):
    """Constructs a compound matplotlib path from a Shapely or GeoJSON-like
    object"""
    this = Polygon(polygon)
    assert this.geom_type == 'Polygon'
    def coding(ob):
        # The codes will be all "LINETO" commands, except for "MOVETO"s at the
        # beginning of each subpath
        n = len(getattr(ob, 'coords', None) or ob)
        vals = ones(n, dtype=Path.code_type) * Path.LINETO
        vals[0] = Path.MOVETO
        return vals
    vertices = concatenate(
                    [asarray(this.exterior)] 
                    + [asarray(r) for r in this.interiors])
    codes = concatenate(
                [coding(this.exterior)] 
                + [coding(r) for r in this.interiors])
    return Path(vertices, codes)


def PolygonPatch(polygon, **kwargs):
    """Constructs a matplotlib patch from a Shapely or GeoJSON-like
    object with full support for polygon holes"""
    return PathPatch(PolygonPath(polygon), **kwargs)

