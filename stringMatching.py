
def findCount (text, keyWord):
    count = 0
    for i in range (len (text)-len (keyWord)+1):        # no need to check till the end of the string
        if text [i] == keyWord [0]:                     # check each char with the first character of the keyword
            for j in range (1, len (keyWord)):          # if a match is found, check other charcters of the keyword
                if text [i+j] == keyWord [j]:
                    if j == len (keyWord)-1:            # if last character of the keyword is matched, count is increased by 1
                        count = count + 1
                
                else:                                   # if a middle character of the keyword is mismatched, 
                    break                               # go to the next character of the string (text)
                

    return count


#text = "In the convential world, it won't ever happen"
#keyWord = 'lD,'

text = input ()
keyWord = input ()

#text = ''.join (text)

count = findCount (text, keyWord)

print (count)