This is the environment bit of [CuLE](https://github.com/NVlabs/cule/), bundled up into 
a conda package. Install it with
```
conda install torchcule -c ajones -c pytorch -c default -c conda-forge
```
Limitations are that it drags a bit of conda-forge in with it when you install it elsewhere (urgh), and I've only
compiled it for my architecture. If you want to build it yourself,
```
conda-build pkg -c pytorch -c default -c conda-forge
```
This'll likely take ~30 min. You can test it out on a handful of envs by adding the `--fastbuild` switch to `build.sh`.

I do my building and testing in a [docker container](./docker), which is a version of my standard development env.

## Credit
All the code in here is from the Nvidia CuLE project. If you use this work, you should [cite their paper](https://arxiv.org/abs/1907.08467):
```
@misc{dalton2019gpuaccelerated,
   title={GPU-Accelerated Atari Emulation for Reinforcement Learning},
   author={Steven Dalton and Iuri Frosio and Michael Garland},
   year={2019},
   eprint={1907.08467},
   archivePrefix={arXiv},
   primaryClass={cs.LG}
}
```