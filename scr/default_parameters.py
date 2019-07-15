def default_parameters(PROGRAM):
    #&Global
    GLOBAL={}
    GLOBAL["RUN_TYPE"]="ENERGY"
    GLOBAL["PROJECT_NAME"]="test"
    GLOBAL["FILE_NAME"]=GLOBAL["PROJECT_NAME"]+".inp"
    GLOBAL["PRINT_LEVEL"]="MEDIUM"
    GLOBAL["PROPERTIES"]="NONE"
    GLOBAL["NSTATES"]="1"

    #&Force_eval
    FORCE_EVAL={}
    FORCE_EVAL["METHOD"]="QUICKSTEP"
    FORCE_EVAL["METHOD_SECTION"]="DFT"
    FORCE_EVAL["POISSON_SOLVER"]="PERIODIC"
    FORCE_EVAL["EACH"]="1"
    #DFT
    FORCE_EVAL["BASIS_SET_FILE_NAME-path"]="BASIS_SET.dat"
    FORCE_EVAL["BASIS_SET_FILE_NAME"]=PROGRAM["Path"]+"data/Basis_set_folder/"+FORCE_EVAL["BASIS_SET_FILE_NAME-path"]
    FORCE_EVAL["POTENTIAL_FILE_NAME-path"]="POTENTIAL.dat"
    FORCE_EVAL["POTENTIAL_FILE_NAME"]=PROGRAM["Path"]+"data/Potential_folder/"+FORCE_EVAL["POTENTIAL_FILE_NAME-path"]
    FORCE_EVAL["BASIS_SET"]="DZVP-GTH-BLYP"
    FORCE_EVAL["POTENTIAL"]="GTH-BLYP"
    FORCE_EVAL["XC_FUNCTIONAL"]="BLYP"
    FORCE_EVAL["LIBXC"]=""
    FORCE_EVAL["HF"]="FALSE"
    FORCE_EVAL["FRACTION"]="0.00"
    FORCE_EVAL["QS"]="GPW"
    FORCE_EVAL["VDW_POTENTIAL"]="NONE"
    FORCE_EVAL["MAX_SCF"]="200"
    FORCE_EVAL["EPS_SCF"]="1.0E-6"
    FORCE_EVAL["DIAGONALIZATION"]="STANDARD"
    FORCE_EVAL["PRECONDITIONER"]="FULL_KINETIC"
    FORCE_EVAL["NGRIDS"]="4"
    FORCE_EVAL["CUTOFF"]="280"
    FORCE_EVAL["REL_CUTOFF"]="40"
    #Forcefield
    FORCE_EVAL["PARMTYPE"]="OFF"
    FORCE_EVAL["PARM_FILE_NAME"]=""

    #/&Subsys
    SUBSYS={}
    SUBSYS["COORD"]=""
    SUBSYS["CENTER_COORDINATES"]="TRUE"
    SUBSYS["ABC"]="10.000 10.000 10.000"
    SUBSYS["PERIODIC"]="XYZ"
    SUBSYS["ELEMENTS"]=list()
    SUBSYS["VALENCE_ELEMENTS"]=[]
    SUBSYS["CHARGE"]="0"
    SUBSYS["MULTIPLICITY"]="0"
    SUBSYS["FIXED"]=""
    SUBSYS["TARGET1"]="-1.0"
    SUBSYS["TARGET2"]="1.0"
    SUBSYS["ATOMS_FRAG1"]=""
    SUBSYS["ATOMS_FRAG2"]=""


    #&Ext_Restart
    EXT_RESTART={}
    EXT_RESTART["SAVE_RESTART"]="FALSE"
    EXT_RESTART["RESTART_EACH"]="1"
    EXT_RESTART["RESTART"]="FALSE"
    EXT_RESTART["RESTART_FILE_NAME"]=""

    #&MOTION
    MOTION={}
    #Geo_Opt
    MOTION["TYPE"]="MINIMIZATION"  
    MOTION["OPTIMIZER"]="BFGS"
    MOTION["MAX_DR"]="3.00E-03"  
    MOTION["MAX_ITER"]="200"    
    #MD
    MOTION["ENSEMBLE"]="NVE"
    MOTION["STEPS"]="200"
    MOTION["TIMESTEP"]="0.50"
    MOTION["TEMPERATURE"]="300.00"
    MOTION["THERMOSTAT"]="NOSE"
    MOTION["TIMECON"]="100"
    #BAND
    MOTION["REPLICA1"]=""
    MOTION["REPLICA2"]=""
    MOTION["REPLICA3"]=""
    MOTION["BAND_TYPE"]="IT-NEB"
    MOTION["NUMBER_OF_REPLICA"]="10"
    MOTION["OPTIMIZE_BAND"]="DIIS"
    MOTION["MAX_STEPS"]="100"

    #Default BASIS SETS
    BASIS_SET={}
    BASIS_SET["BASIS_SETS_NAMES"]=["ALL_BASIS_SETS.dat","BASIS_ADMM.dat","BASIS_ADMM_MOLOPT.dat","BASIS_LRIGPW_AUXMOLOPT.dat","BASIS_MOLOPT.dat","BASIS_MOLOPT_UCL.dat","BASIS_RI_cc-TZ.dat","BASIS_SET.dat","BASIS_ZIJLSTRA.dat","BASIS_def2_QZVP_RI_ALL.dat","BASIS_pob-TZVP.dat","EMSL_BASIS_SETS.dat","GTH_BASIS_SETS.dat","HFX_BASIS.dat","Find"]
    BASIS_SET["ALL_BASIS_SETS.dat"]=["SADLEJ","DZ-ANO","DZV-ALL","DZVP-ALL","DZV-ALL-PADE","DZVP-ALL-PADE","DZV-ALL-PADE-NEW","DZVP-ALL-PADE-NEW","TZV-ALL-PADE","TZVP-ALL-PADE","DZV-ALL-BLYP","DZVP-ALL-BLYP","6-31G*","6-311ppG2d2p","6-311ppG3f2d","6-31ppG3f2d","DZV-GTH-PADE","DZV-GTH-PADE-CONFINED","DZVP-GTH-PADE","DZVP-GTH-PADE-CONFINED","DZV-GTH-BLYP","DZV-GTH-BLYP-CONFINED","DZVP-GTH-BLYP","DZVP-GTH-BLYP-CONFINED"]
    BASIS_SET["BASIS_ADMM.dat"]=['GTH-def2-QZVP', 'aug-GTH-def2-QZVP', 'cFIT3', 'cpFIT3', 'aug-cFIT3', 'aug-cpFIT3', 'FIT3', 'pFIT3', 'aug-FIT3', 'aug-pFIT3']
    BASIS_SET["BASIS_ADMM_MOLOPT.dat"]=['cFIT4', 'cFIT4-SR', 'cFIT5', 'cFIT5-SR', 'FIT4', 'FIT4-SR','FIT5', 'FIT5-SR']
    BASIS_SET["BASIS_LRIGPW_AUXMOLOPT.dat"]=["LRI-DZVP-MOLOPT-GTH-MEDIUM","LRI-DZVP-MOLOPT-GTH-MEDIUM-PLUS","LRI-DZVP-MOLOPT-GTH-LARGE"]
    BASIS_SET["BASIS_MOLOPT.dat"]=['SZV-MOLOPT-GTH', 'DZVP-MOLOPT-GTH', 'TZVP-MOLOPT-GTH', 'TZV2P-MOLOPT-GTH', 'TZV2PX-MOLOPT-GTH', 'SZV-MOLOPT-SR-GTH', 'DZVP-MOLOPT-SR-GTH']
    BASIS_SET["BASIS_MOLOPT_UCL.dat"]=['TZVP-MOLOPT-SR-GTH', 'TZV2P-MOLOPT-SR-GTH']
    BASIS_SET["BASIS_RI_cc-TZ.dat"]=['cc-TZ', 'RI_TZ']
    BASIS_SET["BASIS_SET.dat"]=['DZ-ANO', 'DZV-ALL', 'DZVP-ALL', 'DZV-ALL-PADE', 'DZVP-ALL-PADE', 'DZV-ALL-PADE-NEW', 'DZVP-ALL-PADE-NEW', 'TZV-ALL-PADE','TZVP-ALL-PADE', 'DZV-ALL-BLYP', 'DZVP-ALL-BLYP', '6-31G*', 'SZV-GTH-PADE', 'DZV-GTH-PADE', 'DZV-GTH-PADE-CONFINED', 'DZVP-GTH-PADE', 'DZVP-GTH-PADE-CONFINED', 'MAO-PRIM', 'DZV-GTH-BLYP', 'DZV-GTH-BLYP-CONFINED', 'DZVP-GTH-BLYP', 'DZVP-GTH-BLYP-CONFINED', 'DZV-GTH-PBE', 'DZVP-GTH-PBE', 'TZVDD3DF3PD-GTH-BLYP']
    BASIS_SET["BASIS_ZIJLSTRA.dat"]=['2SP-GTH', '4SP-GTH', '3SP-GTH']
    BASIS_SET["BASIS_def2_QZVP_RI_ALL.dat"]=['def2-QZVP', 'RI-5Z']
    BASIS_SET["BASIS_pob-TZVP.dat"]=['pob-TZVP', 'plus-pob-TZVP']
    BASIS_SET["EMSL_BASIS_SETS.dat"]=['3-21G*', '6-31G*', '6-31G**', '6-31++G**', '6-311G**', '6-311++G**', '6-311++G(2d,2p)', '6-311G(2df,2pd)', '6-311++G(3df,3pd)', 'pc-0', 'pc-1', 'pc-2', 'pc-3', 'pc-4', 'aug-pc-0', 'aug-pc-1', 'aug-pc-2', 'aug-pc-3', 'aug-pc-4', 'Ahlrichs-VDZ', 'Ahlrichs-VTZ', 'Ahlrichs-pVDZ', 'Ahlrichs-TZV', 'Ahlrichs-pTZV', 'aug-cc-pVDZ', 'aug-cc-pVTZ', 'aug-cc-pVQZ', 'aug-cc-pV5Z','IGLO-II', 'IGLO-III', 'Sadlej-pVTZ', 'Roos-ADZ-ANO', 'Roos-ATZ-ANO', 'Ahlrichs-def2-QZVP']
    BASIS_SET["GTH_BASIS_SETS.dat"]=['SZV-GTH', 'DZV-GTH', 'DZVP-GTH', 'TZVP-GTH', 'TZV2P-GTH', 'QZV2P-GTH', 'QZV3P-GTH', 'aug-DZVP-GTH', 'aug-TZVP-GTH', 'aug-TZV2P-GTH', 'aug-QZV2P-GTH', 'aug-QZV3P-GTH']
    BASIS_SET["HFX_BASIS.dat"]=['TZV2P-GTH', 'cc-TZV2P-GTH', 'cc-QZV3P-GTH', 'DZVP-GTH', 'TZ_fiodena_opt', 'RI_DZVP-GTH', 'RI_DZ_init']
    BASIS_SET["Find"]=["Custom"]

    #Default Potential
    POTENTIAL={}
    POTENTIAL["POTENTIALS_NAMES"]=["ALL_POTENTIALS.dat","ECP_POTENTIALS.dat","GTH_POTENTIALS.dat","HF_POTENTIALS.dat","MM_POTENTIAL-TZ.dat","NLCC_POTENTIALS.dat","POTENTIAL.dat","Find"]
    POTENTIAL["ALL_POTENTIALS.dat"]=["ALL"]
    POTENTIAL["ECP_POTENTIALS.dat"]=["Custom"]
    POTENTIAL["GTH_POTENTIALS.dat"]=['GTH-BLYP', 'GTH-BP', 'GTH-HCTH120', 'GTH-HCTH407', 'GTH-LDA', 'GTH-PBE', 'GTH-OLYP']
    POTENTIAL["HF_POTENTIALS.dat"]=['GTH-HF']
    POTENTIAL["MM_POTENTIAL-TZ.dat"]=["MM_FIT_POT"]
    POTENTIAL["NLCC_POTENTIALS.dat"]=['GTH-NLCC-PBE']
    POTENTIAL["POTENTIAL.dat"]=['GTH-BLYP', 'GTH-BP', 'GTH-HCTH120', 'GTH-HCTH407', 'GTH-LDA', 'GTH-PBE', 'GTH-OLYP', 'GTH-HF', 'GTH-NLCC-PBE', 'ALL']
    POTENTIAL["Find"]=["Custom"]
    return GLOBAL,FORCE_EVAL,SUBSYS,EXT_RESTART,MOTION,BASIS_SET,POTENTIAL
