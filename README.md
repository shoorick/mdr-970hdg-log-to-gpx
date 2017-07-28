# mdr-970hdg-log-to-gpx

Convert GPSLog/*.log files made by DVR Mystery MDR-970HDG info GPX

## Description

Digital video recorder [Mystery MDR-970HDG](http://mysteryelectronics.ru/videoregistri-s-odnoie-kameroie/1432-mdr-970hdg) has GPS receiver and it store collected points as tab separated text files named `YYYYmmdd_HHMMSS.log`
located in folder `GPSLog`.

This proprietary format is quite simple but not yet supported
by converters such as [GPSBabel](https://www.gpsbabel.org/). This _quick-and-dirty_ script converts
these log files into GPX, which can be used directly in [JOSM](https://josm.openstreetmap.de/),
uploaded to [OpenStreetMap](http://www.openstreetmap.org/) or [Mapillary.com](https://www.mapillary.com/), and converted via GPSBabel.

## Usage

    ./log2gpx.pl SOURCE.log > RESULT.gpx
    cat SOURCES/*.log | ./log2gpx.pl > RESULT.gpx

## Author

Alexander Sapozhnikov shoorick@cpan.org http://shoorick.ru/
