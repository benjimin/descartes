from matplotlib.patches import PathPatch
from matplotlib.path import Path
from numpy import asarray, concatenate, ones

def PolygonPatch(polygon, **kwargs):
    def coding(ob):
        # The codes will be all "LINETO" commands, except for "MOVETO"s at the
        # beginning of each subpath
        n = len(ob.coords)
        vals = ones(n, dtype=Path.code_type) * Path.LINETO
        vals[0] = Path.MOVETO
        return vals
    def pathify(ob):
        # Convert coordinates to path vertices. Objects produced by Shapely's
        # analytic methods have the proper coordinate order, no need to sort.
        vertices = concatenate(
                    [asarray(ob.exterior)] 
                    + [asarray(r) for r in ob.interiors])
        codes = concatenate(
                [coding(ob.exterior)] 
                + [coding(r) for r in ob.interiors])
        return Path(vertices, codes)
    return PathPatch(pathify(polygon), **kwargs)

