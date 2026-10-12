alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def parse(text):
#   """Turn a pasted text like [[1, 2], [3]] into a nested list of ints."""
    words = text.replace(" ", "").strip("[]").split("],[")
    return [[int(n)for n in word.split(",")if n] for word in words]
def decode(transmission):
#  """Clean, decode and analyze one transmission."""
    cleaned = [[n for n in word if 4 <= n <= 29] for word in transmission]
    words = ["".join([alphabet[n - 4] for n in word]) for word in cleaned]
    message = " ".join(words)
    corrupted = [len([n for n in word if n < 4 or n > 29]) for word in transmission]
    return cleaned, words, message, corrupted 

'''
transmission = [    [18, 0, 19, 8, -2, 17],    
                    [99, 23, 11, 8],   
                    [10, 4, 55, 23, 8]
]
transmission_2 =[    [9, 12, -5, 17, 7],  
                    [14, 0, 8, 28, 100]
]
'''
'''
# Task 1: remove the noise
cleaned = [[n for n in word if 4 <= n <= 29] for word in transmission]

# Task 2: decode the words
decoded_words = ["".join([alphabet[n - 4] for n in word]) for word in cleaned]

# Task 3: reveal the message
message = " ".join(decoded_words)

# Task 4: signal diagnostics
corrupted = [len([n for n in word if n < 4 or n > 29]) for word in transmission]
'''
transmission = parse(input ("Paste the transmission: "))
cleaned, words, message, corrupted = decode(transmission)

print("Cleaned transmission")
print (cleaned)
print ("\nDecoded_words:")
print(words)
print("\nSecret message:")
print(message)
print("\nCorrupted values per word:")
print(corrupted)