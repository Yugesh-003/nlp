# Bigram Implementation Without Library

sentence = "I like mango I like apple banana orange I like"

word_list = sentence.split()

print("Words:", word_list)

# Find bigrams
print("\nBigram Probabilities:\n")

for i in range(len(word_list) - 1):

    pair = word_list[i] + " " + word_list[i + 1]

    pair_count = 0
    word_count = 0

    for j in range(len(word_list) - 1):
        if word_list[j] == word_list[i]:
            word_count += 1

        if word_list[j] == word_list[i] and word_list[j + 1] == word_list[i + 1]:
            pair_count += 1

    prob = pair_count / word_count

    print("Bigram:", pair)
    print("Frequency:", pair_count)
    print("First word frequency:", word_count)
    print("Probability:", round(prob, 2))
    print("-" * 25)