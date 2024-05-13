text = "Christiano Ronaldo"


def reverse_string(text:str):
    col_of_chars = list(text)
    reversed_text = []
    while len(col_of_chars)!=0:
        reversed_text.append(col_of_chars.pop())
    return "".join(reversed_text)


print(reverse_string(text))
    