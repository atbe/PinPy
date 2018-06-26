import unittest
import os
import pinpy

class TestPypinExceptions(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pinpy.API(os.environ['PIN_TOKEN'], os.environ['PIN_V3_TOKEN'])

    def test_content_not_found_exception(self):
        with self.assertRaises(pinpy.exceptions.PinPyContentNotFoundError):
            self.api.get_public_pin_v3('this_is_a_garbage_pin_number')

if __name__ == '__main__':
    unittest.main()
