from words import censoring_words_from_text, word_to_asterisks, word_existence_check, word_position, word_count_in_text, \
    check_word_list, check_text
import unittest

list_or_tuple = (tuple, list)


class TestWords(unittest.TestCase):

    def test_check_word_list(self):
        self.assertEqual(type(check_word_list(['Word', 'List'])), bool)

        with self.assertRaises(ValueError):
            check_word_list([])
        self.assertTrue(check_word_list(['Not', 'empty', 'now']))

        with self.assertRaises(ValueError):
            check_word_list({'word': 'word'})
        self.assertTrue(check_word_list(['Valid']))

        with self.assertRaises(ValueError):
            check_word_list([[], 'Lol', 'there', 'array'])
        self.assertTrue(check_word_list(['there', 'no', 'array', 'now']))

        with self.assertRaises(ValueError):
            check_word_list(['80085', 'nice!'])
        self.assertTrue(check_word_list(['must', 'be', 'str']))

    def test_check_text(self):
        self.assertEqual(type(check_text('Lorem zuggen dvain')), bool)

        with self.assertRaises(ValueError):
            check_text('')
        self.assertTrue(check_text('Not empty now'))

        with self.assertRaises(ValueError):
            check_text(5318008)
        self.assertTrue(check_text('String now'))

        with self.assertRaises(ValueError):
            check_text('   ')
        self.assertTrue(check_text('IRemoveWhiteSpacesJIC'))

    def test_word_to_asterisks(self):
        self.assertEqual(type(word_to_asterisks('word', 'word')), str)
        self.assertEqual(len(word_to_asterisks('word', 'word')), 4)
        self.assertEqual(word_to_asterisks('word', 'word'), '****')
        self.assertEqual(word_to_asterisks('word', 'wordie'), '****ie')
        self.assertEqual(word_to_asterisks('word', 'sword'), 's****')
        with self.assertRaises(ValueError):
            word_to_asterisks('drow', 'word')

    def test_word_existence_check(self):
        self.assertEqual(type(word_existence_check('word', 'word lorem')), bool)
        self.assertTrue(word_existence_check('word', 'word lorem'), True)
        self.assertFalse(word_existence_check('word', 'draw lorem'), False)
        self.assertTrue(word_existence_check('word', 'word word word'), True)
        self.assertTrue(word_existence_check('word', 'sword wordie'), True)

    def test_word_position(self):
        self.assertEqual(type(word_position('rd', 'worD lorem')), int)
        self.assertEqual(word_position('word', 'Word lord zord'), 0)
        self.assertEqual(word_position('word', '**** WORD ***'), 5)
        self.assertEqual(word_position('word', 'lord there word and word'), 11)

    def test_word_count_in_text(self):
        self.assertEqual(type(word_count_in_text('word', 'word word')), int)
        self.assertEqual(word_count_in_text('word', 'WORD word wordword sword, wordie wo/rd'), 6)
        self.assertEqual(word_count_in_text('word', "there no that thing that starts with 'w'"), 0)

    def test_censoring_words_from_text(self):
        self.assertEqual(type(censoring_words_from_text(['word'], 'text')), str)
        self.assertEqual(censoring_words_from_text(['Bad', 'Sad'], 'Bad and sad word'), '*** and *** word')
        self.assertEqual(censoring_words_from_text(['Bad', 'Sad'], 'Clean text'), 'Clean text')
        self.assertEqual(len(censoring_words_from_text(['Bad', 'Sad'], 'Another word')), 12)
        self.assertEqual(len(censoring_words_from_text(['Another', 'word'], 'Another word')), 12)
        with self.assertRaises(ValueError):
            censoring_words_from_text([], 'Yet another word')
        with self.assertRaises(ValueError):
            censoring_words_from_text(['no', 'Words'], '')
        with self.assertRaises(ValueError):
            censoring_words_from_text([], '')


if __name__ == '__main__':
    unittest.main()
