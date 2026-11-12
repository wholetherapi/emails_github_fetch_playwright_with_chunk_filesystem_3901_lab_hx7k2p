import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--checkpoint', required=True)
    p.parse_args()
    print('evaluating VANTAGE')

if __name__ == '__main__':
    main()
