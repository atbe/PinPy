import pinpy
import unittest
import os

'''
These tests are meant for the models of the api/v3 endpoints. They are in no way the same as the api/v1 responses.
'''


class TestBoardPinsV3Model(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pinpy.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.board_pins = self.api.get_public_board_pins_v3('554857685279866446', page_size=10)

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.board_pins, pinpy.BookmarkPagination, msg='BoardPins should be type pypin.models.BookmarkPagination')

    def test_board_pins_iter(self):
        for i, pin in enumerate(self.board_pins):
            if i == 11:
                return
        self.fail("Use a different sample board! Not enough pins to test")


class TestUserFollowersV3Model(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pinpy.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.followers = self.api.get_user_followers_v3('hawkins6654', page_size=10)

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.followers, pinpy.BookmarkPagination, msg='pin should be type pypin.models.UserFollowersV3')

    def test_status(self):
        self.assertEqual(self.followers.status, "success", msg='status should be "success".')

    def test_paginated(self):
        for i, follower in enumerate(self.followers):
            if i == 11:
                return

        self.fail("Use a different sample user! Not enough followers to test.")


class TestUserFollowingV3Model(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pinpy.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.following = self.api.get_user_following_v3('hawkins6654', page_size=10)

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.following, pinpy.BookmarkPagination, msg='pin should be type pypin.models.UserFollowingV3')

    def test_paginated(self):
        for i, user in enumerate(self.following):
            if i == 11: # trigger the pagination
                return

        self.fail("Use a different sample user! Not enough following to test.")


class TestUserPinsV3Model(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pinpy.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.pins = self.api.get_user_pins_v3('hawkins6654', page_size=10)

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.pins, pinpy.BookmarkPagination, msg='pin should be type pypin.models.UserPinsV3')

    def test_status(self):
        self.assertEqual(self.pins.status, "success", msg='status should be "success".')

    def test_paginated(self):
        for i, user in enumerate(self.pins):
            if i == 11:
                return

        self.fail("Use a different sample user! Not enough pins to test.")


class TestBoardV3(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pinpy.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.id = '695384067402673738'
        self.board = self.api.get_board_v3(self.id)

    def test_board_pins_id_getter(self):
        self.assertEqual(self.board.get('id'), self.id, msg='id of board collected should be the one requested')
        self.assertIsNotNone(self.board.get('id'), msg='pin id should be initialized.')


class TestUserV3(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pinpy.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])
        self.id = '695384136122132328'
        self.user = self.api.get_user_v3(self.id)

    def test_board_pins_id_getter(self):
        self.assertEqual(self.user.get('id'), self.id, msg='id of board collected should be the one requested')
        self.assertIsNotNone(self.user.get('id'), msg='pin id should be initialized.')

if __name__ == '__main__':
    unittest.main()