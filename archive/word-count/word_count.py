def word_count(phrase):

    words_dict = {}
    words = phrase.lower().split()
    output = ''
    
    for word in words:
        for ch in word:
            if ch.isalnum():
                output += ''.join(ch).strip()
            elif ch == word[-1]:
                output += ''
            else:
                output += ' '

        print("Output: " + output)
        if output:
            words_dict[output] = words_dict.get(output, 0) + 1
        output = ''
    return words_dict