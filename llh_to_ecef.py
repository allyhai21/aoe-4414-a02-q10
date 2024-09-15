# lh_to_rz.py
#
# Usage: python3 lh_to_rz.py lat_def hae_km
#  COnvert latitude, height above ellipsoid to radius and z-height 
# Parameters:
#  let_deg: latitude in degrees 
#  hae_km: height above ellipsodie in km
#  ...
# Output:
#  Print the equatorial radius and the z-height 
#
# Written by First Last
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions

## calc denominator 
def calc_denom(ecc,lat_rad):
	return math.sqrt(1.0-(ecc**2)*math.pow(math.sin(lat_rad),2.0))

# initialize script arguments
lat_deg = float('nan') #latitude in degrees 
lon_deg = float('nan') #longitude in degrees 
hae_km  = float('nan') #height above ellipsoid in km 


# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1]) 
  lon_deg = float(sys.argv[2])
  hae_km  = float(sys.argv[3])  
else:
    print(\
        'Usage: '\
        'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
    )
    exit()

# write script below this line
lat_rad= lat_deg*(math.pi/180)
lon_rad= lon_deg*(math.pi/180)

#calculate (r_x, r_y, r_z))
denom= calc_denom(E_E, lat_rad)
c_E= R_E_KM/denom
s_E= R_E_KM*(1.0-E_E**2)/denom
r_x= (c_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y= (c_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z= (s_E+hae_km)*math.sin(lat_rad)
print(r_x)
print(r_y)
print(r_z)