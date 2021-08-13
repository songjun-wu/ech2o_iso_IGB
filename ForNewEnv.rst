sudo apt-get install gcc g++
sudo apt-get install libboost-all-dev
sudo apt-get install libarmadillo-dev

New variable

Atmosphere.h
  UINT4 _nTSgrids;
  ifstream ifinflowWaterLevel;
  float *_inflowWaterLevel;  (new, delete)




What did I do today?

2021.08.13	
inflow_mask, and _inflowWaterlevel were added. To achieve this, void initiateTimeSeries(ifstream &ifHandle); void ReadTimeSeries(ifstream &ifHandle, float* value); void UpdateTimeSeries(ifstream &ifHandle, float* value) were built; The _inflowWaterlevel was introduced into GWrouting.cpp










how to construct a rep mask?
1. Define the file name in includes/InitConf.h				string fn_inflowMask;
2. Read the file name in ReadConfigFile.cpp				Config.readInto(fn_inflowMask, "inflowMask");
3. Include mask var in Report.h  					vectCells inflowMask;
4. Construct mask in ReportConstruct.cpp
6. Modify GenerateConfigTemplate.cpp


How to add a the corresponding input varaible (time series)?
1. Define the file name in includes/InitConf.h				string fn_inflowMask;
2. Read the file name in Control/ReadConfigFile.cpp			Config.readInto(fn_inflowWaterLevel, "inflowWaterLevel");
3. Include var in includes/Atmosphere.h					ifstream ifinflowWaterLevel;
									float *_inflowWaterLevel;
4. Open the file containing the var in Atmosphere/AtmosphConstrct.cpp	ifinflowWaterLevel.open((ctrl.path_ClimMapsFolder 
									+ctrl.fn_inflowWaterLevel).c_str(), ios::binary);
      									if(errno!=0) throw ctrl.fn_inflowWaterLevel;  
4. Initialize the var and read the file for first timestep		initiateTimeSeries(ifinflowWaterLevel);
									_inflowWaterLevel = new float[_nTSgrids];
									ReadTimeSeries(ifinflowWaterLevel, _inflowWaterLevel);
5. Update var for each timestep in Atmosphere/AdcanceClimateMaps.cpp	UpdateTimeSeries(ifinflowWaterLevel, _inflowWaterLevel);
6. Don't forget to delete everything you newed				if (_inflowWaterLevel)
									  delete[] _inflowWaterLevel;
7. Also, we need to close the file we opened				if(ifinflowWaterLevel.is_open())
									  ifinflowWaterLevel.close();

How to add a new map variabile (grid)?	






