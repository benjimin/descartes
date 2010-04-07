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
    # Convert coordinates to path vertices. Objects produced by Shapely's
    # analytic methods have the proper coordinate order, no need to sort.
    vertices = concatenate(
                    [asarray(polygon.exterior)] 
                    + [asarray(r) for r in polygon.interiors])
    codes = concatenate(
                [coding(polygon.exterior)] 
                + [coding(r) for r in polygon.interiors])
    return PathPatch(Path(vertices, codes), **kwargs)

