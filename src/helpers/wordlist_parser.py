from itertools import product

def l33tify_string(line: str) -> list:
    l33t_map = {
        'a': ("4",),
        'b': ("8",),
        'e': ("3",),
        'i': ("1", "!"),
        'l': ("1",),
        'o': ("0",),
        's': ("5", "$"),
        'z': ("5",),
        't': ("7",)
    }

    # Create a list of lists where each character in the word has corresponding l33t equivalents or itself
    options = []
    for char in line:
        if char.lower() in l33t_map:  # Check if the character has l33t equivalents
            l33t_equivalents = l33t_map[char.lower()]
            options.append([char] + list(l33t_equivalents))
        else:
            options.append([char])  # Use the character as is if no l33t equivalent exists

    # Generate all combinations using Cartesian product
    permutations = [''.join(p) for p in product(*options)]

    return permutations
        

def l33tify(file: str) -> list:
    l33tified_lines = []
    with open(file) as input_file:
        for line in input_file:
            l33tified_lines += l33tify_string(line.strip())

    return l33tified_lines

def mundane_read(file: str) -> list:
    mundane_lines = []
    with open(file) as input_file:
        for line in input_file:
            mundane_lines.append(line.strip())
    
    return mundane_lines
