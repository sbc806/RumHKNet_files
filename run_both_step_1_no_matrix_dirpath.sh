#!/bin/bash
#SBATCH --account=rrg-guanuofa
#SBATCH --gpus=h100:1
#SBATCH --mem=300G
#SBATCH --time=7-0
#SBATCH --job-name=both-step-1-no-matrix-dirpath
#SBATCH --output=/scratch/schen123/kinases/rumhknet_output/step_1/both/both_step_1_no_matrix_dirpath_%j.out
#SBATCH --err=/scratch/schen123/kinases/rumhknet_output/step_1/both/both_step_1_no_matrix_dirpath_%j.err


module load python/3.11
module load scipy-stack
module load gcc arrow/21.0.0


cd /home/schen123/projects/rrg-guanuofa/schen123/kinases/virtual_environments
source TEST/bin/activate


cd ../sbc806/RumHKNet/src/training/both
cat both_step_1_no_matrix_dirpath.sh > /home/schen123/scratch/kinases/rumhknet_output/step_1/both/both_step_1_no_matrix_dirpath_$SLURM_JOB_ID.txt
./both_step_1_no_matrix_dirpath.sh


deactivate
