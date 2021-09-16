import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Show me the args")

    parser.add_argument('--name', '-n',
                        help='Show your name',
                        default='Minsoo')

    parser.add_argument('--age',
                        help='Show your age',
                        default='27')

    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    print(args)
    print(f'name = {args.name}')
    print(f'age = {args.age}')