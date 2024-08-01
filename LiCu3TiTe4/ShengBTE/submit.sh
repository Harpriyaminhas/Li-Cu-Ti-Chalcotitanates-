#!/bin/bash
#PBS -N idlebnn21
#PBS -e err_""$PBS_JOBID.err
#PBS -o out_""$PBS_JOBID.out
#PBS -l nodes=1:ppn=32
##SBATCH --mem-per-cpu=4000
##PBS -l walltime=999:00:00
cd $PBS_O_WORKDIR

source /apps/env/intel.sh
module load codes/FourPhonon
mpirun -n 16 ShengBTE 2>BTE.err >BTE.out
########
