from helpers import collect_args, l33tify

args = collect_args.get_args()

l33tified_lines = l33tify.l33tify(args.input_files[0])

print(l33tified_lines)

