################################################################################
# Automatically-generated file. Do not edit!
################################################################################

USER_OBJS :=

LIBS := -lboost_serialization -lopenblas -larmadillo -lnetcdf_c++4 -L"../lib" -lcsf64 
#Aaron's set
#LIBS := -lcsf -lboost_serialization -larmadillo #-llapack -lblas

# only uncomment lapack and blas calls if armadillo prompts linker errors (arma:: etc.) 
