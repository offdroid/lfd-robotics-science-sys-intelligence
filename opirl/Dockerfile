FROM python:3.9.18-bookworm
RUN apt-get update && apt-get install curl git libosmesa6-dev patchelf -y
WORKDIR /app
COPY ./mujoco210-linux-x86_64.tar.gz /app/
RUN mkdir /mujoco -p && tar -xvf mujoco210-linux-x86_64.tar.gz -C /mujoco/ --no-same-owner
ENV MUJOCO_PY_MUJOCO_PATH=/mujoco/mujoco210
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mujoco/mujoco210/bin
ENV ENV PIP_ROOT_USER_ACTION=ignore
COPY . /app
RUN pip install -e . && pip install -r /app/requirements.txt && pip install 'gym[mujoco]<0.26' 'cython<3'
ENTRYPOINT ["python", "-u", "run_opirl.py"]
CMD ["--algo", "opirl", "--normalize_states", "--use_bc_reg", "--learn_alpha", "--seed", "1", "--max_timesteps", "1000000", "--env_name", "Swimmer-v2", "--expert_path_dir", "/app/experts/sac/swimmer/expert", "--save_dir", "results/opirl/swimmer"]
