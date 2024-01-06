import datetime
import math
from abc import ABC, abstractmethod
from datetime import datetime


class Parking(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def calculate_parking_fee(self):
        pass

    def calculate_parking_fee_helper(self, start=None, end=None):
        if (start is None) and (end is None):
            start = self.start
            end = self.end
        parking_length = end - start
        parking_length_minutes = self.to_minutes(parking_length)

        fee = math.ceil(parking_length_minutes / self.per_time) * self.per_fee
        if fee > self.max_fee:
            fee = self.max_fee

        print(f"{start} ~ {end}")
        print(fee)

        return fee

    def to_minutes(self, parking_length: datetime):
        total_seconds = parking_length.seconds
        minutes = total_seconds // 60
        return minutes
