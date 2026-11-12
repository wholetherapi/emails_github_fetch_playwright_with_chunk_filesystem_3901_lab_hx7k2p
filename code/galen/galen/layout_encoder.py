import torch
import torch.nn as nn


class LayoutEncoder(nn.Module):
    def __init__(self, hidden_dim=256):
        super().__init__()
        self.proj = nn.Linear(768, hidden_dim)
        self.norm = nn.LayerNorm(hidden_dim)

    def forward(self, tokens):
        return self.norm(self.proj(tokens))
