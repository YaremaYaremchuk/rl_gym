import gym
import numpy as np
import cv2
import matplotlib.pyplot as plt

env = gym.make("MountainCar-v0", render_mode = 'rgb_array')
env.metadata['render_fps'] = 60


learning_rate = 0.1
discount = 0.95
eps = 25000

view_step = 500

epsilon = 0.5
start_decay = 1
end_decay = eps // 2
epsilon_decay = epsilon/(end_decay - start_decay)

obs_size = [40] * len(env.observation_space.high)
obs_win = (env.observation_space.high - env.observation_space.low) / obs_size
q_tab = np.random.uniform(low=-2, high=0, size=(obs_size + [env.action_space.n]))

eps_rews = []
ag_eps_rews = {'ep':[], 'avg': [], 'min':[], 'max': []}


def get_state(state):
    discrete_state = (state - env.observation_space.low) / obs_win
    return tuple(discrete_state.astype(int))




for episode in range(eps):
    eps_reward = 0
    if episode % view_step == 0:
        print(episode)
        rend = True
    else:
        rend = False

    state, info = env.reset()
    ds_state = get_state(state)
    done = False
    while not done:
        if np.random.random() > epsilon:
            action = np.argmax(q_tab[ds_state])
        

        else:
            action = np.random.randint(0, env.action_space.n)
        
        
        new_state, reward, term, trun, _ = env.step(action)
        eps_reward += reward

        new_ds_state = get_state(new_state)

        if(rend):
            img = cv2.cvtColor(env.render(), cv2.COLOR_RGB2BGR)
            cv2.imshow("test", img)
            cv2.waitKey(50)

        if not(term or trun):
            max_fut_q = np.max(q_tab[new_ds_state])
            cur_q = q_tab[ds_state + (action, )]

            new_q = (1-learning_rate) * cur_q + learning_rate *(reward + discount * max_fut_q) 
            q_tab[ds_state + (action, )] = new_q
        else:
            if new_state[0] >= env.goal_position :
                print("LES GO " + str(episode))
                q_tab[ds_state + (action, )] = 0
            done = True
            

        

        ds_state = new_ds_state

    if end_decay >= episode >= start_decay:
        epsilon -= epsilon_decay

    eps_rews.append(eps_reward)

    if episode % 10 == 0:
        np.save(f"tables/{episode}-qtable.npy", q_tab)
    if not episode % view_step:
        average_rew = sum(eps_rews[-view_step:])/len(eps_rews[-view_step:])
        ag_eps_rews['ep'].append(episode)
        ag_eps_rews['avg'].append(average_rew)
        ag_eps_rews['min'].append(min(eps_rews[-view_step:]))
        ag_eps_rews['max'].append(max(eps_rews[-view_step:]))

        print(f" Episode: {episode}, AVG: {average_rew}, MIN: {min(eps_rews[-view_step:])}, MAX: {max(eps_rews[-view_step:])}")

env.close()

plt.plot(ag_eps_rews['ep'], ag_eps_rews['avg'], label="avg")
plt.plot(ag_eps_rews['ep'], ag_eps_rews['min'], label="min")
plt.plot(ag_eps_rews['ep'], ag_eps_rews['max'], label="max")
plt.legend(loc=4)
plt.show()