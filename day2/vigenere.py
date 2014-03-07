import itertools


test_key = "REDDIT"
test_message = "TODAYISMYBIRTHDAY"

test_encoded = "ZEJFOKHTMSRMELCPODWHCGAW"
FREQUENT_WORDS = ["a", "about", "after", "all", "also", "an", "and",
                  "any", "as", "at", "back", "be", "because", "but", 
                  "by", "can", "come", "could", "day", "do", "even", 
                  "first", "for", "from", "get", "give", "go", "good", 
                  "have", "he", "her", "him", "his", "how", "I", "if", 
                  "in", "into", "it", "its", "just", "know", "like", 
                  "look", "make", "me", "most", "my", "new", "no", 
                  "not", "now", "of", "on", "one", "only", "or", "other", 
                  "our", "out", "over", "people", "say", "see", "she", 
                  "so", "some", "take", "than", "that", "the", "their", 
                  "them", "then", "there", "these", "they", "think", "this", 
                  "time", "to", "two", "up", "us", "use", "want", "way", "we", 
                  "well", "what", "when", "which", "who", "will", "with", 
                  "work", "would", "year", "you", "your"]


def get_position(char):
    return ord(char) - 65


def get_character(pos):
    return chr(pos + 65)


def encode(key, string):
    string_chars = list(string)
    key_chars = list(key)
    encoded_string = ""
    for idx, string_char in enumerate(string_chars):
        key_char = key_chars[(idx % len(key))]
        key_pos = get_position(key_char)
        string_pos = get_position(string_char)
        encoded_pos = (key_pos + string_pos) % 26
        encoded_string += get_character(encoded_pos)

    return encoded_string


def decode(key, encoded_string):
    encoded_chars = list(encoded_string)
    key_chars = list(key)
    decoded_string = ""
    for idx, encoded_char in enumerate(encoded_chars):
        key_char = key_chars[(idx % len(key))]
        key_pos = get_position(key_char)
        encoded_pos = get_position(encoded_char)
        decoded_pos = (encoded_pos - key_pos) % 26
        decoded_string += get_character(decoded_pos)
    return decoded_string


"""
Uses a list of the top 100 most frequent English words and prints a list of
decoded messages sorted by the frequency of common words in each decoded
message. Opting for brute force over frequency detection due to the short
message length.
"""


def brute_force(encoded_message, max_key_len):
    key_len = 1
    matches = {}
    while key_len <= max_key_len:
        for key in itertools.imap(''.join, itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=key_len)):
            decoded = decode(key, encoded_message)
            for word in FREQUENT_WORDS:
                word = word.upper()
                if word in decoded:
                    current_val = 0
                    try:
                        current_val = matches[decoded]
                    except KeyError:
                        pass
                    matches[decoded] = current_val + 1
        key_len += 1

    sorted_matches = sorted(matches, key=lambda key: matches[key], reverse=True)

    for match in sorted_matches[:75]:
        print "%s: %s" % (matches[match], match)

encoded_msg = encode(test_key, test_message)
decoded_msg = decode(test_key, encoded_msg)
print "Encoded Message: %s\nDecoded Message: %s\n\nTop Brute Force Matches Containing Frequent English Words:" % (encoded_msg, decoded_msg)

brute_force(test_encoded, 5)

"""
Solution found by visually inspecting the returned 75 possible matches
"""

print "\nSolution: WELCOMETOPROBLEMOFTHEDAY"