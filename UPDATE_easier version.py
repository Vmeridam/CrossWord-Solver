def word_finder():
    
    import pandas as pd
    import numpy as np

    df = pd.read_csv(-------------------------PATH----------------------)
    df = df["Words"].unique()

    countx = 0
    words_list = []
    user = input("Just type the words you know; words you don´t write - ;Example: h-llo -> hello :: -> ")


    for i in df:
        try:
            if len(i) == len(user):
                words_list.append(i)
        except:
            pass


    while countx < len(user):
        
        user_ch_division = list(user)
        
        for y in user_ch_division:
            
            if y == "-":
                countx += 1
            else:
                for z in words_list[:]:
                    if z[countx] != y:
                        words_list.remove(z)
                
                countx += 1
    
    print(words_list)

word_finder()
