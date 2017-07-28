#!/usr/bin/perl

=head1 NAME

log2gpx.pl - Convert GPSLog/*.log files made by DVR Mystery MDR-970HDG
info GPX.

=head1 DESCRIPTION

Digital video recorder Mystery MDR-970HDG has GPS receiver and
it store collected points as tab separated text files named YYYYmmdd_HHMMSS.log
located in folder GPSLog.
This proprietary format is quite simple but not yet supported
by converters such as GPSBabel. This I<quick-and-dirty> script converts
these log files into GPX, which can be used directly in JOSM,
uploaded to OpenStreetMap or Mapillary.com, and converted via GPSBabel.

=head1 USAGE

    ./log2gpx.pl SOURCE.log > RESULT.gpx
    cat SOURCES/*.log | ./log2gpx.pl > RESULT.gpx

=head1 SEE ALSO

L<http://osm.org/>
L<https://josm.openstreetmap.de/> L<http://josm.ru/>
L<https://www.mapillary.com/>
L<https://www.gpsbabel.org/>
L<http://mysteryelectronics.ru/videoregistri-s-odnoie-kameroie/1432-mdr-970hdg>

=head1 AUTHOR

Alexander Sapozhnikov

L<E<lt>shoorick@cpan.orgE<gt>>
L<http://shoorick.ru/>

=cut

print q{<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
    <gpx version="1.1" creator="log2gpx"
        xmlns="http://www.topografix.com/GPX/1/1"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
        <trk>
            <trkseg>
};

while (<>) {
    chomp;
    s/\r//;

    my ( $time, $lat, $lon, $ele, $speed, $course ) = split /\t/;
    # Timestamp     Latitude    Longitude   Elevation   Speed (km/h)    Heading
    # 2017-07-27 19:07:46	N56.254678	E59.273161	313.4	38.72	345

    $time =~ s/ /T/;
    $time .= 'Z';

    $lat =~ s/^N//;
    $lat =~ s/^S/-/;

    $lon =~ s/^E//;
    $lon =~ s/^W/-/;

    $speed /= 3.6; # km/h to m/s

    print qq{
        <trkpt lat="$lat" lon="$lon">
            <ele>$ele</ele>
            <time>$time</time>
            <extensions>
                <speed>$speed</speed>
                <course>$course</course>
            </extensions>
        </trkpt>
    };
}

print q{
            </trkseg>
        </trk>
    </gpx>
};
