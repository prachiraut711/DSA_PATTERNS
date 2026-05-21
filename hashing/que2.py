# Count Frequency of Characters in a String

def countFreq(s):
    freq = {}

    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for key in freq:
        print(key, "->", freq[key])


#here above already has print function so just call function as we not return anything . id we print below then it give output and then NONE
countFreq("apple")
countFreq("prachi")
countFreq("aaaa")