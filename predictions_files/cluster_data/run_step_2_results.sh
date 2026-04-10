#!/bin/bash
#SBATCH --account=def-guanuofa
#SBATCH --mem=64G
#SBATCH --time=3:0:0
#SBATCH --job-name=step-2-results
#SBATCH --output=output/step_2_results_%j.out
#SBATCH --err=output/step_2_results_%j.err


module load python/3.11
module load scipy-stack
module load gcc arrow/21.0.0


cd /home/schen123/projects/rrg-guanuofa/schen123/kinases/virtual_environments
source TEST/bin/activate


cd /home/schen123/scratch/kinases/RumHKNet_files/predictions_files/cluster_data
python step_2_results.py


deactivate
