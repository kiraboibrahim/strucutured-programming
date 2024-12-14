def get_last_name(person_name):
    SPACE_CHAR = " "
    if SPACE_CHAR not in person_name:
        return person_name
    space_char_index = person_name.index(SPACE_CHAR)
    return get_last_name(person_name[space_char_index+1: ])


person_name = input("Enter your full name: ")
last_name = get_last_name(person_name)

print(f"Last name is: {last_name}")
