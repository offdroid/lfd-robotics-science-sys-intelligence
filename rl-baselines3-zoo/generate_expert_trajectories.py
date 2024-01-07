import time
import logging
import joblib
import gym
import numpy as np
from stable_baselines3 import SAC
from stable_baselines3.common.vec_env import VecVideoRecorder, DummyVecEnv

model = SAC.load("logs/sac/Swimmer-v3_1/Swimmer-v3.zip")


def main(model, episodes):
    episode_return = 0
    episode_timesteps = 0
    done = True

    total_timesteps = 0

    eval_returns = []

    # env = DummyVecEnv([lambda: gym.make("Swimmer-v3")])
    env = gym.make("Swimmer-v3")
    obs = None

    obses = []
    next_obses = []
    rews = []
    acts = []
    dones = []
    logp = []
    while len(eval_returns) < episodes:
        if done:
            obs, _ = env.reset()
            episode_return = 0
            episode_timesteps = 0

            joblib.dump(
                {"obs": obses, "next_obs": next_obses, "rew": rews, "act": acts, "done": dones, "logp": logp},
                f"../opirl/experts/sac/swimmer/expert/expert_00000000_epi_{len(eval_returns)}_return_0.0.pkl",
            )
            obses = []
            next_obses = []
            rews = []
            acts = []
            dones = []
            logp = []

        action, _ = model.predict(obs, deterministic=True)
        next_obs, reward, terminated, truncated, _ = env.step(action)
        obses.append(obs)
        next_obses.append(next_obs)
        rews.append(reward)
        acts.append(action)
        dones.append(np.array([done], dtype=float))
        logp.append(np.array([[0.0]], dtype=float))

        done = terminated or truncated
        if done:
            eval_returns.append(episode_return / episode_timesteps)

        episode_return += reward
        episode_timesteps += 1
        total_timesteps += 1

        obs = next_obs


main(model, 16)
