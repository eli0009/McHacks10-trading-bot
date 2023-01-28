with open("negative_words.txt") as fp:
    with open("negatives.py", "w") as outfp:
        for x in fp.readlines():
            print(f'"{x.strip()}",', file=outfp)
