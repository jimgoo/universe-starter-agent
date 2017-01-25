"""
This will start Docker remote container viewed at localhost:5200
"""
import gym
import universe # register the universe environments

#envstr = 'flashgames.DuskDrive-v0'
#envstr = 'wob.mini.FocusText-v0'
#envstr = 'wob.mini.ClickButton-v0'
envstr = 'flashgames.PingPongSurvival-v0'

env = gym.make(envstr)
env.configure(remotes=1) # downloads and starts a flashgames runtime
observation_n = env.reset()

while True:
    #action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n] # your agent here
    action_n = [env.action_space.sample() for _ in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()
