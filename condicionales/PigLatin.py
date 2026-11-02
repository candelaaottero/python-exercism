def translate(text):
    if (text[0] == "a" or text[0] == "e" or text[0] == "i" or text[0] == "o" or text[0] == "u" or 
       text[0:2] == "xr" or text[0:2] == "yt"):
        return text + "ay"

print(translate("xrja"))