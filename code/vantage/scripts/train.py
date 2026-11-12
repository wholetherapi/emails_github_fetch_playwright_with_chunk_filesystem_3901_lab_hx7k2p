import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--config', default='configs/default.yaml')
    p.parse_args()
    print('training VANTAGE')

if __name__ == '__main__':
    main()
