This version includes slight modifications of (1) the extra deeper groundwater structure; (2) catchment treatments for coarser modeling resolutions (e.g., actual area of boundary cells, river width/length, sealed area proportion, surface flux partitioning into surface flow and surface lateral flux, etc.); (3) Completely separated channel storage and surface ponding storage.
Main modified code files are:
./Constructors; ./Control/; ./includes;  --all necessary modifications for any changes in variables, functions, configure files.
./Budgets/*-- added grid areal proportion (“ttarea”) in each budget functions where “dx*dx” is used.
./Hydro/ --modified GWrouting.cpp, KinematicWave.cpp, CalcCatchArea.cpp, CalcInitialStreamStorage.cpp
./Tracking/
--modified MixingV_latup.cpp, OutletVals.cpp, FCdownstream.cpp
--added MixingV_plusExtraGW.cpp, OutletVals_plusExtraGW.cpp, FCdownstream.cpp, PrefluxTrack_plusExtraGW.cpp and IncrementAge_plusExtraGW.cpp for tracer mixing when the Extra deep groundwater module is activated (by setting “ExtraGW_Storage = 0” in Config.ini).
