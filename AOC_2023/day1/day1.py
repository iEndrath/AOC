def make_list():
    list = []
    with open("input.txt", "r") as file:

        for line in file.readlines():

            list.append(line.strip())
    return list

list = make_list()

list_of_numbers = []

for i in list:
    first_number = ""
    last_number = ""
    for j in i:
        if j.isdigit():
            if first_number == "":
                first_number = j
            last_number = j
    full_number = first_number + last_number
    list_of_numbers.append(int(full_number))

print(sum(list_of_numbers))
