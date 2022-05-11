#!/usr/bin/env python

"""
Name
----

log2gpx.py - Convert GPSLog/*.log files made by DVR Mystery MDR-970HDG
info GPX.

Description
-----------

Digital video recorder Mystery MDR-970HDG has GPS receiver and
it store collected points as tab separated text files named YYYYmmdd_HHMMSS.log
located in folder GPSLog.
This proprietary format is quite simple but not yet supported
by converters such as GPSBabel. This script converts
these log files into GPX, which can be used directly in JOSM,
uploaded to OpenStreetMap or Mapillary.com, and converted via GPSBabel.

Usage
-----

    ./log2gpx.pl SOURCE.log > RESULT.gpx
    cat SOURCES/*.log | ./log2gpx.pl > RESULT.gpx

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
    description='Convert GPSLog/*.log files made by DVR Mystery MDR-970HDG info GPX.'
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
        time, lat, lon, ele, speed, course = line.rstrip().split('\t')
        # Timestamp     Latitude    Longitude   Elevation   Speed (km/h)    Heading
        # 2017-07-27 19:07:46	N56.254678	E59.273161	313.4	38.72	345

        # Create points:
        segment.points.append(gpxpy.gpx.GPXTrackPoint(
            # course=course,
            elevation=ele,
            latitude=lat.replace('N', '').replace('S', '-'),
            longitude=lon.replace('E', '').replace('W', '-'),
            speed=float(speed) / 3.6, # km/h to m/s
            time=datetime.datetime.fromisoformat(time),
        ))

print(gpx.to_xml())
