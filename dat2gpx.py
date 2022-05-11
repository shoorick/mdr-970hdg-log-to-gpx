#!/usr/bin/env python

"""
Name
----

dat2gpx.py - Convert INFO/FILE*.dat files made by DVR Mystery MDR-970HDG
info GPX.

Description
-----------

Digital video recorder Mystery MDR-970HDG has GPS receiver and
it store collected points as tab separated text files named FILE####.dat
located in folder INFO.
This proprietary format is quite simple but not yet supported
by converters such as GPSBabel. This script converts
these log files into GPX, which can be used directly in JOSM,
uploaded to OpenStreetMap or Mapillary.com, and converted via GPSBabel.

Usage
-----

    ./dat2gpx.pl SOURCE.dat > RESULT.gpx
    cat SOURCES/*.dat | ./log2gpx.pl > RESULT.gpx

See also
--------

* http://osm.org
* https://josm.openstreetmap.de
* http://josm.ru
* https://www.mapillary.com
* https://www.gpsbabel.org
* http://mysteryelectronics.ru/videoregistri-s-odnoie-kameroie/1432-mdr-970hdg

Author
------

Alexander Sapozhnikov

<shoorick@cpan.org>
http://shoorick.ru
"""

import argparse
import datetime
import gpxpy
import gpxpy.gpx

parser = argparse.ArgumentParser(
    description='Convert INFO/FILE*.dat files made by DVR Mystery MDR-970HDG info GPX.'
)
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')

gpx = gpxpy.gpx.GPX()
track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(track)

args = parser.parse_args()
for f in args.file:
    segment = gpxpy.gpx.GPXTrackSegment()
    track.segments.append(segment)

    for line in f:
        # Type    Timestamp     Latitude    Longitude   Speed (km/h)    Course?
        # [S]     0       0       0
        # [G]     2001-07-23 17:36:24     N54.922736      E60.704700      96      75
        if line[0:3] != '[G]':
            continue
        what, time, lat, lon, speed, course = line.rstrip().split('\t')

        # Create points:
        segment.points.append(gpxpy.gpx.GPXTrackPoint(
            latitude=lat.replace('N', '').replace('S', '-'),
            longitude=lon.replace('E', '').replace('W', '-'),
            speed=float(speed) / 3.6, # km/h to m/s
            time=datetime.datetime.fromisoformat(time),
        ))

print(gpx.to_xml())
