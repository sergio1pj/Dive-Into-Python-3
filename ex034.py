message = input(">")
words = message.split(" ")

emojis = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😂",
    ":P": "😛",
    ";)": "😉",
    ":O": "😮",
    ":*": "😗",
    ":|": "😐",
    ":/": "😕",
    ":\\": "😕",
    ":@": "😠",
    ":$": "😳",
    ":^": "😳",
    ":S": "😳",
    ":3": "😳",
    ":X": "😳",
    ":*": "😗"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)