
def read_lines():
    lines = []
    try:
        while True:
            line = input()
            if line == "": break
            lines.append(line)
    except EOFError:
        pass
    return lines


lines = read_lines()
print(list(reversed(lines)))


