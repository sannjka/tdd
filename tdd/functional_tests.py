from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_cat_start_a_todo_list(self):
        # Edith had heard about a cool new online to-do app.
        # She goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invated to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing tures)

        # When she hits enter, the page updates, and now the page ists
        # "1: Buy peacock feathers" as ant item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now show both items on her list

        # Satisfied, she goes bach to sleep

if __name__ == "__main__":
    unittest.main()
