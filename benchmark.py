import time

N = 3600
T = 100

env = torchcule.atari.Env('PongNoFrameskip-v4', N, device='cuda:0')

obs = env.reset()
start = time.time()
for _ in range(T):
    actions = torch.randint(env.action_space.n, size=(env.num_envs,), device='cuda')
    obs, reward, term, _ = env.step(actions)
print(f'{N*T/(time.time()-start):.0f} samples/sec')