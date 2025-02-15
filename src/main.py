from helpers import collect_args, wordlist_parser

args = collect_args.get_args()

wordlists=[]

for file in args.input_files:
    if(args.l33tify):
        l33tified_lines = wordlist_parser.l33tify(file)
        wordlists.append(l33tified_lines)
    else:
        mundane_lines = wordlist_parser.mundane_read(file)
        wordlists.append(mundane_lines)


print(wordlists)

