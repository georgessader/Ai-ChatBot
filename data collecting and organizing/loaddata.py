def onlySentence():
    n=0
    s=""
    s+="""{
        "intents": [
            """
    with open("data.txt", encoding='utf-8-sig') as file:
        for line in file:
            line=line.replace("\'","")
            line=line.replace("\"","")
            line=line.replace("\n","")
            if line=="" or line==" ":
                continue
            s+="""{
                "tag": """+str(n)+""",
                "patterns": 
                """+str(line.split(","))+"""
                ,
                "responses": [\""""+line+"""\"
                ]
            },"""
            n+=1
    s=s[:-1]
    s=s.replace("\'","\"")
    s=s.replace("\\x","")
    s+="""]
    }"""
    # print(s)

    with open("intents.json", "w", encoding='utf-8-sig') as text_file:
        text_file.write(s)


def sentenceWithWords():
    n=0
    s=""
    s+="""{
        "intents": [
            """
    with open("data.txt", encoding='utf-8-sig') as file:
        for line in file:
            line=line.replace("\n","")
            linlist=line.split(",")
            for i in range(len(linlist)):
                for j in range(len(linlist[i].split(" "))):
                    linlist.append(linlist[i].split(" ")[j])
            s+="""{
                "tag": \""""+str(n)+"""\",
                "patterns": 
                """+str(linlist)+"""
                ,
                "responses": [\""""+line+"""\"
                ]
            },"""
            n+=1
    s=s[:-1]
    s=s.replace("\'","\"")
    s+="""]
    }"""
    # print(s)

    with open("intents.json", "w", encoding='utf-8-sig') as text_file:
        text_file.write(s)



def sentenceWithWordsAdvance():
    n=0
    s=""
    s+="""{
        "intents": [
            """
    with open("data.txt", encoding='utf-8-sig') as file:
        for line in file:
            line=line.replace("\'","")
            line=line.replace("\"","")
            line=line.replace("\n","")
            if line=="" or line==" ":
                continue
            linlist=line.split(",")
            for i in range(len(linlist)):
                for j in range(len(linlist[i].split(" "))):
                    linlist.append(linlist[i].split(" ")[j])
            s+="""{
                "tag": \""""+str(n)+"""\",
                "patterns": 
                """+str(linlist)+"""
                ,
                "responses": [\""""+line+"""\"
                ]
            },"""
            n+=1
    s=s[:-1]
    s=s.replace("\'","\"")
    s+="""]
    }"""
    # print(s)

    with open("intents.json", "w", encoding='utf-8-sig') as text_file:
        text_file.write(s)

onlySentence()