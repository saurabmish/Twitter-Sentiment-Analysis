import unittest

from app.client import TwitterClient

class TestTwitterClient(unittest.TestCase):

    def setUp(self):
        self.default_user = TwitterClient()
        self.custom_user = TwitterClient('chelseafc')

    def test_default_user_present(self):
        self.assertTrue(self.default_user)

    def test_custom_user_present(self):
        self.assertTrue(self.custom_user)

    def test_default_user_timeline(self):
        self.assertIsNotNone(self.default_user.get_timeline_tweets(1))

    def test_custom_user_timeline(self):
        self.assertIsNotNone(self.custom_user.get_timeline_tweets(1))

    def test_default_timeline_type(self):
        self.assertIsInstance(self.default_user.get_timeline_tweets(1), list)

    def test_custom_timeline_type(self):
        self.assertIsInstance(self.custom_user.get_timeline_tweets(1), list)


if __name__ == '__main__':
    main()