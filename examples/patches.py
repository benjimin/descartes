from matplotlib import pyplot
from shapely.geometry import *

from descartes.patch import PolygonPatch


# Create a matplotlib figure
fig = pyplot.figure(num=1, figsize=(6, 3), dpi=180)

# Create a polygon with 2 holes using buffer and difference methods
polygon = Point(0, 0).buffer(10.0).difference(
    MultiPoint([(-5, 0), (5, 0)]).buffer(3.0))

# 1
# Create a subplot
ax = fig.add_subplot(121)

# Make the polygon into a patch and add it to the subplot
patch = PolygonPatch(polygon, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)

# Fit the figure around the polygon's bounds, render, and save
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2*w, maxx + 0.2*w)
ax.set_ylim(miny - 0.2*h, maxy + 0.2*h)
ax.set_aspect(1)

# 2
# Create a subplot
ax = fig.add_subplot(122)

# Turn the GeoJSON-ish dict form of the polygon from #1 into a patch
geo = polygon.__geo_interface__
patch = PolygonPatch(geo, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)

# Fit the figure around the polygon's bounds, render, and save
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2*w, maxx + 0.2*w)
ax.set_ylim(miny - 0.2*h, maxy + 0.2*h)
ax.set_aspect(1)

fig.savefig('patches.png')

