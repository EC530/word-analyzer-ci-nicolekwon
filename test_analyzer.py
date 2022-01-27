import analyzer

expected_word_list_txt = ['i', 'have', 'been', 'one', 'acquainted',
                          'with', 'the', 'night', 'walked', 'out', 'in', 'rain', 'and', 'back']

expected_word_frequency_txt = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1]

expected_word_list_pdf = ['some', 'say', 'the', 'world', 'will', 'end', 'in', 'fire', 'ice']
expected_word_frequency_pdf = [2, 2, 1, 1, 1, 1, 2, 1, 1]

# Unit test for txt
def test_analyzer_txt():
    word_list_txt, word_frequency_txt = analyzer.count_words('test.txt')
    assert expected_word_list_txt == word_list_txt and expected_word_frequency_txt == word_frequency_txt

# Unit test for pdf
def test_analyzer_pdf():
    word_list_pdf, word_frequency_pdf = analyzer.count_words('test.pdf')
    assert expected_word_list_pdf == word_list_pdf and expected_word_frequency_pdf == word_frequency_pdf
