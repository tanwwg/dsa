
def read_lines():
    lines = []
    while True:
        line = input()
        if line == "": break
        lines.append(line)
    return lines


lines = read_lines()
print(list(reversed(lines)))


