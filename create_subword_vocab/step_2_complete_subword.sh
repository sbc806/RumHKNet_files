#!/bin/bash
#SBATCH --account=def-guanuofa
#SBATCH --cpus-per-task=8
#SBATCH --mem=128G
#SBATCH --time=7-0
#SBATCH --job-name=step-2-subword
#SBATCH --output=data_process_output/step_2_subword_%j.out
#SBATCH --err=data_process_output/step_2_subword_%j.err

module load python/3.11
module load scipy-stack
module load gcc arrow/19.0.1

cd /home/schen123/projects/def-guanuofa/schen123/kinases/virtual_environments
source TEST/bin/activate

cd ../sbc806/LucaPCycle/src/data_process/V3

python rumhknet_subword_step_2.py --func corpus --outfile ../../../subword/step_2/step_2_all_sequences_corpus.txt

python rumhknet_subword_step_2.py --func learn_bpe --num_symbols=30000 --infile ../../../subword/step_2/step_2_all_sequences_corpus.txt --outfile ../../../subword/step_2/step_2_all_sequences_corpus_codes_30000.txt --verbose

python rumhknet_subword_step_2.py --func apply_bpe --infile ../../../subword/step_2/step_2_all_sequences_corpus.txt --codes_file ../../../subword/step_2/step_2_all_sequences_corpus_codes_30000.txt --outfile ../../../subword/step_2/step_2_all_sequences_corpus_token_30000.txt

python rumhknet_subword_step_2.py --func get_vocab --infile ../../../subword/step_2/step_2_all_sequences_corpus_token_30000.txt --outfile ../../../subword/step_2/step_2_all_sequences_corpus_subword_vocab_30000_ori.txt

python rumhknet_subword_step_2.py --func subword_vocab_2_token_vocab --infile ../../../subword/step_2/step_2_all_sequences_corpus_subword_vocab_30000_ori.txt --outfile ../../../vocab/step_2/step_2_all_sequences_corpus_subword_vocab_30000.txt
