import unittest

suite = unittest.TestLoader().discover(start_dir="chessTests", pattern="test*.py")
unittest.TextTestRunner().run(suite)
