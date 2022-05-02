# Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
# Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
# Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

def top_3_words(text):
    illegals = ';/_?,.:!-'
    text_lower = text.lower()
    for char in illegals:
        text_lower = text_lower.replace(char, ' ')
    # 2
    words: list = [word for word in text_lower.split() if word.replace("'", '') != '']
    processed = set()
    # 3
    counters: dict = dict()
    for word in words:
        if word not in processed:
            processed.add(word)
            counter = words.count(word)
            if counter in counters:
                counters[counter].append(word)
            else:
                counters[counter] = [word]
    # 4
    results: list = list()
    n = 3
    keys = sorted(counters.keys(), reverse=True)
    for counter in keys:
        diff = n - len(results)
        results += counters[counter][:diff]

        if len(results) == 3:
            break

    return results
    return
