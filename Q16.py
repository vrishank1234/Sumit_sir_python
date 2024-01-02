# 16. Build a hotel reservation system with classes for rooms, guests, and reservations.
# Implement methods for checking room availability, booking rooms, and generating
# invoices.

from datetime import datetime
import random
import string

class Room:
    def __init__(self, room_number, capacity, rate_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.rate_per_night = rate_per_night
        self.reservations = []

    def is_available(self, start_date, end_date):
        for reservation_start, reservation_end in self.reservations:
            if start_date < reservation_end and end_date > reservation_start:
                return False
        return True

    def book_room(self, guest, start_date, end_date):
        if self.is_available(start_date, end_date):
            reservation_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            self.reservations.append((start_date, end_date, reservation_id, guest))
            return reservation_id
        else:
            return None

    def get_rate_per_night(self):
        return self.rate_per_night

class Guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_availability(self, start_date, end_date):
        available_rooms = []
        for room in self.rooms:
            if room.is_available(start_date, end_date):
                available_rooms.append(room)
        return available_rooms

    def book_room(self, guest, room, start_date, end_date):
        reservation_id = room.book_room(guest, start_date, end_date)
        if reservation_id:
            return reservation_id
        else:
            return None

    def generate_invoice(self, room, reservation_id):
        for reservation_start, reservation_end, res_id, guest in room.reservations:
            if res_id == reservation_id:
                duration = (reservation_end - reservation_start).days
                total_cost = duration * room.get_rate_per_night()
                print("Invoice:")
                print(f"Guest: {guest.name}")
                print(f"Room Number: {room.room_number}")
                print(f"Reservation ID: {reservation_id}")
                print(f"Check-in Date: {reservation_start}")
                print(f"Check-out Date: {reservation_end}")
                print(f"Total Cost: Rs.{total_cost:.2f}")
                return
        print("Reservation not found.")

def get_guest_details():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    return Guest(name, email)

def get_booking_dates():
    print("Enter booking dates:")
    start_date_str = input("Check-in date (YYYY-MM-DD): ")
    end_date_str = input("Check-out date (YYYY-MM-DD): ")

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    return start_date, end_date

def main():
    # Create a hotel
    hotel = Hotel()

    # Add rooms to the hotel
    room1 = Room("101", 2, 100.0)
    room2 = Room("102", 4, 150.0)
    room3 = Room("103", 1, 80.0)

    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)

    # Get guest details
    guest = get_guest_details()

    # Get booking dates
    start_date, end_date = get_booking_dates()

    # Check room availability
    available_rooms = hotel.check_availability(start_date, end_date)

    if not available_rooms:
        print("No available rooms for the selected dates.")
    else:
        # Book a room
        selected_room = available_rooms[0]
        reservation_id = hotel.book_room(guest, selected_room, start_date, end_date)
        if reservation_id:
            print(f"Room booked successfully. Reservation ID: {reservation_id}")
            # Generate an invoice
            hotel.generate_invoice(selected_room, reservation_id)

if __name__ == "__main__":
    main()
