#!/bin/bash
#SBATCH --account=def-guanuofa
#SBATCH --mem=64G
#SBATCH --time=7-0
#SBATCH --job-name=check-overlap
#SBATCH --output=output/check_overlap_%j.out
#SBATCH --err=output/check_overlap_%j.err


module load python/3.11
module load scipy-stack
module load gcc arrow/19.0.1


cd /home/schen123/projects/def-guanuofa/schen123/kinases/virtual_environments
source TEST/bin/activate

cd /home/schen123/projects/def-guanuofa/schen123/kinases/RumHKNet_files/data_splits
python -u check_overlap.py


deactivate
