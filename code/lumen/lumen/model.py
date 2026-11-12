import torch
import torch.nn as nn


class LatentUtilityModel(nn.Module):
    def __init__(self, dim=32):
        super().__init__()
        self.encoder = nn.Linear(dim, dim * 2)
        self.decoder = nn.Linear(dim * 2, dim)

    def forward(self, x):
        return self.decoder(self.encoder(x))
