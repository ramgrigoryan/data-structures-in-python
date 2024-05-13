numbers1 = [2,5,1,2,3,5,1,2,4]
numbers2 = [2,1,1,2,3,5,1,2,4]
numbers3 = [2,3,4,5]

def first_recurring_number(numbers):
    already_meet_items = set()
    for i in numbers:
        if i in already_meet_items:
            print(already_meet_items)
            print(i)
            return i
        already_meet_items.add(i)
    print("No recurring numbers")
    return None

first_recurring_number(numbers1)

first_recurring_number(numbers2)

first_recurring_number(numbers3)

