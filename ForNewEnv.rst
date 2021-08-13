sudo apt-get install gcc g++
sudo apt-get install libboost-all-dev
sudo apt-get install libarmadillo-dev


how to construct a rep mask?
1. Define the file name in includes/InitConf.h			string fn_inflowMask;
2. Read the file name in ReadConfigFile.cpp			Config.readInto(fn_inflowMask, "inflowMask");
3. Include mask var in Report.h  				vectCells inflowMask;
4. Construct mask in ReportConstruct.cpp
6. Modify GenerateConfigTemplate.cpp


How to add a new input varaible (time series)?
1. Define the file name in includes/InitConf.h			string fn_inflowMask;
2. Read the file name in Control/ReadConfigFile.cpp		Config.readInto(fn_inflowWaterLevel, "inflowWaterLevel");
3. Include mask var in includes/basin.h				ifstream ifinflowWaterLevel;
