from application import init_app
from download_grd import *

grd_file = 'ETOPO1_Ice_g_gdal.grd.gz'
#Check if ETOPO1_Ice_g_gdal.grd.gz is downloaded:
if not os.path.isfile(grd_file):
    url = f"https://www.ngdc.noaa.gov/mgg/global/relief/ETOPO1/data/ice_surface/grid_registered/netcdf/{grd_file}"
    print(f"Downloading {grd_file} (377Mb)...")
    download_file(url)
    print("Extraction...")
    extract_gz(grd_file)
    #Leave only .grd file
    os.remove(grd_file)

app = init_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
