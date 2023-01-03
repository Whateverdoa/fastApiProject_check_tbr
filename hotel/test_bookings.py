import unittest
from abc import ABC
from datetime import date

from hotel.operations.bookings import BookingCreateData, create_booking, InvalidDateError
from hotel.operations.interface import DataObject


class DataInterfaceStub:

    def read_by_id(self, id: int) -> DataObject:
        raise NotImplementedError()

    def read_all(self) -> list[DataObject]:
        raise NotImplementedError()

    def create(self, data: DataObject) -> DataObject:
        raise NotImplementedError()

    def updating(self, id: int, data: DataObject) -> DataObject:
        raise NotImplementedError()

    def delete(self, id: int) -> DataObject:
        raise NotImplementedError()


class RoomInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        return {"id": id, "number": "101", "size": 10, "price": 150_00}


class BookingInterface(DataInterfaceStub):
    def create(self, data: DataObject) -> DataObject:
        booking = dict(data)
        booking["id"] = 1
        return booking


class TestBooking(unittest.TestCase):

    def test_price_one_day(self):
        booking_data = BookingCreateData(
            room_id=1,
            customer_id=1,
            from_date=date(2021, 12, 24),
            to_date=date(2021, 12, 25),
        )
        booking = create_booking(data=booking_data,
                                 booking_interface=BookingInterface(),
                                 room_interface=RoomInterface(),
                                 )

        self.assertEqual(booking["price"], 150_00)

    def test_day_not_zero(self):
        booking_data = BookingCreateData(
            room_id=1,
            customer_id=1,
            from_date=date(2021, 12, 25),
            to_date=date(2021, 12, 25),
        )
        self.assertRaises(InvalidDateError,
                          create_booking,
                          booking_data,
                          BookingInterface(),
                          RoomInterface())


if __name__ == "__main__":
    unittest.main()
