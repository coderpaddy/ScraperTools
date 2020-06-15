import tools
import random
import unittest

class TestScrapeMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestScrapeMethods, self).__init__(*args, **kwargs)
        self.root_url = "https://www.blackhatworld.com/"
        self.specific_url = "forums/introductions.24/"

    def test_get_soup(self):
        soup = tools.get_soup(f"{self.root_url}{self.specific_url}")
        self.main_soup = soup
        self.assertTrue(soup)

    def test_single(self):
        elem = tools.get_elem(tools.get_soup(f"{self.root_url}{self.specific_url}"), "div", "class", "noticeContent")
        self.assertTrue(elem)

    def test_multiple(self):
        elems = tools.get_elems(tools.get_soup(f"{self.root_url}{self.specific_url}"), "li", "class", "discussionListItem")
        self.assertTrue(elems)

    def test_full_scrape(self):
        elems = tools.get_elems(tools.get_soup(f"{self.root_url}{self.specific_url}"), "li", "class", "discussionListItem")
        item_dict = {}
        count = 0
        for elem in elems:
            count += 1
            main_block = tools.get_elems(elem, "h3", "class", "title")[0]
            item_dict[count] = {
                "title": main_block.a.get_text(),
                "url": f"{self.root_url}{main_block.a.attrs['href']}",
            }
        self.assertEqual(count, len(item_dict))
        self.assertIsNotNone(item_dict[random.randint(0, count - 1)])

if __name__ == '__main__':
    unittest.main()