import numpy as np
import torch
import torch.nn as nn

def to_one_hot(y_tensor, ndims):
    """ helper: take an integer vector and convert it to 1-hot matrix. """
    y_tensor = y_tensor.type(torch.LongTensor).view(-1, 1)
    y_one_hot = torch.zeros(
        y_tensor.size()[0], ndims).scatter_(1, y_tensor, 1)
    return y_one_hot


def predict_probs(states):
    """
    Predict action probabilities given states.
    :param states: numpy array of shape [batch, state_shape]
    :returns: numpy array of shape [batch, n_actions]
    """
    # convert states, compute logits, use softmax to get probability
    #torch.softmax()
    #np.soft
    

    # YOUR CODE GOES HERE
    # probs = None
    # batch_len = states.shape[0]
    # probs = np.zeros((batch_len, n_actions))
    # for i in range(batch_len):
    #     np.ndarray
    #     unique, counts = np.unique(states[i], return_counts=True)
    #     dict_counts = dict(zip(unique, counts))
    #     for a in range(n_actions):
    #         counts_sum = sum(dict_counts.values())
    #         if a in dict_counts.keys():
    #             probs[i, a] = dict_counts[a] / float(counts_sum)
    
    with torch.no_grad():
        logits = model(torch.FloatTensor(states))
        probs = torch.softmax(logits, dim=-1).numpy()

    assert probs is not None, "probs is not defined"
    return probs

def get_cumulative_rewards(rewards,  # rewards at each step
                           gamma=0.99  # discount for reward
                           ):
    """
    Take a list of immediate rewards r(s,a) for the whole session
    and compute cumulative returns (a.k.a. G(s,a) in Sutton '16).

    G_t = r_t + gamma*r_{t+1} + gamma^2*r_{t+2} + ...

    A simple way to compute cumulative rewards is to iterate from the last
    to the first timestep and compute G_t = r_t + gamma*G_{t+1} recurrently

    You must return an array/list of cumulative rewards with as many elements as in the initial rewards.
    """
    # YOUR CODE GOES HERE
    cumulative_rewards = [0] * len(rewards)
    def reccurent_g(t):
        result = 0
        if t == len(rewards) - 1:
            result = rewards[t]
        else:
            result = rewards[t] + gamma * reccurent_g(t+1)
        cumulative_rewards[t] = result
        return result
    if len(rewards) > 0:
        reccurent_g(0)

    assert cumulative_rewards is not None, "cumulative_rewards is not defined"
    return cumulative_rewards

def get_loss(states, actions, rewards, gamma=0.99, entropy_coef=1e-2):
    """
    Compute the loss for the REINFORCE algorithm.
    """
    states = torch.tensor(states, dtype=torch.float32)
    actions = torch.tensor(actions, dtype=torch.int32)
    cumulative_returns = np.array(get_cumulative_rewards(rewards, gamma))
    cumulative_returns = torch.tensor(cumulative_returns, dtype=torch.float32)

    # predict logits, probas and log-probas using an agent.
    logits = model(states)
    assert logits is not None, "logits is not defined"

    probs = torch.softmax(logits, dim=-1)#predict_probs(states)
    assert probs is not None, "probs is not defined"

    log_probs = torch.log_softmax(logits, dim=-1)
    assert log_probs is not None, "log_probs is not defined"

    assert all(isinstance(v, torch.Tensor) for v in [logits, probs, log_probs]), \
        "please use compute using torch tensors and don't use predict_probs function"

    # select log-probabilities for chosen actions, log pi(a_i|s_i)
    batch_len = states.shape[0]
    log_probs_for_actions = torch.zeros(batch_len) # [batch,]
    for i in range(batch_len):
        log_probs_for_actions[i] = log_probs[i,actions[i]]
    assert log_probs_for_actions is not None, "log_probs_for_actions is not defined"

    J_multiply_result = log_probs_for_actions * cumulative_returns
    J_hat = torch.sum(J_multiply_result) / torch.numel(J_multiply_result)# a number
    assert J_hat is not None, "J_hat is not defined"
    
    # Compute loss here. Don't forget entropy regularization with `entropy_coef`
    entropy = torch.sum(probs * log_probs, dim=-1).mean() * -1
    assert entropy is not None, "entropy is not defined"
    loss = 0 - J_hat - entropy_coef * entropy
    assert loss is not None, "loss is not defined"

    return loss
