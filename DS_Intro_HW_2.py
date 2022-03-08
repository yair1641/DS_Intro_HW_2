
def check_input(sentence, reverse_word):
    if type(reverse_word) != str:
        return False
    for word in sentence:
        if type(word) != str:
            return False
    return True


def check_match(sentence, reverse_word):
    for word in sentence:
        if reverse_word == word:
            return True
    return False


def reverse(sentence, reverse_word):
    sentence = sentence.split()
    tmp_sentence = ''
    match_flag = False
    if not check_input(sentence, reverse_word):
        return "invalid input"
    if not check_match(sentence, reverse_word):
        return "no match word found"
    for word in sentence:
        if word == reverse_word and not match_flag:
            match_flag = True
            tmp_sentence += reverse_word[::-1]
            tmp_sentence += ' '
        else:
            tmp_sentence += word
            tmp_sentence += ' '
    return str(tmp_sentence)


print(reverse("i like milk and i like banana", "like"))