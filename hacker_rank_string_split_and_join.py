def split_and_join(line):
    line_split=line
    line_split = line_split.split(' ')
    line_split="-".join(line_split)
    print(line_split)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
