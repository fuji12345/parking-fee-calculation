import math
from datetime import datetime

from .parking import Parking


class Night(Parking):
    def __init__(self, start: datetime, end: datetime, per_time=60, per_fee=100, max_fee=300) -> None:
        super().__init__()
        self.per_time = per_time
        self.per_fee = per_fee
        self.max_fee = max_fee

        self.start = start
        self.end = end

    def start_pakring_at_night(self):
        if self.start < self.start.replace(hour=8, minute=0) and self.start.replace(hour=8, minute=0) < self.end:
            print("夜間始まり：早朝")
            self.end = self.start.replace(hour=8)
        if (
            self.start.replace(hour=20, minute=0) < self.start
            and self.start.replace(day=self.start.day + 1, hour=8, minute=0) < self.end
        ):
            print("夜間始まり：夜")
            self.end = self.start.replace(day=self.start.day + 1, hour=8)

    def calculate_parking_fee(self):
        # startが早朝の場合はfinishを朝8時にする
        # 夜間始まりは、20時~24時の場合と0時~8時の場合がある
        if self.start < self.start.replace(hour=8, minute=0) and self.start.replace(hour=8, minute=0) < self.end:
            print("夜間始まり：早朝")
            self.end = self.start.replace(hour=8, minute=0)
        if (
            self.start.replace(hour=20, minute=0) < self.start
            and self.start.replace(day=self.start.day + 1, hour=8, minute=0) < self.end
        ):
            print("夜間始まり：夜")
            self.end = self.start.replace(day=self.start.day + 1, hour=8, minute=0)

        # endがstart日の翌日の08:00より後の場合、endはstart日の翌日の08:00になる
        finish_time = self.start.replace(day=self.start.day + 1, hour=8, minute=0)
        if finish_time < self.end:
            self.end = finish_time

        fee = self.calculate_parking_fee_helper()
        return fee, self.end
