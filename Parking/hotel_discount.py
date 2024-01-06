import math
from datetime import datetime

from .parking import Parking


class Hotel_discount(Parking):
    def __init__(self, start, end, per_time=20, per_fee=200, max_fee=1300) -> None:
        super().__init__()
        self.per_time = per_time
        self.per_fee = per_fee
        self.max_fee = max_fee

        self.daily_parking_fee = 1200

        self.start = start
        self.end = end

    def calculate_parking_fee(self):
        # 11時から14時までは20分ごとに200円(最大料金：1300円)
        # 14時から翌日11時までは利用時間に関わらず1200円
        # if 11時から14時なら通常料金＋それ以外なら1200プラスして次の日に飛ばす。
        total_fee = 0
        while True:
            if self.end <= self.start:
                break

            eleven_am = self.start.replace(hour=8, minute=0)
            two_pm = self.start.replace(hour=14, minute=0)

            if eleven_am <= self.start < two_pm:
                if two_pm <= self.end:
                    total_fee += self.calculate_parking_fee_helper(start=self.start, end=two_pm)
                    self.start = two_pm
                else:
                    total_fee += self.calculate_parking_fee_helper(start=self.start, end=self.end)
                    self.start = two_pm
            else:
                total_fee += 1200
                self.start = self.start.replace(day=self.start.day + 1, hour=11, minute=0)
                print(f"fixed fee 14:00 ~ 11:00")
                print(1200)

        return total_fee
