import unittest

class TestHelloWorld(unittest.TestCase):
  def test_hello_world(self):
    from hello_world import hello_world
    self.assertEqual(hello_world(), "Hello, World!")
