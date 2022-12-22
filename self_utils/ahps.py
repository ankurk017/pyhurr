import xarray as xr
import numpy as np
import cartopy.crs as ccrs


def read_ahps(ahps_filename):
    ahps = xr.open_dataset(ahps_filename)
    crs = ahps["crs"]
    lon = ahps.variables["x"][:]
    lat = ahps.variables["y"][:]

    polar_proj = ccrs.NorthPolarStereo(
        central_longitude=crs.attrs["straight_vertical_longitude_from_pole"],
        true_scale_latitude=crs.attrs["standard_parallel"],
        globe=None,
    )
    plate_proj = ccrs.PlateCarree(central_longitude=0.0, globe=None)
    x_mesh, y_mesh = np.meshgrid(lon, lat)
    ahps_latlon = plate_proj.transform_points(polar_proj, x_mesh, y_mesh)
    lon_platecarre = ahps_latlon[:, :, 0]
    lat_platecarre = ahps_latlon[:, :, 1]
    obs = ahps.variables["observation"].values * 25.4
    obs[obs <= 0] = np.nan

    return lon_platecarre, lat_platecarre, obs
