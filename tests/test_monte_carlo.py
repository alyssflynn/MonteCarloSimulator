import math
from unittest import mock, TestCase

from numpy import array

from monte_carlo import monte_carlo_step, build_monte_carlo_array

class TestMonteCarlo(TestCase):
    @mock.patch("monte_carlo.normal")
    def test_monte_carlo_step(self, mock_normal):
        mock_normal.return_value = 2
        rate = 1
        base = 3

        step = monte_carlo_step(base, rate, mock_normal.return_value)

        self.assertEqual(base * rate * math.exp(2), step)


    @mock.patch("monte_carlo.monte_carlo_step", autospec=True)
    def test_build_monte_carlo_array_adds_new_step_if_depth_is_not_zero(self,
            mock_step):
        mock_step.return_value = "STEP"

        monte_array = build_monte_carlo_array(6, 4, 5, 3)

        mock_step.assert_has_calls([
            mock.call(6, 4, 5),
            mock.call("STEP", 4, 5),
            mock.call("STEP", 4, 5)
        ])
