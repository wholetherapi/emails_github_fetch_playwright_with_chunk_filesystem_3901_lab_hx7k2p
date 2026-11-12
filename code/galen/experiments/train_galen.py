import argparse
import torch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='configs/base.yaml')
    args = parser.parse_args()
    print('training Galen with', args.config)

if __name__ == '__main__':
    main()
