dset ^gradsplots.dat
options  byteswapped
undef 1.e30
title  OUTPUT FROM WRF V3.8.1 MODEL
xdef   97 levels 
   258.04773    
   258.31757    
   258.58740    
   258.85724    
   259.12708    
   259.39691    
   259.66678    
   259.93661    
   260.20645    
   260.47629    
   260.74612    
   261.01596    
   261.28580    
   261.55563    
   261.82547    
   262.09534    
   262.36517    
   262.63501    
   262.90485    
   263.17468    
   263.44452    
   263.71436    
   263.98419    
   264.25403    
   264.52386    
   264.79370    
   265.06354    
   265.33337    
   265.60321    
   265.87305    
   266.14288    
   266.41275    
   266.68259    
   266.95242    
   267.22226    
   267.49210    
   267.76193    
   268.03177    
   268.30161    
   268.57144    
   268.84128    
   269.11115    
   269.38098    
   269.65082    
   269.92065    
   270.19049    
   270.46033    
   270.73016    
   271.00000    
   271.26984    
   271.53967    
   271.80951    
   272.07935    
   272.34918    
   272.61902    
   272.88885    
   273.15872    
   273.42856    
   273.69839    
   273.96823    
   274.23807    
   274.50790    
   274.77774    
   275.04758    
   275.31741    
   275.58725    
   275.85712    
   276.12695    
   276.39679    
   276.66663    
   276.93646    
   277.20630    
   277.47614    
   277.74597    
   278.01581    
   278.28564    
   278.55548    
   278.82532    
   279.09515    
   279.36499    
   279.63483    
   279.90466    
   280.17453    
   280.44437    
   280.71420    
   280.98404    
   281.25388    
   281.52371    
   281.79355    
   282.06339    
   282.33322    
   282.60309    
   282.87292    
   283.14276    
   283.41260    
   283.68243    
   283.95227    
ydef   69 levels 
   16.428871    
   16.687515    
   16.945808    
   17.203751    
   17.461342    
   17.718567    
   17.975426    
   18.231903    
   18.487999    
   18.743721    
   18.999054    
   19.253998    
   19.508545    
   19.762688    
   20.016434    
   20.269768    
   20.522690    
   20.775192    
   21.027275    
   21.278931    
   21.530159    
   21.780960    
   22.031311    
   22.281219    
   22.530685    
   22.779709    
   23.028275    
   23.276382    
   23.524025    
   23.771202    
   24.017914    
   24.264145    
   24.509911    
   24.755188    
   25.000000    
   25.244316    
   25.488136    
   25.731453    
   25.974297    
   26.216621    
   26.458450    
   26.699776    
   26.940590    
   27.180878    
   27.420670    
   27.659935    
   27.898674    
   28.136887    
   28.374565    
   28.611717    
   28.848343    
   29.084427    
   29.319969    
   29.554970    
   29.789421    
   30.023331    
   30.256691    
   30.489487    
   30.721741    
   30.953423    
   31.184555    
   31.415115    
   31.645119    
   31.874557    
   32.103424    
   32.331711    
   32.559433    
   32.786575    
   33.013138    
zdef   29 linear 1 1  
tdef    9 linear 00Z28AUG2005     360MN      
VARS   30
pressure      29  0  Model pressure (hPa)
geopt         29  0  Geopotential (m2/s2)
height        29  0  Model height (km)
tk            29  0  Temperature (K)
tc            29  0  Temperature (C)
theta         29  0  Potential Temperature (K)
td            29  0  Dewpoint Temperature (C)
td2            1  0  Dewpoint Temperature at 2m (C)
rh            29  0  Relative Humidity (%)
clflo          1  0  Low Cloud Fraction (%)
clfmi          1  0  Mid Cloud Fraction (%)
clfhi          1  0  High Cloud Fraction (%)
rh2            1  0  Relative Humidity at 2m (%)
wspd          29  0  Wind Speed (m s-1)
wdir          29  0  Wind Direction (Degrees)
ws10           1  0  Wind Speed at 10 M (m s-1)
wd10           1  0  Wind Direction at 10 M (Degrees)
umet          29  0  Rotated wind component (m s-1)
vmet          29  0  Rotated wind component (m s-1)
u10m           1  0  Rotated wind component (m s-1)
v10m           1  0  Rotated wind component (m s-1)
slp            1  0  Sea Levelp Pressure (hPa)
dbz           29  0  Reflectivity (-)
max_dbz        1  0  Max Reflectivity (-)
cape          29  0  CAPE (J/kg)
cin           29  0  CIN (J/kg)
mcape          1  0  MCAPE (J/kg)
mcin           1  0  MCIN (J/kg)
lcl            1  0  LCL (meters AGL)
lfc            1  0  LFC (meters AGL)
ENDVARS
@ global String comment TITLE =  OUTPUT FROM WRF V3.8.1 MODEL
@ global String comment START_DATE = 2005-08-28_00:00:00
@ global String comment SIMULATION_START_DATE = 2005-08-28_00:00:00
@ global String comment WEST-EAST_GRID_DIMENSION =    98
@ global String comment SOUTH-NORTH_GRID_DIMENSION =    70
@ global String comment BOTTOM-TOP_GRID_DIMENSION =    30
@ global String comment DX =     30000.00
@ global String comment DY =     30000.00
@ global String comment SKEBS_ON =     0
@ global String comment SPEC_BDY_FINAL_MU =     1
@ global String comment USE_Q_DIABATIC =     0
@ global String comment GRIDTYPE = C
@ global String comment DIFF_OPT =     1
@ global String comment KM_OPT =     4
@ global String comment DAMP_OPT =     0
@ global String comment DAMPCOEF =         0.20
@ global String comment KHDIF =         0.00
@ global String comment KVDIF =         0.00
@ global String comment MP_PHYSICS =     3
@ global String comment RA_LW_PHYSICS =     1
@ global String comment RA_SW_PHYSICS =     1
@ global String comment SF_SFCLAY_PHYSICS =     1
@ global String comment SF_SURFACE_PHYSICS =     2
@ global String comment BL_PBL_PHYSICS =     1
@ global String comment CU_PHYSICS =     1
@ global String comment SF_LAKE_PHYSICS =     0
@ global String comment SURFACE_INPUT_SOURCE =     3
@ global String comment SST_UPDATE =     0
@ global String comment GRID_FDDA =     0
@ global String comment GFDDA_INTERVAL_M =     0
@ global String comment GFDDA_END_H =     0
@ global String comment GRID_SFDDA =     0
@ global String comment SGFDDA_INTERVAL_M =     0
@ global String comment SGFDDA_END_H =     0
@ global String comment HYPSOMETRIC_OPT =     2
@ global String comment USE_THETA_M =     0
@ global String comment SF_URBAN_PHYSICS =     0
@ global String comment SHCU_PHYSICS =     0
@ global String comment MFSHCONV =     0
@ global String comment FEEDBACK =     0
@ global String comment SMOOTH_OPTION =     0
@ global String comment SWRAD_SCAT =         1.00
@ global String comment W_DAMPING =     0
@ global String comment DT =       180.00
@ global String comment RADT =        30.00
@ global String comment BLDT =         0.00
@ global String comment CUDT =         5.00
@ global String comment AER_OPT =     0
@ global String comment SWINT_OPT =     0
@ global String comment AER_TYPE =     1
@ global String comment AER_AOD550_OPT =     1
@ global String comment AER_ANGEXP_OPT =     1
@ global String comment AER_SSA_OPT =     1
@ global String comment AER_ASY_OPT =     1
@ global String comment AER_AOD550_VAL =         0.12
@ global String comment AER_ANGEXP_VAL =         1.30
@ global String comment AER_SSA_VAL =         0.00
@ global String comment AER_ASY_VAL =         0.00
@ global String comment MOIST_ADV_OPT =     1
@ global String comment SCALAR_ADV_OPT =     1
@ global String comment TKE_ADV_OPT =     1
@ global String comment DIFF_6TH_OPT =     0
@ global String comment DIFF_6TH_FACTOR =         0.12
@ global String comment OBS_NUDGE_OPT =     0
@ global String comment BUCKET_MM =        -1.00
@ global String comment BUCKET_J =        -1.00
@ global String comment PREC_ACC_DT =         0.00
@ global String comment SF_OCEAN_PHYSICS =     0
@ global String comment ISFTCFLX =     0
@ global String comment ISHALLOW =     0
@ global String comment ISFFLX =     1
@ global String comment ICLOUD =     1
@ global String comment ICLOUD_CU =     0
@ global String comment TRACER_PBLMIX =     1
@ global String comment SCALAR_PBLMIX =     0
@ global String comment YSU_TOPDOWN_PBLMIX =     0
@ global String comment GRAV_SETTLING =     0
@ global String comment DFI_OPT =     0
@ global String comment SIMULATION_INITIALIZATION_TYPE = REAL-DATA CASE
@ global String comment WEST-EAST_PATCH_START_UNSTAG =     1
@ global String comment WEST-EAST_PATCH_END_UNSTAG =    97
@ global String comment WEST-EAST_PATCH_START_STAG =     1
@ global String comment WEST-EAST_PATCH_END_STAG =    98
@ global String comment SOUTH-NORTH_PATCH_START_UNSTAG =     1
@ global String comment SOUTH-NORTH_PATCH_END_UNSTAG =    69
@ global String comment SOUTH-NORTH_PATCH_START_STAG =     1
@ global String comment SOUTH-NORTH_PATCH_END_STAG =    70
@ global String comment BOTTOM-TOP_PATCH_START_UNSTAG =     1
@ global String comment BOTTOM-TOP_PATCH_END_UNSTAG =    29
@ global String comment BOTTOM-TOP_PATCH_START_STAG =     1
@ global String comment BOTTOM-TOP_PATCH_END_STAG =    30
@ global String comment GRID_ID =     1
@ global String comment PARENT_ID =     0
@ global String comment I_PARENT_START =     1
@ global String comment J_PARENT_START =     1
@ global String comment PARENT_GRID_RATIO =     1
@ global String comment CEN_LAT =        25.00
@ global String comment CEN_LON =       -89.00
@ global String comment TRUELAT1 =         0.00
@ global String comment TRUELAT2 =         0.00
@ global String comment MOAD_CEN_LAT =        25.00
@ global String comment STAND_LON =       -89.00
@ global String comment POLE_LAT =        90.00
@ global String comment POLE_LON =         0.00
@ global String comment GMT =         0.00
@ global String comment JULYR =  2005
@ global String comment JULDAY =   240
@ global String comment MAP_PROJ =     3
@ global String comment MAP_PROJ_CHAR = Mercator
@ global String comment MMINLU = USGS
@ global String comment NUM_LAND_CAT =    24
@ global String comment ISWATER =    16
@ global String comment ISLAKE =    -1
@ global String comment ISICE =    24
@ global String comment ISURBAN =     1
@ global String comment ISOILWATER =    14
