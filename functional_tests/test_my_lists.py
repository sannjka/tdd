from selenium.webdriver.common.by import By
from .base import FunctionalTest
from .server_tools import create_session_on_server


class MyListsTest(FunctionalTest):

    def test_create_pre_authenticated_session_works(self):
        email = 'edith@example.com'
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_out(email)

        # Edith is a logged in user
        self.create_pre_authenticated_session(email)
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_in(email)

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged in user
        self.create_pre_authenticated_session('edith@example.com')
        self.browser.get(self.live_server_url)
        self.add_list_item('Reticulate splines')
        self.add_list_item('Immanentize eschaton')
        first_list_url = self.browser.current_url

        # She notices "My lists" link, for the first time.
        self.browser.find_element(By.LINK_TEXT, 'My lists').click()

        # She sees that her list is in there, named according to its
        # first list item
        self.wait_for(lambda: self.browser.find_element(
            By.LINK_TEXT, 'Reticulate splines'
        ))
        self.browser.find_element(By.LINK_TEXT, 'Reticulate splines').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # She decides to start anothe list, just to see
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # Under "My lists" her new list appears
        self.browser.find_element(By.LINK_TEXT, 'My lists').click()
        self.wait_for(lambda: self.browser.find_element(
            By.LINK_TEXT, 'Click cows'
        ))
        self.browser.find_element(By.LINK_TEXT, 'Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # She logs out. "My lists option" disappears
        self.browser.find_element(By.LINK_TEXT, 'Log out').click()
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_elements(By.LINK_TEXT, 'My lists'),
            []
        ))

