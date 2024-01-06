import math
from datetime import datetime

from .parking import Parking


class Daytime(Parking):
    def __init__(self, start: datetime, end: datetime, per_time=20, per_fee=200, max_fee=1300) -> None:
        super().__init__()
        self.per_time = per_time
        self.per_fee = per_fee
        self.max_fee = max_fee

        self.start = start
        self.end = end

    def is_skip(self):
        if self.start < self.start.replace(hour=8, minute=0):
            print("day skip")
            return True
        if self.start.replace(hour=20, minute=0) < self.start:
            print("day skip")
            return True
        return False

    def calculate_parking_fee(self):
        # # 夜間に駐車開始した場合、最初のdaytimeの駐車料金計算はスキップされる
        if self.is_skip():
            return 0, self.start

        # endがself.start日の20:00より後の場合、endはself.start日の20:00になる
        if self.start.replace(hour=20, minute=0) < self.end:
            self.end = self.start.replace(hour=20, minute=0)

        fee = self.calculate_parking_fee_helper()
        return fee, self.end
