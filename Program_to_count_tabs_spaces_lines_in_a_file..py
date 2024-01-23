file=input("Enter the file name:")
with open (file) as f:
    text=f.read()
    space=0
    tab=0
    line=0
    for char in text:
        if char==" ":
            space+=1
        elif char=="\t":
            tab+=1
        elif char=="\n":
            line+=1
