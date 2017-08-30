import pypin
import unittest
import os

class TestPinModel(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(os.environ['PIN_TOKEN'])
        self.pin = self.api.get_public_pin('132645151506393653')

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.pin, pypin.Pin, msg='Pin should be type pypin.models.Pin')

    def test_pin_id_getter(self):
        self.assertIsNotNone(self.pin.id, msg='Pin id should be initialized.')

class TestUserModel(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(os.environ['PIN_TOKEN'])
        self.user = self.api.get_user('132645288933331629')

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.user, pypin.User, msg='Pin should be type pypin.models.Pin')

    def test_user_id_getter(self):
        self.assertIsNotNone(self.user.id, msg='User id should be initialized.')

class TestBoardModel(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(os.environ['PIN_TOKEN'])
        self.board = self.api.get_public_board('132645220214057739')

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.board, pypin.Board, msg='Board should be type pypin.models.Board')
        self.assertIsInstance(self.board.creator, pypin.User, msg='Boards creator should be type pypin.models.User')

    def test_board_id_getter(self):
        self.assertIsNotNone(self.board.id, msg='Board id should be initialized.')


class TestBoardPinsModel(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(os.environ['PIN_TOKEN'])
        self.board_pins = self.api.get_public_board_pins('107734684775018526')

    def test_constructor(self):
        # TODO: Remove the hardcoded sample Pin and use some sort of cassettes.
        self.assertIsInstance(self.board_pins, pypin.BoardPins, msg='BoardPins should be type pypin.models.BoardPins')

    def test_board_pins_id_getter(self):
        self.assertIsNotNone(self.board_pins.id, msg='BoardPins id should be initialized.')

    def test_board_pins_iter(self):
        c = 0
        for pin in self.board_pins:
            c += 1
            self.assertIsInstance(pin, pypin.Pin, msg='Iterating over BoardPins should return Pins.')
        self.assertEqual(c, self.api.get_public_board(self.board_pins.id).pin_count,
                         msg='Iter should loop over the number of pins on the board.')


if __name__ == '__main__':
    unittest.main()