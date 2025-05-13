import numpy as np
import gymnasium as gym
import matplotlib.pyplot as plt
import os

# Discretize the continuous state space
pos_bins = np.linspace(-1.2, 0.6, 20)
vel_bins = np.linspace(-0.07, 0.07, 20)


def discretize(obs):
    pos, vel = obs
    pos_idx = np.digitize(pos, pos_bins) - 1
    vel_idx = np.digitize(vel, vel_bins) - 1
    return (pos_idx, vel_idx)


# Q-learning parameters
alpha = 0.1       # learning rate
gamma = 0.99      # discount factor
epsilon = 1.0     # initial exploration
min_epsilon = 0.01
decay_rate = 0.995

# Q-table: shape [position_bins x velocity_bins x actions]
q_table = np.zeros((len(pos_bins), len(vel_bins), 3))

# Training loop
#env = gym.make("MountainCar-v0", render_mode="human")
env = gym.make("MountainCar-v0")
episodes = 10000
max_positions = []
steps_per_episode = []

for ep in range(episodes):
    obs, _ = env.reset()
    state = discretize(obs)
    done = False
    max_pos = obs[0]
    steps = 0

    while not done:
        # Epsilon-greedy action selection
        if np.random.random() < epsilon:
            action = np.random.choice(3)
        else:
            action = np.argmax(q_table[state])

        next_obs, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        next_state = discretize(next_obs)

        # Q-learning update
        best_next_action = np.argmax(q_table[next_state])
        q_table[state][action] += alpha * (
            reward + gamma * q_table[next_state][best_next_action] - q_table[state][action]
        )

        state = next_state
        max_pos = max(max_pos, next_obs[0])
        steps += 1

    # Decay epsilon
    epsilon = max(min_epsilon, epsilon * decay_rate)

    # Record stats
    max_positions.append(max_pos)
    steps_per_episode.append(steps)

    # Print progress
    if (ep + 1) % 500 == 0:
        print(f"Episode {ep+1}: Max position = {max_pos:.4f}, Steps = {steps}, Epsilon = {epsilon:.4f}")

env.close()


# Moving average for smoother plots
def moving_average(data, window_size=50):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')


# Plot: Max X Position
plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.plot(max_positions, color='gray', alpha=0.3)
plt.plot(moving_average(max_positions), color='blue')
plt.title("Max X Position per Episode")
plt.xlabel("Episode")
plt.ylabel("Max X Position")

# Plot: Steps per Episode
plt.subplot(1, 2, 2)
plt.plot(steps_per_episode, color='gray', alpha=0.3)
plt.plot(moving_average(steps_per_episode), color='green')
plt.title("Steps per Episode")
plt.xlabel("Episode")
plt.ylabel("Number of Steps")

# Save graphs
os.makedirs("graphs", exist_ok=True)
plt.savefig("graphs/training_progress.png")
# plt.show()

