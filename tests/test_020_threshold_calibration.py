import unittest

from care_gap_prioritizer.models import Record
from care_gap_prioritizer.scoring import score_record


class DepthCheck20(unittest.TestCase):
    def test_020_threshold_calibration(self):
        record = Record(id="member-020", exposure=50400, signal=0.848, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
