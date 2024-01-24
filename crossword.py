def word_finder():
    
    import pandas as pd
    import numpy as np

    df = pd.read_csv(------------- PATH TO THE FILE -----------------)
    df = df["Words"].unique()

    countx = 0
    words_list = []
    user = int(input("Length of the character: "))


    for i in df:
        try:
            if len(i) == user:
                words_list.append(i)
        except:
            pass


    while countx < user:
        question = input("Do you know the ª character? -> ")
        if question == "N":
            countx += 1
        else:
            
            for y in words_list[:]:
                if y[countx] != question:
                    words_list.remove(y)
            
            countx += 1
    
    print(words_list)


word_finder()


