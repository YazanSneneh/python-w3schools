
try:
    file = open('./text_file.txt')
    for line in file:
        print(line)
except FileNotFoundError:
    print("Please check file name or check if file exist")
finally:
    file.close()