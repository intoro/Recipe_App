import unittest

from project import app


class ProjectTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test


    ########################
    #### helper methods ####
    ########################

    def register(self, email, password, confirm):
        return self.app.post(
            'register/',
            data=dict(email=email, password=password, confirm=confirm),
            follow_redirects=True
        )

    def login(self, email, password):
        return self.app.post(
            '/login',
            data=dict(email=email, password=password),
            follow_redirects=True
        )



    ###############
    #### tests ####
    ###############

    # def test_main_page(self):
    #     response = self.app.get('/', follow_redirects=True)
    #     self.assertIn(b'Recipes', response.data)
    #     self.assertIn(b'Title', response.data)
    #     self.assertIn(b'Description', response.data)
    #
if __name__ == "__main__":
    unittest.main()
