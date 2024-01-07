#!/bin/bash

EXPERT_PATH_DIR="experts/sac/hopper/expert"

python -u run_opirl.py \
  --algo opirl \
  --use_bc_reg \
  --normalize_states \
  --learn_alpha \
  --seed 2 \
  --max_timesteps 1000000 \
  --env_name Hopper-v2 \
  --expert_path_dir $EXPERT_PATH_DIR \
  --save_dir results/opirl/hopper
