def replace(p_list, value_to_remove, value_to_add):
    for i, item in enumerate(p_list):
        if item == value_to_remove:
            p_list[i] = value_to_add

def main():
    with open("provinces.txt", "rt") as file:
        contents = []
        for line in file:
            contents.append(line.strip("\n"))

        contents.pop(0)
        contents.pop(-1)

        replace(contents, 'AB', "Alberta")

        print(contents)
        
        print(contents.count("Alberta"))

        
main()