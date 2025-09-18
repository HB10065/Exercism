"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.
 
    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return 'un' + word

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.
 
    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.
 
    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.
 
    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    new_str = vocab_words[0]
    prefix = new_str
    for word_i in range(1, len(vocab_words)):
        new_str += ' :: ' + prefix + vocab_words[word_i]

    return new_str

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.
 
    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.
 
    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    new_str = word[:-4]
    if (new_str[len(new_str) - 1] == 'i' and new_str[len(new_str) - 2] not in 'aeiou'):
        new_str = new_str[:-1] + 'y'

    return new_str

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.
 
    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.
 
    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    listed_sentence = sentence.split()
    changed_word = listed_sentence[index]
    if index == -1:
        changed_word = changed_word[:-1] + 'en'
    else:
        changed_word += 'en'
    
    return changed_word
