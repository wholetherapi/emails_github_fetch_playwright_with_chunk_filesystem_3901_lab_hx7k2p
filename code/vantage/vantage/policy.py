import torch
import torch.nn as nn


class VantagePolicy(nn.Module):
    def __init__(self, obs_dim=64, act_dim=4):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(obs_dim, 128), nn.ReLU(), nn.Linear(128, act_dim))

    def forward(self, obs):
        return self.net(obs)
