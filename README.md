# LfD

The `opirl` folder contains the code from `https://github.com/sff1019/opirl` and `rl-baselines3-zoo` is from `https://github.com/DLR-RM/rl-baselines3-zoo`.
`opirl/mujoco210-linux-x86_64.tar.gz` is from `https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz`.

Make sure to have followed the installation instructions found in both repositories!
Should you encounter issues use Docker or verify that the installation, as done in the Dockerfile, works on your system.

The expert trajectories are already generated and found in `opirl/experts/sac/swimmer/expert/`.
To generate them yourself, first download the the model
```
# from the `rl-baselines3-zoo` folder
python -m rl_zoo3.load_from_hub --algo sac --env Swimmer-v3 -orga sb3 -f logs/
```
Then run
```
python generate_expert_trajectories.py
```
from the same directory.
This will create 16 trajectories in `opirl/experts/sac/swimmer/expert/`.

For Docker run the following commands inside the `opirl` folder
```
docker build -t opirl .
docker run -v "/path/to/results/on/local/machine:/app/results" -it --rm opirl --algo opirl --normalize_states --use_bc_reg --learn_alpha --seed 1 --max_timesteps 1000000 --env_name Swimmer-v2 --expert_path_dir /app/experts/sac/swimmer/expert --save_dir results/opirl/swimmer
```
Be sure to update the `/path/to/results/on/local/machine` to where ever you want the results to be written to (absolute path!).
Run with different seeds to test robustness.


Without docker use
```
python -u run_opirl.py --algo opirl --normalize_states --use_bc_reg --learn_alpha --seed 1 --max_timesteps 1000000 --env_name Swimmer-v2 --expert_path_dir experts/sac/swimmer/expert --save_dir results/opirl/swimmer
```
from the `opirl` directory.
Alternatively, use the script in `opirl/scripts`.

The results are found in the results directory.
Most interesting is the `eval.csv` file which contains the policy evaluations during regular intervals of the training.

Plot the results using `plot.py`. Update the path to the results first, if necessary.
Requires `pip install seaborn pandas`.
