import unittest

from dls_util.image import Color

class TestColor(unittest.TestCase):
    # given-when-then

    def setUp(self):
        self.firstColor = Color(10,50,100)

    def test_init_riases_valueerror_when_r_is_not_number(self):
        pass

    def test_init_riases_valueerror_when_r_is_lt_zero(self):
        pass

    def test_init_riases_valueerror_when_r_is_gt_255(self):
        pass

    def test_init_sets_alpha_255_if_not_set(self):
        pass

    def test_bgra_returns_rgb_plus_alpha_tuple(self):
        self.assertEquals(Color.bgra(self.firstColor), (100,50,10,255))

    def test_bgra_Red_returns_rgb_plus_alpha_tuple_with_full_red_channel(self):
        self.assertEquals(Color.Red().bgra(), (0, 0, 255, 255))

    def test_bgra_Green_returns_rgb_plus_alpha_tuple_with_full_red_channel(self):
        self.assertEquals(Color.Green().bgra(), (0, 255, 0, 255))

    def test_bgra_Blue_returns_rgb_plus_alpha_tuple_with_full_red_channel(self):
        self.assertEquals(Color.Blue().bgra(), (255, 0, 0, 255))

    def test_bgra_TW_returns_rbb_plus_alpha_tuple_with_zero_alpha(self):
        self.assertEquals(Color.TransparentWhite().bgra(), (255, 255, 255, 0))

    def test_bgr(self):
        self.assertEquals(self.firstColor.bgr(), (100,50,10))

    def test_mono(self):
        self.assertEquals(Color.mono(self.firstColor), round(0.3*10 + 0.6*50 + 0.1*100))

    def test_to_qt_returns_QColour_of_rgba_values_zeroone(self):

        actual = Color.to_qt(self.firstColor)
        self.assertEqual(actual.getRgbF(),  (10.0/255, 50.0/255, 100.0/255, 1.0))

    def test_from_qt_returns_QColour_of_rgba_as_zero255(self):

        qtcolor = Color.to_qt(self.firstColor)
        actual = Color.from_qt(qtcolor)

        self.assertEqual(Color.bgra(actual),  (100, 50, 10, 255))

    def test_to_hex(self):
        self.assertEquals(Color.to_hex(self.firstColor), '#0a3264')

    def test_to_string_returns_csv_rgba(self):
        self.assertEqual(str(self.firstColor), "10,50,100,255")

    def test_Black_is_0x000000FF(self):
        #or use str(color)
        self.assertEqual(Color.Black().to_hex(), "0x000000FF")

    def test_Blue_is_0x0000FFFF(self):
        self.assertEqual(Color.Blue().to_hex(), "0x0000FFFF")

    def test_Grey_is_0x808080FF(self):
        self.assertEqual(Color.Grey().to_hex(), "0x808080FF")

    def test_from_string_returns_Color_with_given_rbg_and_alpha255_with_csv_three_valued_string(self):
        col = Color.from_string("25, 100, 243")
        self.assertEqual(col.bgra(), (243, 100, 25, 255))

    def test_from_string_returns_Color_with_given_rbga_with_csv_four_valued_string(self):
        col = Color.from_string("251, 63, 1, 128")
        self.assertEqual(col.bgra(), (1, 63, 251, 128))

    def test_from_string_returns_Color_with_given_rbga_with_custom_seperator_four_valued_string(self):
        col = Color.from_string("251;63;1;128", ";")
        self.assertEqual(col.bgra(), (1, 63, 251, 128))

    def test_from_string_raises_ValueError_if_no_separator(self):
        self.assertRaises(ValueError, Color.from_string, "121242")