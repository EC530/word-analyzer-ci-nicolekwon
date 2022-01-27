# word-analyzer-ci-nicolekwon

> This ReadMe details Nicole Kwon's Project 1 for EC530. 

---


## Table of Contents


- [Descriptions of Project and Phases](#descriptions)
- [Explanations of Code Set-Up and Layout](#explanations)

---

## Descriptions

#### Project

The exercise application mission behind this project is to analyze a document. Specifically, the user stories are reading text files and creating histograms of all the word frequencies in documents.

Optional functionalities that were added include reading PDF files and displaying the histograms. 

#### Phases

Phase 1:   (Due 1/23)
- [x] Study [GitHub Actions](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
- [x] Define your programming rules and styles
- [x] Develop Github actions and implement your rules using preferred linter (flake8)
- [x] Develop the main console application or stub function

Phase 2:  (Due 1/27)
- [x] Complete basic functionality
- [x] Define unit tests for your program and implement example console application and one test

Phase 3:  (Due 1/30)
- [x] Implement your test programs and integrate them in GitHub actions
- [ ] Complete and deliver homework

---

## Explanations

#### Set-Up 

1. Clone the Github repository onto your local machine. 
2. Download [Python3](https://www.python.org/downloads/) if not installed already.
3. Open Terminal and run the following commands: 

| Command | Purpose |
| --- | --- |
| `pip3 install matplotlib` | Package used for displaying the histogram |
| `pip3 install PyPDF2` | Package used for reading a PDF |
| `python3 analyzer.py` | Line used for running the program |

4. If you want to analyze the PDF instead of the text file, change 'test.txt' to 'test.pdf' in the following line of analyzer.py:

```
word_list, word_frequency = count_words('test.txt')
```

#### Layout

- python-package.yml: Contains the workflow for Github Actions, allowing for continuous integration of programming rules/styles, linting, and unit testing
- requirements.txt: Specifies prerequisites of the different dependencies used in the code
- analyzer.py: Counts the frequency of all the words contained in a text or PDF file and displays a histogram
- test_analyzer.py: Runs 2 unit tests for reading and analyzing the word frequencies in test.txt and test.pdf

---

[Back to the Top](#word-analyzer-ci-nicolekwon)
