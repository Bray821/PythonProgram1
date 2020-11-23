def to_nato(words):

    list_of_words = []
    nato_alphabet = {
        
        "A":"Alfa",
        "a":"Alfa",
        "B":"Bravo",
        "b":"Bravo",
        "C":"Charlie",
        "c":"Charlie",
        "D":"Delta",
        "d":"Delta",
        "E":"Echo",
        "e":"Echo",
        "F":"Foxtrot",
        "f":"Foxtrot",
        "G":"Golf",
        "g":"Golf",
        "H":"Hotel",
        "h":"Hotel",
        "I":"India",
        "i":"India",
        "J":"Juliett",
        "j":"Juliett",
        "K":"Kilo",
        "k":"Kilo",
        "L":"Lima",
        "l":"Lima",
        "M":"Mike",
        "m":"Mike",
        "N":"November",
        "n":"November",
        "O":"Oscar",
        "o":"Oscar",
        "P":"Papa",
        "p":"Papa",
        "Q":"Quebec",
        "q":"Quebec",
        "R":"Romeo",
        "r":"Romeo",
        "S":"Sierra",
        "s":"Sierra",
        "T":"Tango",
        "t":"Tango",
        "U":"Uniform",
        "u":"Uniform",
        "V":"Victor",
        "v":"Victor",
        "W":"Whiskey",
        "w":"Whiskey",
        "X":"X-ray",
        "x":"X-ray",
        "Y":"Yankee",
        "y":"Yankee",
        "Z":"Zulu",
        "z":"Zulu",
        "!":"!",
        "?":"?",
        ".":".",
        ",":","
    }
    Final_Word = ""
    for i in words:
        if i in nato_alphabet:
            value_of_alpha = nato_alphabet[i]
            list_of_words.append(value_of_alpha)
    for i in list_of_words:
        Final_Word+= i+" "
    
    return Final_Word.strip()

print(to_nato("If, you can read!"))