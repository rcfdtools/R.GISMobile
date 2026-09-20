# -*- coding: UTF-8 -*-

from exif import Image
from moviepy.editor import VideoFileClip

def decimal_coords(coords, ref):
 decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
 if ref == 'S' or ref == 'W':
     decimal_degrees = -decimal_degrees
 return decimal_degrees

def image_coordinates(img_path):
    coords = ''
    with open(img_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref),
                      img.gps_altitude)
        except AttributeError:
            print('No Coordinates')
    else:
        print('The Image has no EXIF information')
    info = f"`File`: {src.name}. `OS version`: {img.get('software', 'Not Known')}. `Date`: {img.datetime_original}. `Aperture`: {img.aperture_value}."
    print(info)
    if coords:
        print(f"Was taken: {img.datetime_original}, and has coordinates xyz:{coords}")

def image_info(img_path):
    coords = ''
    with open(img_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref),
                      img.gps_altitude)
            cx = decimal_coords(img.gps_longitude, img.gps_longitude_ref)
            cy = decimal_coords(img.gps_latitude, img.gps_latitude_ref)
        except AttributeError:
            print('No Coordinates')
    else:
        print('The Image has no EXIF information')
    info = f"**File: {src.name}**. OS version: {img.get('software', 'Not Known')}. Date: {img.datetime_original}. Aperture: {img.aperture_value} "
    print(info)
    readme_file.write(info+'\n')
    if coords:
        map_location = ('Location over [Google Maps](http://maps.google.com/maps?q=' + str(
            cy) + ',' + str(cx) + ') or [Openstreet Map](https://www.openstreetmap.org/query?lat=' + str(cy) + '&lon=' + str(cx) + ')')
        print(f"Coordinates:{coords}")
        readme_file.write(f"<br>Coordinates & altitude: {coords}<br>")
        readme_file.write(map_location + '\n')


# Picture properties sample
img_path = '../11/2013-07-04_08.55.15.jpg'
image_coordinates(img_path)

# Convert .mp4 to .gif sample
#videoClip = VideoFileClip('7/PXL_20230503_184310359.TS.mp4').resize(0.25)
#videoClip.write_gif('7/PXL_20230503_184310359.TS.gif')
