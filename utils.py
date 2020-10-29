def format_int(i, separator=" "):
    number = str(i)[::-1]
    final_str = ""
    for index in range(len(i)):
        current_char = number[index]
        if index%3 == 0 and index != 0:
            current_char += separator
        final_str = current_char+final_str
    return final_str