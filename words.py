import re

_dataWords = ["Bad", "Sad", "Suck", "Con", "Dumb", "Voldemort"]
_dataText = "Du Bad hast sad mich gefragt dumb und bad ich hab con nichts sucker gesagt"

list_or_tuple = (tuple, list)


def word_to_asterisks(word, text):
    """Replaces letters from word, to asterisks"""
    if word_existence_check(word, text):
        position = word_position(word, text)
        return text[:position] + '*' * len(word) + text[position + len(word):]
    else:
        raise ValueError('You try to input wrong data')


def word_existence_check(word, text):
    """Checks if word exist in text in any Register"""
    if word.lower() in text.lower():
        return True
    else:
        return False


def word_position(word, text):
    """Gets word start position"""
    return text.lower().index(word.lower())


def word_count_in_text(word, text):
    return text.lower().count(word.lower())


def check_word_list(words_list):
    if not words_list:
        raise ValueError('Empty words list!')
    if type(words_list) not in list_or_tuple:
        raise ValueError('You try to put non list or tuple data!')
    for word in words_list:
        if type(word) is not str:
            raise ValueError('You try to put non str data in list of words!')
        if not word.isalnum():
            raise ValueError('Words can only contain a-z, A-Z symbols!')
    return True


def check_text(text):
    if not text:
        raise ValueError('Empty text!')
    if type(text) != str:
        raise ValueError('You try to put non str data!')
    if text.isspace():
        raise ValueError("Text can't be only with whitespaces!")
    return True


def censoring_words_from_text(words_list, text):
    """Gets list or tuple of banned words and text,
    then replaces words to asterisks, number of asterisks equal to word length"""
    if check_word_list(words_list) and check_text(text):
        censored_text = text
        for word in words_list:
            if word_existence_check(word, censored_text):
                for iteration in range(word_count_in_text(word, censored_text)):
                    censored_text = word_to_asterisks(word, censored_text)
        return censored_text
    else:
        raise ValueError('Wrong data')


if __name__ == '__main__':
    result = censoring_words_from_text(_dataWords, _dataText)
    print("Before processing - " + _dataText)
    print("After processing  - " + result)

