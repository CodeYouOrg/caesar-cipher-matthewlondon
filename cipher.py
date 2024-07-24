# add your code here
def get_input():
    sentence_input = input("Please enter a sentence:")
    return sentence_input

def cipher(sentence_input):
    i = 0
    while i < len(sentence_input):
        cipher_sentence = []
        if sentence_input[i].isalpha():
            cipher_sentence.append(sentence_input[i])
            i += 1
        else:
            cipher_sentence.append("")
            i += 1
    return cipher_sentence
    

def main():
    sentence = get_input()


main()