# coding: utf-8

import numpy as np

n_states = 500 # for Taxi-v3
n_actions = 6 # for Taxi-v3

def select_elites(states_batch, actions_batch, rewards_batch, percentile=50):
    """
    Select states and actions from games that have rewards >= percentile
    :param states_batch: list of lists of states, states_batch[session_i][t]
    :param actions_batch: list of lists of actions, actions_batch[session_i][t]
    :param rewards_batch: list of rewards, rewards_batch[session_i]

    :returns: elite_states,elite_actions, both 1D lists of states and respective actions from elite sessions

    Please return elite states and actions in their original order
    [i.e. sorted by session number and timestep within session]

    If you are confused, see examples below. Please don't assume that states are integers
    (they will become different later).
    """
    elite_states = []
    elite_actions = []
    #elites = [elite_states, elite_actions]
    percentile_value = np.percentile(rewards_batch, percentile)
    for i in range(len(rewards_batch)):
        if rewards_batch[i] >= percentile_value:
            elite_states += states_batch[i]
            elite_actions += actions_batch[i]
    return elite_states, elite_actions

def update_policy(elite_states, elite_actions, n_states, n_actions):
    """
    Given old policy and a list of elite states/actions from select_elites,
    return new updated policy where each action probability is proportional to

    policy[s_i,a_i] ~ #[occurences of si and ai in elite states/actions]

    Don't forget to normalize policy to get valid probabilities and handle 0/0 case.
    In case you never visited a state, set probabilities for all actions to 1./n_actions

    :param elite_states: 1D list of states from elite sessions
    :param elite_actions: 1D list of actions from elite sessions

    """
    #never_visited_state_policy = [1./n_actions] * n_actions
    #new_policy = []
    new_policy = np.ones((n_states, n_actions)) / n_actions
    from collections import defaultdict, Counter
    state_actions = defaultdict(list)
    for state, action in zip(elite_states, elite_actions):
        state_actions[state].append(action)
    for state, actions_list in state_actions.items():
        if state < n_states:
            action_counts = Counter(actions_list)
            for action in range(n_actions):
                if action in action_counts:
                    new_policy[state, action] = action_counts[action] / len(actions_list)
                else:
                    new_policy[state, action] = 0.0
            row_sum = new_policy[state, :].sum()
            if row_sum > 0:
                new_policy[state, :] /= row_sum
            else:
                new_policy[state, :] = 1.0 / n_actions
    return new_policy

#def generate_session(policy, t_max=int(10**4)):
def generate_session(env, policy, t_max=int(10**4)):
    """
    Play game until end or for t_max ticks.
    :param policy: an array of shape [n_states,n_actions] with action probabilities
    :returns: list of states, list of actions and sum of rewards
    """
    n_actions = policy.shape[1]
    states, actions = [], []
    total_reward = 0.

    s, info = env.reset()

    for t in range(t_max):
        # your code here - sample action from policy and get new state, reward, done flag etc. from the environment
        a = np.random.choice(np.arange(n_actions), p=policy[s])
        new_s, r, done, truncated, info = env.step(a)
        assert new_s is not None and r is not None and done is not None
        assert a is not None
        # your code here
        # Record state, action and add up reward to states,actions and total_reward accordingly.
        states.append(s)
        actions.append(a)
        total_reward += r

        s = new_s
        if done:
            break
    return states, actions, total_reward
