import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
                        prog='ProgramName',
                        description='What the program does',
                        epilog='Text at the bottom of help')
    parser.add_argument('to_output')
    parser.add_argument('-v', '--verbose', action='store_true')

    args=parser.parse_args()

    return args