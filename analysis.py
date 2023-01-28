from negatives import words

article = ""

negative_score = 0
for word in words:
    if word in article:
        negative_score += 1
