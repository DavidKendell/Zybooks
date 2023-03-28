text = input()
nospace = [c for c in text.split(" ") if c != ""]
print(len(nospace))