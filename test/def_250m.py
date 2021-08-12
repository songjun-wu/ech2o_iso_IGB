#*******************************************************************************
# CONFIGURATION FILE
#*******************************************************************************

import numpy as np
from datetime import datetime, timedelta

# ==============================================================================
#  Optimization characteristics
#
# ------------------------------------------------------------------------------
class Opti:

    main_path = './Outputs/'
    # -- Name of the output directory for the current assimilations
    #    if no name is provided, the default path will be that of this def file
    PATH_EXEC = 'setup_all'   

    # Number of iterations
    nit = 10

    # Take into account bare rock? (limiting soil evap)
    simRock = 0
    wetland = 0

# ==============================================================================
# Site conceptualization
#------------------------------------------------------------------------
class Site:  
    # -- Soil
    soils = ['soil0','soil1']
    ns = len(soils)
    sfiles = ['unit_' + s + '.map' for s in soils]
    # -- Vegetation
    vegs = ['veg0','veg1']
    nv = len(vegs)
    vfile = 'SpeciesParams.tab'

# ==============================================================================
# Define the measurements on which assimilation is performed as well as
# the error structures on the observations
#------------------------------------------------------------------------
class Data:  

    obsdir = './Outputs/Data/'
    
    # -- Observations used
    obs = {}
    # Soil Waters Blue Water Storage and Fluxes
    obs['OutletDischarge']       = {'sim_file':'Streamflow.tab' ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['SubsurfaceR']  = {'sim_file':'GWLatO.tab' ,'sim_pts':2,'conv':1,'type':'Ts'}
    # obs['OverlandR']    = {'sim_file':'SrfLatO.tab' ,'sim_pts':2,'conv':1,'type':'Ts'}
    #obs['SMC-L1']       = {'sim_file':'SoilMoistureL1.tab' ,'sim_pts':2,'conv':1,'type':'Ts'}
    #obs['SMC-L2']       = {'sim_file':'SoilMoistureL2.tab' ,'sim_pts':2,'conv':1,'type':'Ts'}
    #obs['SMC-L3']       = {'sim_file':'SoilMoistureL3.tab' ,'sim_pts':2,'conv':1,'type':'Ts'}
    # obs['Infilt']       = {'sim_file':'Infilt.tab'         ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['Rechar']       = {'sim_file':'Recharge.tab'       ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['Leak']         = {'sim_file':'Leakance.tab'       ,'sim_pts':1,'conv':1,'type':'Ts'}

    # # Green water fluxes
    # obs['ET']           = {'sim_file':'Evap.tab'           ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['Transp']       = {'sim_file':'EvapT.tab'          ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['Es']           = {'sim_file':'EvapS.tab'          ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['Ei']           = {'sim_file':'EvapI.tab'          ,'sim_pts':1,'conv':1,'type':'Ts'}

    # Temperature and energy balance components
    # obs['Soil-T1']       = {'sim_file':'SoilTemp_d1.tab'   ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['Soil-T2']       = {'sim_file':'SoilTemp_d2.tab'   ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['Soil-T3']       = {'sim_file':'SoilTemp_d3.tab'   ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['Surf-T']        = {'sim_file':'SkinTemp.tab'      ,'sim_pts':2,'conv':1,'type':'Ts'}
    #obs['Soil-T']        = {'sim_file':'SoilTemp.tab'      ,'sim_pts':2,'conv':1,'type':'Ts'}
    # obs['LE_tot']        = {'sim_file':'LEtot.tab'         ,'sim_pts':1,'conv':1,'type':'Ts'}
#    obs['SE_tot']        = {'sim_file':'Senstot.tab'       ,'sim_pts':1,'conv':1,'type':'Ts'}

    # Vegetation components
#    obs['LAI-0']        = {'sim_file':'lai_0.tab'          ,'sim_pts':1,'conv':1,'type':'Ts'}
#    obs['Can-T-0']      = {'sim_file':'CanopyTemp_0.tab'   ,'sim_pts':1,'conv':1,'type':'Ts'}
#    obs['GPP-0']        = {'sim_file':'GPP_0.tab'          ,'sim_pts':1,'conv':1,'type':'Ts'}

    # Isotopic values of interest
    #obs['d2H-Outletsurface']   = {'sim_file':'d2H_surface.tab'     ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['d18O-Outletsurface']   = {'sim_file':'d18O_surface.tab'   ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['d2H-surface']   = {'sim_file':'d2H_surface.tab'     ,'sim_pts':2,'conv':1,'type':'Ts'}
    # obs['d2H-Soil-L1']   = {'sim_file':'d2H_soilL1.tab'     ,'sim_pts':2,'conv':1,'type':'Ts'}
    # obs['d2H-Soil-L2']   = {'sim_file':'d2H_soilL2.tab'     ,'sim_pts':2,'conv':1,'type':'Ts'}
    # obs['d2H-GW']   = {'sim_file':'d2H_groundwater.tab'     ,'sim_pts':3,'conv':1,'type':'Ts'}
    # obs['d2H-ExtraGW']   = {'sim_file':'d2H_ExtraGWOut.tab'     ,'sim_pts':3,'conv':1,'type':'Ts'}
    # obs['Age-Outletsurface']   = {'sim_file':'Age_surface.tab'     ,'sim_pts':1,'conv':1,'type':'Ts'}
    # obs['Age-surface']   = {'sim_file':'Age_surface.tab'     ,'sim_pts':2,'conv':1,'type':'Ts'}
    # obs['Age-Soil-L1']   = {'sim_file':'Age_soilL1.tab'     ,'sim_pts':2,'conv':1,'type':'Ts'}
    # obs['Age-Soil-L2']   = {'sim_file':'Age_soilL2.tab'     ,'sim_pts':2,'conv':1,'type':'Ts'}
    # obs['Age-GW']   = {'sim_file':'Age_groundwater.tab'     ,'sim_pts':2,'conv':1,'type':'Ts'}

    nobs = len(obs)
    # -- Simulations outputs

    # Starting date
    simbeg = datetime(2001,1,1)
    lsim = 365 #3635
    
    # Number of obsrvations points 
    nts = 4
    sim_order = [1,2,3,4]

# ==============================================================================
# Parameters that are optimized
# ------------------------------------------------------------------------------
class Paras:
       
    # -- Parameters to optimize: dimensions
    ref = {}

    # - soil-dependent
    #ref['Depth_1']     = {'soil':1, 'veg':0, 'log':0, 'file':'depth_soil',    'min':[0.7], 'max':[8]}
    # ref['HLayer1']   = {'soil':1, 'veg':0, 'log':0, 'file':'depth_soilL1','min':[0.05,0.05],'max':[0.25,0.25]}
    # ref['HLayer2']   = {'soil':1, 'veg':0, 'log':0, 'file':'depth_soilL2','min':[0.05,0.05],'max':[0.5,0.5]}
    ref['Porosity']  = {'soil':1, 'veg':0, 'log':0, 'file':'poros',        'min':[0.4,0.4],'max':[0.5,0.5]}
    ref['Ktop']    = {'soil':1, 'veg':0, 'log':1, 'file':'Keff',         'min':[1e-6,1e-6],'max':[1e-4,1e-4]}
    ref['Anisotropy']= {'soil':1, 'veg':0, 'log':1, 'file':'KvKh',         'min':[1e-4,1e-4],'max':[0.5,0.5]}
    ref['BClambda']  = {'soil':1, 'veg':0, 'log':0, 'file':'BClambda',     'min':[2,2], 'max':[12,12]}
    ref['PsiAE']     = {'soil':1, 'veg':0, 'log':0, 'file':'psi_ae',       'min':[0.01,0.01],'max':[0.8,0.8]}
    # ref['SMresidual']= {'soil':1, 'veg':0, 'log':0, 'file':'theta_r',      'min':[0.01,0.01],'max':[0.05,0.05]}
    ref['kKexp']     = {'soil':1, 'veg':0, 'log':0, 'file':'kKsat',       'min':[0.1,0.1],'max':[15,15]} #yangx--changed "log" from 1 to 0
    ref['kPorosity'] = {'soil':1, 'veg':0, 'log':0, 'file':'kporos',       'min':[2,2],   'max':[10,10]}
    #ref['Wc']        = {'soil':1, 'veg':0, 'log':0, 'file':'Wc',           'min':[0.5,0.5], 'max':[0.7,0.7]}
    #ref['Wp']        = {'soil':1, 'veg':0, 'log':0, 'file':'Wp',           'min':[3,3],   'max':[12,12]}
    ref['snowmeltCo']= {'soil':1, 'veg':0, 'log':1, 'file':'snowmeltCoeff','min':[1e-9,1e-9],'max':[2e-7,2e-7]}
    ref['leakance']  = {'soil':1, 'veg':0, 'log':1, 'file':'leakance',     'min':[1e-6,1e-6],'max':[1e-2,1e-2]}
    # ref['dampdepth'] = {'soil':1, 'veg':0, 'log':0, 'file':'dampdepth',    'min':[0.5,0.5], 'max':[2,2]}
    # ref['tempdamp']  = {'soil':1, 'veg':0, 'log':0, 'file':'temp_damp',    'min':[5,5],   'max':[15,15]}
    # ref['SthermalK'] = {'soil':1, 'veg':0, 'log':0, 'file':'soilthermalK', 'min':[0.05,0.05],'max':[0.3,0.3]}
    ref['Sheatcap']  = {'soil':1, 'veg':0, 'log':1, 'file':'soilheatcap',  'min':[1e4,1e4], 'max':[1e8,1e8]}
    ref['albedoS']   = {'soil':1, 'veg':0, 'log':0, 'file':'albedo',       'min':[0.1,0.1], 'max':[0.4,0.4]}
    # ref['Rugosity']  = {'soil':1, 'veg':0, 'log':0, 'file':'randrough',    'min':[0.01,0.01],'max':[0.2,0.2]}

    # - uniform channel parameters
    ref['ChanGWSeep']= {'soil':0, 'veg':0, 'log':0, 'file':'chanparam',    'min':[0.001],  'max':[10]}
    ref['manningRiv']= {'soil':0, 'veg':0, 'log':0, 'file':'chanmanningn', 'min':[50],  'max':[150]}

    #ref['ChanExtraGWSeep']= {'soil':0, 'veg':0, 'log':0, 'file':'chanExtraparam',    'min':[0.001],  'max':[10]}
    #ref['HydroFrac_ExtraGW']= {'soil':0, 'veg':0, 'log':0, 'file':'ExtraGW_hydroFraction',    'min':[0.001],  'max':[0.1]}
 
    # - vegetation-dependent
    # vegetation state in maps
#    ref['LAI']       = {'soil':0, 'veg':0, 'log':0,'min':4,   'max':5,   'file':'lai_0'}
#    ref['ntr_Crops'] = {'soil':0, 'veg':0, 'log':1,'min':0.1, 'max':0.3, 'file':'ntr_0'}
#    ref['bas_Crops'] = {'soil':0, 'veg':0, 'log':1,'min':1e-5,'max':0.1, 'file':'bas_0'}
#    ref['hgt_Grass'] = {'soil':0, 'veg':0, 'log':0,'min':0.1,  'max':0.5,  'file':'hgt_0'}
#    ref['Rt_Crops']  = {'soil':0, 'veg':0, 'log':0,'min':100, 'max':1000,'file':'root_0'}
     # # water use
    ref['gsmax']    = {'soil':0, 'veg':1, 'log':1,'min':[1e-3,1e-3], 'max':[5e-2,5e-2]}
    # ref['CanopyQuantumEffic']   = {'soil':0, 'veg':1, 'log':1,'min':[1e-7,1e-7], 'max':[1e-5,1e-5]}
    # ref['CanopyQuantumEffic']   = {'soil':0, 'veg':1, 'log':1,'min':[1e-7,1e-7], 'max':[1.5e-2,1.5e-2]}
    # ref['OptimalTemp']      = {'soil':0, 'veg':1, 'log':0,'min':[5,5],    'max':[25,25]}
    # ref['MaxTemp']      = {'soil':0, 'veg':1, 'log':0,'min':[25,25],   'max':[40,40]}
    # ref['MinTemp']      = {'soil':0, 'veg':1, 'log':0,'min':[-5,-5],   'max':[5,5]}
    # ref['FoliageAllocCoef_a']={'soil':0, 'veg':1, 'log':0,'min':[1.5,1.5],  'max':[3,3]}
    # ref['FoliageAllocCoef_b']={'soil':0, 'veg':1, 'log':1,'min':[1e-3,1e-3], 'max':[5e-2,5e-2]}
    # ref['StemAllocCoef_a']={'soil':0, 'veg':1, 'log':0,'min':[2,2],    'max':[4,4]}
    # ref['StemAllocCoef_b']={'soil':0, 'veg':1, 'log':1,'min':[1e-8,1e-8], 'max':[9e-6,9e-6]}
    ref['gs_light_coeff']  = {'soil':0, 'veg':1, 'log':0,'min':[1,1],    'max':[500,500]}
    ref['gs_vpd_coeff']    = {'soil':0, 'veg':1, 'log':1,'min':[1e-4,1e-4], 'max':[1e-2,1e-2]}
    ref['gs_psi_d']     = {'soil':0, 'veg':1, 'log':0,'min':[0.01,0.01],  'max':[8.5,8.5]}
    ref['gs_psi_c']     = {'soil':0, 'veg':1, 'log':0,'min':[0.5,0.5],  'max':[10,10]}
    # ref['WiltingPnt']   = {'soil':0, 'veg':1, 'log':0,'min':[0.01,0.01], 'max':[0.05,0.05]}
    # ref['SpecificLeafArea']       = {'soil':0, 'veg':1, 'log':1,'min':[1e-5,1e-5], 'max':[5e-2,5e-2]}
    # ref['SpecificRootArea']       = {'soil':0, 'veg':1, 'log':1,'min':[1e-5,1e-5], 'max':[5e-2,5e-2]}
    # #ref['WoodDens']  = {'soil':0, 'veg':1, 'log':0,'min':[],'max':[]}
    # ref['Fhdmax']    = {'soil':0, 'veg':1, 'log':0,'min':[11,100],   'max':[22,500]}
    # ref['Fhdmin']    = {'soil':0, 'veg':1, 'log':0,'min':[1,10],    'max':[10,20]}
    # ref['LeafTurnoverRate']   = {'soil':0, 'veg':1, 'log':1,'min':[1e-9,1e-9], 'max':[1e-7,1e-7]}
    # ref['MaxLeafTurnoverWaterStress']= {'soil':0,'veg':1, 'log':1,'min':[1e-9,1e-9], 'max':[1e-7,1e-7]}
    # ref['LeafTurnoverWaterStressParam']= {'soil':0,'veg':1, 'log':1,'min':[1e-9,1e-9], 'max':[0.5,0.5]}
    # ref['MaxLeafTurnoverTempStress']= {'soil':0,'veg':1, 'log':1,'min':[1e-9,1e-9], 'max':[1e-7,1e-7]}
    # ref['LeafTurnoverTempStressParam']= {'soil':0,'veg':1, 'log':1,'min':[1e-9,1e-9], 'max':[0.5,0.5]}
    # ref['ColdStressParam']= {'soil':0,'veg':1,'log':0,'min':[-5,-5],   'max':[5,5]}
    # ref['RootTurnoverRate']   = {'soil':0, 'veg':1, 'log':1,'min':[1e-9,1e-9], 'max':[1e-7,1e-7]}
    ref['MaxCanStorageParam']   = {'soil':0, 'veg':1, 'log':1,'min':[1e-5,1e-5], 'max':[5e-4,5e-4]}
    ref['Kroot']  = {'soil':0, 'veg':1, 'log':0,'min':[0.1,0.1],  'max':[5,5]}
    # # energy balance
    # ref['albedo']    = {'soil':0, 'veg':1, 'log':0,'min':[0.1,0.1],  'max':[0.25,0.25]}
    # ref['emissivity']= {'soil':0, 'veg':1, 'log':0,'min':[0.9,0.9],  'max':[0.99,0.99]}
    ref['KBeers']    = {'soil':0, 'veg':1, 'log':0,'min':[0.1,0.1],  'max':[1,1]}
    # ref['CanopyWatEffic']   = {'soil':0, 'veg':1, 'log':0,'min':[500,500],  'max':[5000,5000]}
    # ref['DeadGrassLeafTurnoverRate'] ={'soil':0,'veg':1, 'log':1,'min':[1e-9,1e-9], 'max':[2e-6,2e-6]}
    # ref['DeadGrassLeafTurnoverTempAdjustment']={'soil':0,'veg':1, 'log':0,'min':[10,10],   'max':[20,20]}
