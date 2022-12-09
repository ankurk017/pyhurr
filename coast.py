import matplotlib.pyplot as plt
import cartopy.crs as ccrs

import cartopy.feature as cfeature
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


def plot_coast(axes):
    countries = cfeature.NaturalEarthFeature(
        scale="50m", category="cultural", name="admin_0_countries", facecolor="none"
    )
    states = cfeature.NaturalEarthFeature(
        scale="50m",
        category="cultural",
        name="admin_1_states_provinces_lines",
        facecolor="none",
    )
    axes.add_feature(countries, edgecolor="k", linewidth=0.5)
    axes.add_feature(states, edgecolor="k", linewidth=0.5)
    gl = axes.gridlines(
        crs=ccrs.PlateCarree(),
        draw_labels=True,
        linewidth=2,
        color="gray",
        alpha=0,
        linestyle="--",
    )
    gl.top_labels = False
    gl.bottom_labels = True
    gl.left_labels = True
    gl.right_labels = False
    gl.xlines = True
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
