*********************************
:20220301 Add inflow mask:
1. Define file name "fn_inflowMask" in ./includes/InitConf.h
2. Read file name in "fn_inflowMask" in ./Control/ReadConfigFile.cpp
3. Include mask var "inflowMask" in ./includes/Report.h
4. Construct "inflowMask" in ./Constructors/ReportConstruct.cpp
5. Add "inflowMask" in ./Control/GenerateConfigTemplate.cpp

*********************************
:20220301 Build modules to read time series:
1. Define module "initiateTimeSeries", "ReadTimeSeries" in ./includes/Atmosphere.h
2. Build module "initiateTimeSeries", "ReadTimeSeries" in ./Atmosphere/InitiateClimateMap.cpp

*********************************
:20220301 Add discharge at inflow gaugue(s) in the form of time series:
1. Define file name "fn_inflowDischarge" in ./includes/InitConf.h
2. Read file name in "fn_inflowDischarge" in ./Control/ReadConfigFile.cpp
3. Include var "ifinflowDischarge" in ./includes/Atmosphere.h
4. Read all data into "ifinflowDischarge", read 1st timestep into "_inflowDischarge", and delete cache "_inflowDischarge" in ./Constructors/AtmosphConstruct.cpp
5. Read data into "_inflowDischarge" for each timestep in ./Atmosphere/AdvanceClimateMaps.cpp
6. Add inflow discharge at gaugue(s) in ./Hydro/GWrouting.cpp
7. Clean the memory "_inflowDischarge" and close the file "ifinflowDischarge" in ./Destructors/AtmosphDesctruct.cpp
