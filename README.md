apt-get update
apt-get update && apt-get install -y --no-install-recommends apt-utils
apt-get install -y aptitude
apt-get install -y binutils libproj-dev gdal-bin
aptitude install -y libgdal-dev
aptitude install -y python3-gdal
aptitude install -y binutils

pip install -r requirements.txt
