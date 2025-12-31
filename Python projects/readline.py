# tried replicate similar function created in C 
# from: https://github.com/awlog/past-practice/tree/main/C%20projects
# to practice logic

filename = input("File: ")
line_number = int(input("Line: "))

file = open(filename, "r")
lines = file.readlines()
file.close()
line = lines[line_number - 1].rstrip('\n')
print(line)