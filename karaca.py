# My answer
def encrypt_me(word):
    karaca_codes = {'a': '0',
        'e': '1',
        'i': '2',
        'o': '2',
        'u': '3'
        }
    word_list = list(word[::-1])
    for number, value in enumerate(word_list):
        if value in karaca_codes:
            word_list[number] = karaca_codes[value]
        else:
            pass
    return "".join(word_list) + "aca"

# A user named zatoichi49
def encrypt_short(word):
    return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'

# 2nd top
def encrypt_dm(word):
    v= {'a':'0','e':'1','o':'2','u':'3'}
    return ''.join(v[i] if i in v else i for i in word[::-1]) +'aca'

# 3rd one using replace()
def encrypt_pj(word):
    for r in (('a', '0',), ("e", "1"), ("o", "2"), ("u", "3")):
        word = word.replace(*r)

    return word + 'aca'
