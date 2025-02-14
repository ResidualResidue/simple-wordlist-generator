import io

def l33tify(file: io.BytesIO) -> list:
    l33tified_lines = []
    with open(file) as input_file:
        for line in input_file:
            l33tified_lines.append(line)

    return l33tified_lines