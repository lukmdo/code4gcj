import unittest
from Btrains import gen_num_trains


class TestFoo(unittest.TestCase):
    def test_case1(self):
        num_trains_at_station_a = gen_num_trains(
            departures=('09:00', '10:00', '11:00'),
            arrivals=('15:00', '10:30'),
            turnarround=5
        )
        self.assertEqual(num_trains_at_station_a, 2)
        num_trains_at_station_b = gen_num_trains(
            departures=('12:02', '09:00'),
            arrivals=('12:00', '13:00', '12:30'),
            turnarround=5
        )
        self.assertEqual(num_trains_at_station_b, 2)


    def test_case2(self):
        num_trains_at_station_a = gen_num_trains(
            departures=('09:00', '12:00'),
            arrivals=(),
            turnarround=5
        )
        self.assertEqual(num_trains_at_station_a, 2)
        num_trains_at_station_b = gen_num_trains(
            departures=(),
            arrivals=('09:01', '12:02'),
            turnarround=5
        )
        self.assertEqual(num_trains_at_station_b, 0)


if __name__ == '__main__':
    unittest.main()
