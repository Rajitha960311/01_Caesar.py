alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(newtext):
    cyphertext = ""
    for char in newtext:
        if char in alpha:
            newpos = (alpha.find(char)+3)%26
            cyphertext += alpha[newpos]
        else:
            cyphertext += char
    return cyphertext
    

print("Enter New Text :")
newtext = input()
newtext = newtext.lower()
print(encrypt(newtext))
