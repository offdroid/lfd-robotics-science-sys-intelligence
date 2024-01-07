#!/bin/bash

EXPERT_PATH_DIR="experts/sac/swimmer/expert"

python -u run_opirl.py \
  --algo opirl \
  --normalize_states \
  --use_bc_reg \
  --learn_alpha \
  --seed 1 \
  --max_timesteps 1000000 \
  --env_name Swimmer-v2 \
  --expert_path_dir $EXPERT_PATH_DIR \
  --save_dir results/opirl/swimmer
