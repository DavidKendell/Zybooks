caption = input()
if caption[-1] == ",":
    caption = caption[:-1] + "."
if caption[-2:] == ".." and caption[-3:] != "...":
    caption = caption[:-1]
print(caption)