# Galen

Official implementation of "Galen: Grounded Layout Generation for Scientific
Figures".

## What is included

- `galen/` - grounding encoder and constrained layout solver
- `experiments/` - training and evaluation entry points
- `results/` - released result tables and plotting helpers

## Quick start

```bash
pip install -r requirements.txt
python experiments/train_galen.py --config configs/base.yaml
python experiments/evaluate_chi.py --checkpoint runs/galen/best.pt
```

## Citation

If you use this code, please cite:

> Raman, P., Okafor, S., and Sanders, D. Galen: Grounded Layout Generation for
> Scientific Figures. Under review at ACM CHI 2026.
