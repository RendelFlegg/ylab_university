import unittest
import homework_1


class TestHomework1(unittest.TestCase):
    def test_domain_naim(self):
        self.assertTrue(homework_1.domain_name('http://google.com') == 'google',
                        'Error when checking "http://google.com"')
        self.assertTrue(homework_1.domain_name('http://google.co.jp') == 'google',
                        'Error when checking "http://google.co.jp"')
        self.assertTrue(homework_1.domain_name('www.xakep.ru') == 'xakep',
                        'Error when checking "www.xakep.ru"')
        self.assertTrue(homework_1.domain_name('https://youtube.com') == 'youtube',
                        'Error when checking "https://youtube.com"')
        self.assertTrue(homework_1.domain_name('http://github.com/carbonfive/raygun') == 'github',
                        'Error when checking "http://github.com/carbonfive/raygun"')
        self.assertTrue(homework_1.domain_name('http://www.zombie-bites.com') == 'zombie-bites',
                        'Error when checking "http://www.zombie-bites.com"')
        self.assertTrue(homework_1.domain_name('https://www.cnet.com') == 'cnet',
                        'Error when checking "https://www.cnet.com"')

    def test_int32_to_ip(self):
        self.assertTrue(homework_1.int32_to_ip(2154959208) == '128.114.17.104',
                        'Error when checking 2154959208')
        self.assertTrue(homework_1.int32_to_ip(0) == '0.0.0.0',
                        'Error when checking 0')
        self.assertTrue(homework_1.int32_to_ip(2149583361) == '128.32.10.1',
                        'Error when checking 2149583361')
        self.assertTrue(homework_1.int32_to_ip(32) == '0.0.0.32',
                        'Error when checking 32')

    def test_zeros(self):
        self.assertTrue(homework_1.zeros(0) == 0, 'Error when checking 0')
        self.assertTrue(homework_1.zeros(6) == 1, 'Error when checking 6')
        self.assertTrue(homework_1.zeros(30) == 7, 'Error when checking 7')
        self.assertTrue(homework_1.zeros(12) == 2, 'Error when checking 12')

    def test_bananas(self):
        self.assertTrue(homework_1.bananas('banann') == set(),
                        'Error when checking "banann"')
        self.assertTrue(homework_1.bananas('banana') == {'banana'},
                        'Error when checking "banana"')
        self.assertTrue(homework_1.bananas('bbananana') == {'b-an--ana', '-banana--', '-b--anana', 'b-a--nana',
                                                            '-banan--a', 'b-ana--na', 'b---anana', '-bana--na',
                                                            '-ba--nana', 'b-anan--a', '-ban--ana', 'b-anana--'},
                        'Error when checking "bbananana"')
        self.assertTrue(homework_1.bananas('bananaaa') == {'banan-a-', 'banana--', 'banan--a'},
                        'Error when checking "bananaaa"')
        self.assertTrue(homework_1.bananas('bananana') == {'ban--ana', 'ba--nana', 'bana--na',
                                                           'b--anana', 'banana--', 'banan--a'},
                        'Error when checking "bananana"')

    def test_count_find_num(self):
        self.assertTrue(homework_1.count_find_num([2, 5, 7], 500) == [5, 490], 'Error when checking [2, 5, 7], 500')
        self.assertTrue(homework_1.count_find_num([2, 3], 200) == [13, 192], 'Error when checking [2, 3], 200')
        self.assertTrue(homework_1.count_find_num([2, 5], 200) == [8, 200], 'Error when checking [2, 5], 200')
        self.assertTrue(homework_1.count_find_num([2, 3, 5], 500) == [12, 480], 'Error when checking [2, 3, 5], 500')
        self.assertTrue(homework_1.count_find_num([2, 3, 5], 1000) == [19, 960], 'Error when checking [2, 3, 5], 1000')
        self.assertTrue(homework_1.count_find_num([2, 3, 47], 200) == [], 'Error when checking [2, 3, 47], 200')
