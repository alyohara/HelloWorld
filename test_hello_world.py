import unittest

class TestHelloWorld(unittest.TestCase):
  def test_hello_world(self):
    from helloWorld import helloWorld
    self.assertEqual(helloWorld(), "Hello, World!")
