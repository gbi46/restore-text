from nltk.corpus import words as nltk_words
from itertools import permutations

import nltk, re

nltk.download('punkt', quiet=True)
nltk.download('words', quiet=True)

WORDS = set(word.lower() for word in nltk_words.words())

def is_valid_word(word):
    """
    Check if a word is valid by checking against the NLTK words corpus.
    """
    return word.lower() in WORDS


def generate_variants(word):
    """
    Generate all possible valid variants of a word.
    """
    candidates = []
    pattern = word.replace('*', '.')
    regex = re.compile(f'^{pattern}$', re.IGNORECASE)
    for dict_word in WORDS:
        if len(dict_word) == len(word) and regex.match(dict_word):
            candidates.append(dict_word)
    return candidates


def is_anagram_of_valid_word(word):
    """
    Check if any permutation of a word is a valid English word.
    Only used for short words (up to 7 letters).
    """
    if len(word) > 7:
        return False
    for perm in set(permutations(word)):
        candidate = ''.join(perm)
        if candidate.lower() in WORDS:
            return candidate
    return False


def restore_text(text):
    """
    Restore text by replacing invalid words with valid variants or permutations.
    """

    if len(text) == 0:
        print("Text is empty.")
        return None
    elif len(text) < 200:
        print("Text is too short to process. Please provide a text with minimum 200 symbols.")
        return None
    elif len(text) > 500:
        print("Text is too long to process. Please provide a text with maximum 500 symbols.")
        return None

    restored = []
    idx = 0
    max_len = 20

    while idx < len(text):
        found = False
        for end in range(min(len(text), idx + max_len), idx + 1, -1):
            word = text[idx:end]

            # Без зірочок
            if "*" not in word and is_valid_word(word):
                restored.append(word)
                idx = end
                found = True
                break

            # Зірочки
            if "*" in word:
                candidates = generate_variants(word)
                if candidates:
                    restored.append(sorted(candidates, key=lambda w: -len(w))[0])
                    idx = end
                    found = True
                    break

            # Анаграмми
            if "*" not in word and len(word) <= 7:
                candidate = is_anagram_of_valid_word(word)
                if candidate:
                    restored.append(candidate)
                    idx = end
                    found = True
                    break

        if not found:
            restored.append(text[idx])
            idx += 1

    return ' '.join(restored)