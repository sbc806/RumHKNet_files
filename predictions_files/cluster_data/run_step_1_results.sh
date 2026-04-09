#!/bin/bash
#SBATCH --account=def-guanuofa
#SBATCH --mem=100G
#SBATCH --time=1-0
#SBATCH --job-name=step-1-results
#SBATCH --output=output/step_1_results_%j.out
#SBATCH --err=output/step_1_results_%j.err


module load python/3.11
module load scipy-stack
module load gcc arrow/21.0.0


cd /home/schen123/projects/rrg-guanuofa/schen123/kinases/virtual_environments
source TEST/bin/activate


cd ../home/schen123/RumHKNet_files/predictions_files/cluster_data
cat both_step_1_no_matrix_dirpath.sh > /home/schen123/scratch/kinases/RumHKNet_output/step_1/both/both_step_1_no_matrix_dirpath_$SLURM_JOB_ID.txt
./both_step_1_no_matrix_dirpath.sh


deactivate
