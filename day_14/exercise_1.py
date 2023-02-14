def formated_name(f, m, l=""):
    if l: 
        f_n = F"{f} {m} {l}"
    else:
        f_n = F"{f} {m}"
    return f_n.title()
print(formated_name("babangida", "adam", "sani"))
