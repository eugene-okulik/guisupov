str_value = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, "
             "facilisis vitae semper at, dignissim vitae libero")
str_new = str_value.split()
suf = "ing"

res = []

for word in str_new:
    if word.endswith(","):
        # res.append(word[:-1] + a )
        res.append((word.replace(',', suf)) + ',')
    elif word.endswith("."):
        res.append((word.replace('.', suf)) + '.')
    else:
        res.append(word + suf)

print(' '.join(res))
