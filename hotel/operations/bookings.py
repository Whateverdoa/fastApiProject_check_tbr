from datetime import date

from pydantic import BaseModel
from hotel.operations.interface import DataInterface, DataObject


class BookingCreateData(BaseModel):
    """with pydantic to validate the data that can be used"""

    room_id: int
    customer_id: int
    from_date: date
    to_date: date


class InvalidDateError(Exception):
    pass


def read_all_bookings(booking_interface: DataInterface) -> list[DataObject]:
    return booking_interface.read_all()


def read_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.read_by_id(booking_id)


def create_booking(
        data: BookingCreateData,
        booking_interface: DataInterface,
        room_interface: DataInterface) -> DataObject:
    # retrieve the room(to make a calculation)
    room = room_interface.read_by_id(data.room_id)
    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise InvalidDateError("Invalid dates")
    booking_dict = data.dict()
    booking_dict["price"] = room['price'] * days

    booking = booking_interface.create(booking_dict)
    return booking


def delete_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.delete(booking_id)
