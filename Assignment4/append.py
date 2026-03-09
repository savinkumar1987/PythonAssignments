with open("output.txt", 'wt') as fh: # open output.txt in write mode
    text_write = input("Enter text to write to the file: ")
    fh.write(text_write)
    print("data successfully written to output.txt")

with open("output.txt", 'at') as fh1: # open output.txt in append mode
     text_append = input("Enter Additional text to append: ")
     fh1.write(f"\n{text_append}")
     print("Data successfully appended")

with open("output.txt",'rt') as fh2: # open output.txt in read mode
    print("Final content of output.txt")
    lines = fh2.readlines()
    for line in lines:
        print(f"{line.rstrip('\n')}")


