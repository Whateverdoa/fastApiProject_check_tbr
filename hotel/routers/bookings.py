from fastapi import APIRouter

from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking, DBRoom
from hotel.operations.bookings import (read_all_bookings,
                                       read_booking,
                                       BookingCreateData,
                                       create_booking, delete_booking
                                       )

router = APIRouter()


@router.get("/bookings")
def api_read_all_bookings():
    booking_interface = DBInterface(DBBooking)
    return read_all_bookings(booking_interface)


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int):
    booking_interface = DBInterface(DBBooking)
    return read_booking(booking_id, booking_interface)


@router.post("/booking")
def api_create_booking(booking: BookingCreateData):
    booking_interface = DBInterface(DBBooking)
    room_interface = DBInterface(DBRoom)
    return create_booking(booking, booking_interface, room_interface)


@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id):
    booking_interface = DBInterface(DBBooking)
    return delete_booking(booking_id, booking_interface)
