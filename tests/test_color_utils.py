import unittest
from colorlib.color_utils import hex_to_rgb, rgb_to_hex, complement_color


class TestColorUtils(unittest.TestCase):
    def test_hex_to_rgb(self):
        self.assertEqual(hex_to_rgb('#FFFFFF'), (255, 255, 255))
        self.assertEqual(hex_to_rgb('#000000'), (0, 0, 0))
        self.assertEqual(hex_to_rgb('#FF5733'), (255, 87, 51))

    def test_rgb_to_hex(self):
        self.assertEqual(rgb_to_hex((255, 255, 255)), '#FFFFFF')
        self.assertEqual(rgb_to_hex((0, 0, 0)), '#000000')
        self.assertEqual(rgb_to_hex((255, 87, 51)), '#FF5733')

    def test_complement_color(self):
        self.assertEqual(complement_color('#FFFFFF'), '#000000')
        self.assertEqual(complement_color('#000000'), '#FFFFFF')
        self.assertEqual(complement_color('#FF5733'), '#00A8CC')


if __name__ == '__main__':
    unittest.main()
