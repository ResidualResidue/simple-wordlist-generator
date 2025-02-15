import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
                        prog='simple-wordlist-generator',
                        description='DO NOT USE FOR ILLEGAL PURPOSES. ETHICAL SECURITY PROFESSIONALS ONLY. Super simple wordlist generator for security researchers. Aggregate and l33tify wordlists, mainly geared towards small, specially currated wordlists for use over networks with rate limitting or account lockouts!',
                    )
    
    parser.add_argument('-f', '--input-files', action='store', nargs='+', required=True)
    parser.add_argument('-l', '--l33tify', action='store_true')
    parser.add_argument('-o', '--out-file', action='store')

    args=parser.parse_args()

    return args