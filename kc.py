class Person:
    def __init__(self, name):
        self.name = name

list_of_people = [
    Person("Laila"),
    Person("Evander"),
    Person("Talia"),
    Person("Asha"),
]

#   in the list has a "name" property. For example, if
#   you did this, it would print out each name of the
#   Person instance.
#
#   for person in people:
#       print(person.name)

ßß
def names_in_list(names, people):

    result = []
    peoplenames = []

    for person in people:
        peoplenames.append(person.name)

    for name in names:
        result.append(name in peoplenames)

    return result


# def names_in_list_terra(names, people):
#     result = []
#     for name in names:
#         found_name = False
#         for person in people:
#             if person.name == name:
#                 found_name = True
#         if not found_name:
#             result.append(False)
#             print(name)
#             print(person.name)

#     return result



result = names_in_list(["Asha", "Azami", "Basia"], list_of_people)
print(result)
# prints [True, False, False]

result = names_in_list(["Asha", "Evander", "Laila"], list_of_people)
print(result)
# prints [True, True, True]

result = names_in_list([], list_of_people)
print(result)
# prints []

result = names_in_list(["Lina", "Anima"], list_of_people)
print(result)
# prints [False, False]
