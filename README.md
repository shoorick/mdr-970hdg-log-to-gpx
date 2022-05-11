# mdr-970hdg-log-to-gpx

Convert GPSLog/*.log files made by DVR Mystery MDR-970HDG info GPX

## Description

Digital video recorder
[Mystery MDR-970HDG](http://mysteryelectronics.ru/videoregistri-s-odnoie-kameroie/1432-mdr-970hdg)
has GPS receiver and it store collected points as tab separated
text files named `YYYYmmdd_HHMMSS.log` located in folder `GPSLog`.

This proprietary format is quite simple but not yet supported by converters
such as [GPSBabel](https://www.gpsbabel.org/). These scripts convert log files
into GPX, which can be used directly in [JOSM](https://josm.openstreetmap.de/),
uploaded to [OpenStreetMap](http://www.openstreetmap.org/)
or [Mapillary.com](https://www.mapillary.com/), and converted via GPSBabel.

There are two versions: _quick-and-dirty_ prototype with Perl and next version with Python 3.

## Requirements

### Perl

* Nothing, just Perl itself.

### Python

* Python 3,
* [gpxpy](https://pypi.org/project/gpxpy/)

## Installation

```bash
python3 -m venv .env  # or replace .env with appropriate name
. .env/bin/activate
pip install -r requirements.txt
```

## Usage

### Perl

```bash
./log2gpx.pl SOURCE.log > RESULT.gpx
cat SOURCES/*.log | ./log2gpx.pl > RESULT.gpx
```

### Python

```bash
./log2gpx.py SOURCE.log > RESULT.gpx
cat SOURCES/*.log | ./log2gpx.py > RESULT.gpx
```

## Author

Alexander Sapozhnikov shoorick@cpan.org http://shoorick.ru/
