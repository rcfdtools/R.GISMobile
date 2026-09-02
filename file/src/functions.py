# https://github.com/rcfdtools/R.HydroTools/tree/main/tool/Population
# -*- coding: UTF-8 -*-

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# General parameters
# https://matplotlib.org/stable/gallery/color/named_colors.html
# https://matplotlib.org/stable/api/markers_api.html
accent_color = 'darkgoldenrod'

# Function for print and show results in a log file
def print_log(file_log, txt_print, on_screen=False, center_div=False):
    # div50 is use for show 2 plots in the same line
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print)
    if center_div:
        file_log.write('\n\n</div>\n' + '\n')

# Location map with GeoPandas (single)
def location_map(point_latitude, point_longitude, point_name, state_filter = 'All', county_label_on = False, show_marker = True, horizontal_size = 6, vertical_size = 6, plot_state = False, county_filter = 'All', plot_only_shape = False):
    county_linewidth = 0.25
    state_linewidth = 1.25
    fontsize = 10
    xytext = (6, 6)
    if state_filter == 'All' and county_filter == 'All': state_linewidth = 1.0
    if state_filter == 'All':
        state_shapefile = gpd.read_file('../shp/ColombiaState4326.shp')
        county_shapefile = gpd.read_file('../shp/ColombiaCounty4326.shp')
    else:
        state_shapefile = gpd.read_file('../shp/ColombiaState4326.shp', where=f"DeCodigo = '{state_filter}'")
        county_shapefile = gpd.read_file('../shp/ColombiaCounty4326.shp', where=f"DeCodigo = '{state_filter}'")
        #county_shapefile = gpd.read_file('../shp/ColombiaCounty4326.shp', where=f"MpCodigo = '{county_filter}'")
    if county_filter != 'All':
        county_shapefile = gpd.read_file('../shp/ColombiaCounty4326.shp', where=f"MpCodigo = '{county_filter}'")
    point_location = Point(point_longitude, point_latitude)
    point_gdf = gpd.GeoDataFrame(geometry=[point_location], crs=state_shapefile.crs)
    fig, ax = plt.subplots(figsize=(horizontal_size, vertical_size))  # Adjust figure size as needed
    if plot_only_shape: # Applied when you print only the county limit
        county_linewidth = 4
        plt.margins(0)
        ax.margins(0.025)
        ax.axis('off')
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        fontsize = 26
        xytext = (-120, 0)
    if plot_state:
        county_shapefile.boundary.plot(ax=ax, edgecolor='black', linewidth=county_linewidth)  # , label='AH'
        if county_label_on:
            state_shapefile.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=state_linewidth, legend=True, legend_kwds={'fontsize': 'small'}, label='DeCodigo')
        else:
            state_shapefile.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=state_linewidth, legend=True, legend_kwds={'fontsize': 'small'})
    else:
        # county_shapefile.boundary.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=county_linewidth) # , label='AH'
        county_shapefile.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=county_linewidth)  # , label='AH'
    #state_shapefile.plot(ax=ax, column='DeCodigo', cmap='Greens', edgecolor='black', linewidth=0.75, legend=True, legend_kwds={'fontsize': 'small'}) # , label='AH'
    #ax.legend(loc='lower left')
    if not plot_only_shape:
        ax.set_title("Map Location")
        plt.xlabel("Longitude°")
        plt.ylabel("Latitude°")
        ax.tick_params(axis='both', labelsize=9)
    else:
        plt.axis('off')
    if show_marker:
        point_gdf.plot(ax=ax, marker='o', color=accent_color, markersize=40, legend=False)  # color='black', 'marker' and 'markersize' customize the point
    ax.annotate(
        text= point_name,
        xy=(point_longitude, point_latitude),
        xytext=xytext,  # Offset the text slightly (e.g., 5 points right, 5 points up)
        textcoords="offset points",
        fontsize=fontsize,
        color='white',
        bbox=dict(boxstyle='round', facecolor=accent_color, alpha=0.9, pad=0.25)
    )
    return plt
