#!/bin/bash
#SBATCH --account=def-guanuofa
#SBATCH --mem=100G
#SBATCH --time=1-0
#SBATCH --job-name=step-1-results
#SBATCH --output=output/step_1/both/both_step_1_no_matrix_dirpath_%j.out
#SBATCH --err=/scratch/schen123/kinases/RumHKNet_output/step_1/both/both_step_1_no_matrix_dirpath_%j.err


module load python/3.11
module load scipy-stack
module load gcc arrow/21.0.0


cd /home/schen123/projects/rrg-guanuofa/schen123/kinases/virtual_environments
source TEST/bin/activate


cd ../sbc806/RumHKNet/src/training/both
cat both_step_1_no_matrix_dirpath.sh > /home/schen123/scratch/kinases/RumHKNet_output/step_1/both/both_step_1_no_matrix_dirpath_$SLURM_JOB_ID.txt
./both_step_1_no_matrix_dirpath.sh


deactivate
