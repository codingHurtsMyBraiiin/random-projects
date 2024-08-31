def modify(orig_char, new_char, orig_str):
    new_str = ""

    for i in orig_str:

        if i == orig_char:
            new_str += new_char
        else:
            new_str += i
    
    return new_str

print(modify("o", "w", "LeroyJenkins"))
