import matplotlib.pyplot as plt
import numpy as np
import PyPDF2

# counting word frequency
def count_words(file_name):

    # reading pdf
    last_char = file_name[-1]
    if (last_char == 'f'):
        pdfFileObj = open(file_name, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        text = pageObj.extractText()
    # reading text file
    else: 
        file = open(file_name)
        text = file.read()
        file.close()

    # ignoring punctuation 
    for char in '~`—@#$%^&*(){}[]\|<>:;/!?-.,\n':
        text=text.replace(char,' ')
    text = text.lower()
    wlist = text.split()

    # breaking the text up
    word_frequency = [] # number of times a word has been mentioned
    word_list = [] # different words 
  
    # looping until all words separated
    for i in wlist:             
  
        # checking for the duplicacy
        if i not in word_list:
  
            # inserting word in list
            word_list.append(i) 
              
    for i in range(0, len(word_list)):
  
        # counting the frequency of each word 
        word_frequency.append(wlist.count(word_list[i]))

    # plotting a histogram 
    x = np.arange(len(word_list))
    plt.bar(x, height=word_frequency, width=0.99)
    plt.xticks(x, word_list)
    plt.title('Word Frequency in ' + file_name)
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.show()

    return word_list, word_frequency

def main():
    # testing .txt file
    word_list, word_frequency = count_words('test.pdf')
    print(word_list)
    print(word_frequency)

if __name__ == "__main__":
    main()
