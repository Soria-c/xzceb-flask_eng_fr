import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    """Tests for translator"""
    def test_null_input(self):
        """Tests null input"""
        with self.assertRaises(TypeError):
            french_to_english()
        with self.assertRaises(TypeError):
            english_to_french()
    
    def test_english_to_french(self):
        """English to french test"""
        self.assertEqual("Bonjour", english_to_french("Hello"))
    
    def test_french_to_english(self):
        """French to english test"""
        self.assertEqual("Hello", french_to_english("Bonjour"))

if __name__ == "__main__":
    unittest.main()
        