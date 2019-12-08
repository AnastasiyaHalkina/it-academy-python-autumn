import unittest
import all_def
import task1_3
import task1_2


class TestAddToListInDict(unittest.TestCase):
    def setUp(self) -> None:
        self.thedict = {
                        'list1': [1, 2],
                        'list2': [1, 2],
                        'list3': [1, 2]
                       }

    def test_add_element_inlist(self):
        result = task1_3.add_to_list_in_dict(self.thedict, 'list2', 3)
        self.assertEqual(result, {'list1': [1, 2],
                                  'list2': [1, 2, 3],
                                  'list3': [1, 2]})

    def test_add_new_key(self):
        result = task1_3.add_to_list_in_dict(self.thedict, 'list4', 1)
        self.assertEqual(result, {'list1': [1, 2],
                                  'list2': [1, 2],
                                  'list3': [1, 2],
                                  'list4': [1]})

    def tearDown(self):
        self.thedict = {
            'list1': [1, 2],
            'list2': [1, 2],
            'list3': [1, 2]
        }


class TestPrintListElement(unittest.TestCase):
    def setUp(self) -> None:
        self.thelist = ['aaa', 'bbb', 'ccc']

    def test_print_element_in_list(self):
        result = task1_2.print_list_element(self.thelist, 1)
        self.assertEqual(result, 'bbb')

    def test_print_index_error(self):
        result = task1_2.print_list_element(self.thelist, 5)
        self.assertEqual(result, None)

    def tearDown(self):
        self.thelist = ['aaa', 'bbb', 'ccc']

class TestSecondIndex(unittest.TestCase):
    def test_count_symbol_one(self):
        text = 'abcde'
        symbol = 'b'
        self.assertEqual(text.count(symbol), 1)

    def test_count_symbol_two(self):
        text = 'abc abc'
        symbol = 'b'
        self.assertEqual(text.count(symbol), 2)

    def test_count_less_two(self):
        text = 'abcde'
        symbol = 'b'
        result = all_def.second_index(text, symbol)
        self.assertEqual(result, None)

    def test_second_index(self):
        text = 'qwerty qwerty'
        symbol = 'ty'
        result = all_def.second_index(text, symbol)
        self.assertEqual(result, 11)


class TestFirstWord(unittest.TestCase):
    def test_first_word_dot(self):
        text = '.abc def ghi.'
        result = all_def.first_word(text)
        self.assertEqual(result, 'abc')

    def test_first_word_comma(self):
        text = ',abc def ghi,'
        result = all_def.first_word(text)
        self.assertEqual(result, 'abc')

    def test_first_word_dot_space(self):
        text = '. abc def ghi.'
        result = all_def.first_word(text)
        self.assertEqual(result, 'abc')

    def test_first_word_comma_space(self):
        text = ', abc def ghi.'
        result = all_def.first_word(text)
        self.assertEqual(result, 'abc')

    def test_first_without_punct(self):
        text = 'abc def ghi.'
        result = all_def.first_word(text)
        self.assertEqual(result, 'abc')


class TestIndexPower(unittest.TestCase):
    def test_index_number(self):
        array = [1, 2, 3, 4]
        n = 6
        result = all_def.index_power(array, n)
        self.assertEqual(result, -1)

    def test_index_power(self):
        array = [1, 2, 3, 4]
        n = 2
        result = all_def.index_power(array, n)
        self.assertEqual(result, 9)


class TestLongWord(unittest.TestCase):
    def test_get_long_word(self):
        result1 = all_def.get_long_word(
            text="123, 1234, 12 - 1234567!"
        )
        result2 = all_def.get_long_word(
            text="12345. 123 12 1"
        )
        result3 = all_def.get_long_word(
            text='Aaaa - bbbbbbb, cc!'
        )

        self.assertEqual(result1, '1234567')
        self.assertEqual(result2, '12345')
        self.assertEqual(result3, 'bbbbbbb')


class TestNewString(unittest.TestCase):
    def test_string_without_spaces(self):
        text = 'abc def ghi'
        result = all_def.get_new_string(text)
        self.assertEqual(result, 'abcdefghi')

    def test_string_non_repeat(self):
        text = 'abc cde def'
        result = all_def.get_new_string(text)
        self.assertEqual(result, 'abcdef')


class TestCountWords(unittest.TestCase):
    def test_upper_words(self):
        text = "QWERTY"
        result = all_def.count_words(text)
        self.assertEqual(result, (0, 6))

    def test_lower_words(self):
        text = "qwerty"
        result = all_def.count_words(text)
        self.assertEqual(result, (6, 0))

    def test_count_only_words(self):
        text = 'AaBbCcD'
        result = all_def.count_words(text)
        self.assertEqual(result, (3, 4))

    def test_with_different_symb(self):
        text = '123AaBbCcD'
        result = all_def.count_words(text)
        self.assertEqual(result, (3, 4))


class TestCountMeString(unittest.TestCase):
    def test_count_one_word(self):
        text = 'aaaaa'
        result = all_def.count_me_string(text)
        self.assertEqual(result, {'a': 5})

    def test_count_few_words(self):
        text = 'ababca'
        result = all_def.count_me_string(text)
        self.assertEqual(result, {'a': 3, 'b': 2, 'c': 1})


if __name__ == '__main__':
    unittest.main()
