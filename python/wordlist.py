import re

f = sorted(set( 
    list(filter(None,
        re.sub(r"[^a-z0-9\- ]", " ",
            " ".join(
                list(map(
                    lambda verse: " ".join(verse.split("--")[:-1]),
                    list(filter(
                        (".").__ne__,
                        open("src_files/nasb.txt", "r").read().splitlines()
                    ))
                ))
            ).lower()
        ).split(" ")
    ))
))

with open("src_files/nasb_list.txt", 'a+') as file:
    for word in f:
        file.write(word + '\n')