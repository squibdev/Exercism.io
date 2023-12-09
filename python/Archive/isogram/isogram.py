def is_isogram(string):

    string = string.lower()
   
    output = True

    for ch in string:
        if ch.isalnum():
            count = string.count(ch)
            if count > 1:
                output = False
                return output

    return output