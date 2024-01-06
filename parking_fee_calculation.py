import argparse
import datetime
from datetime import datetime

from Parking import Daytime, Hotel_discount, Night, Parking


def is_termination_condition(parked_datetime, departure_datetime):
    return (departure_datetime - parked_datetime).days < 0 or (parked_datetime == departure_datetime)


def main(args):
    parked_time: str = args.parked_time
    departure_time: str = args.departure_time

    parked_datetime = datetime.strptime(parked_time, "%Y-%m-%d %H:%M")
    departure_datetime = datetime.strptime(departure_time, "%Y-%m-%d %H:%M")

    hote_parking = Hotel_discount(parked_datetime, departure_datetime)
    fee_with_hotel_discount = hote_parking.calculate_parking_fee()
    print(f"parking fee with hotel discount: {fee_with_hotel_discount}")
    print("################################")

    total_fee = 0
    while True:
        if is_termination_condition(parked_datetime, departure_datetime):
            break

        # 日中の料金計算
        daytime: Parking = Daytime(parked_datetime, departure_datetime)
        fee, current_start = daytime.calculate_parking_fee()
        total_fee += fee

        # 計算済みの時間を進める
        parked_datetime = current_start
        if is_termination_condition(parked_datetime, departure_datetime):
            break

        # 夜間の料金計算
        night: Parking = Night(parked_datetime, departure_datetime)
        fee, current_start = night.calculate_parking_fee()
        parked_datetime = current_start
        total_fee += fee

    print(f"total fee: {total_fee}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("parked_time", type=str)
    parser.add_argument("departure_time", type=str)
    args = parser.parse_args()
    main(args)
