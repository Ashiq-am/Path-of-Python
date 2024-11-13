def train(env, policy, optimizer, episodes=1000):
    for episode in range(episodes):
        state = env.reset()
        log_probs = []
        rewards = []
        done = False

        while not done:
            state = torch.FloatTensor(state).unsqueeze(0)
            probs = policy(state)
            m = Categorical(probs)
            action = m.sample()
            state, reward, done, _ = env.step(action.item())

            log_probs.append(m.log_prob(action))
            rewards.append(reward)
            # Inside the train function, after an episode ends:

            if done:
                episode_rewards.append(sum(rewards))
                discounted_rewards = compute_discounted_rewards(rewards)
                policy_loss = []
                for log_prob, Gt in zip(log_probs, discounted_rewards):
                    policy_loss.append(-log_prob * Gt)
                optimizer.zero_grad()
                policy_loss = torch.cat(policy_loss).sum()
                policy_loss.backward()
                optimizer.step()

                if episode % 50 == 0:
                    print(f"Episode {episode}, Total Reward: {sum(rewards)}")
                break

env = gym.make('CartPole-v1')
policy = PolicyNetwork()
optimizer = optim.Adam(policy.parameters(), lr=1e-2)

train(env, policy, optimizer)
