from datetime import datetime
import unittest
from export_to_mysql import get_data


class TestData(unittest.TestCase):

    def test_validate(self):
        sheet = get_data(filename="HINDALCO_1D.xlsx")

        for index, row in sheet.iterrows():
            time = row['datetime']
            close = row['close']
            high = row['high']
            low = row['low']
            open = row['open']
            volume = row['volume']
            instrument = row['instrument']

            self.assertIsInstance(time, datetime)
            self.assertIsInstance(close, float)
            self.assertIsInstance(high, float)
            self.assertIsInstance(low, float)
            self.assertIsInstance(open, float)
            self.assertIsInstance(volume, float)
            self.assertIsInstance(instrument, str)


if __name__ == "__main__":
    unittest.main()
