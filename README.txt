Descartes
=========

Use Shapely_ or GeoJSON-like geometric objects as matplotlib paths and patches

.. image:: http://farm5.static.flickr.com/4027/4501956705_637a74a404_o_d.png
   :width: 800
   :height: 300

Requires: matplotlib, numpy, and optionally Shapely 1.2.

Example::

  from matplotlib import pyplot
  from shapely.geometry import LineString
  
  from descartes.patch import PolygonPatch

  line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])

  fig = pyplot.figure(1, figsize=(7.5, 3), dpi=180)
  
  # 1
  ax = fig.add_subplot(121)
  
  dilated = line.buffer(0.5)
  patch1 = PolygonPatch(dilated, facecolor='#99ccff', edgecolor='#6699cc')
  ax.add_patch(patch1)
  
  x, y = line.xy
  ax.plot(x, y, color='#999999')
  
  ax.set_xlim(-1, 4)
  ax.set_ylim(-1, 3)
  
  #2
  ax = fig.add_subplot(122)

  patch2a = PolygonPatch(dilated, facecolor='#cccccc', edgecolor='#999999')
  ax.add_patch(patch2a)
  
  eroded = dilated.buffer(-0.3)

  # GeoJSON-like data works as well

  polygon = eroded.__geo_interface__
  # >>> geo['type']
  # 'Polygon'
  # >>> geo['coordinates'][0][:2]
  # ((0.50502525316941682, 0.78786796564403572), (0.5247963548222736, 0.8096820147509064))
  patch2b = PolygonPatch(polygon, facecolor='#99ccff', edgecolor='#6699cc')
  ax.add_patch(patch2b)
  
  ax.set_xlim(-1, 4)
  ax.set_ylim(-1, 3)
  
  fig.subplots_adjust(0.0, 0.0, 1.0, 1.0, 0.1)
  fig.savefig('buffering.png')

See also: examples/patches.py.

.. _Shapely: http://gispython.org/lab/wiki/Shapely

