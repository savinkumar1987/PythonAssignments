try:
    with open("sample.txt",'rt') as fh: # open sample.txt in read mode
        lines = fh.readlines()
        count = 0
        for line in lines: # for loop for print line by line
            count += 1
            print(f"Line {count}: {line.rstrip('\n')}")
except FileNotFoundError:
    print(f"Error : The file 'sample.txt' not found")
