import io

def l33tify(file: str) -> list:
    l33tified_lines = []
    with open(file) as input_file:
        for line in input_file:
            l33tified_lines.append(line + '1337')

    return l33tified_lines

def mundane_read(file: str) -> list:
    mundane_lines = []
    with open(file) as input_file:
        for line in input_file:
            mundane_lines.append(line)
    
    return mundane_lines