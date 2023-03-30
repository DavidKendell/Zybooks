strings = ["e|-", "B|-", "G|-", "D|-", "A|-", "E|-"]
chords = {"G": ["3-", "0-", "0-", "0-", "2-", "3-"],
          "C": ["0-", "1-", "0-", "2-", "3-", "--"],
          "D": ["2-", "3-", "2-", "0-", "--", "--"]
        }
numChords = int(input())
for i in range(numChords):
    chord = input()
    strings = [strings[i] + chords[chord][i] for i in range(6)]
for chord in strings:
    print(chord)
