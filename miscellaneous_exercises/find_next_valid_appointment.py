# You have a patient's appointment history.
# Return the first booked appointment on or after today.
# If there isn't one, return None.

# Example result: {"date": "2026-10-15", "status": "booked"}

from datetime import datetime

appointments = [
    {"date": "2026-09-10", "status": "completed"},
    {"date": "2026-09-25", "status": "cancelled"},
    {"date": "2026-10-05", "status": "completed"},
    {"date": "2026-10-15", "status": "booked"},
    {"date": "2026-11-02", "status": "booked"},
]

today = datetime.today().strftime("%Y-%m-%d")
first_booked_appointment = None

for appointment in appointments:
  if appointment["date"] >= today and appointment["status"] == "booked":
    first_booked_appointment = appointment
    break

# test the output
print(first_booked_appointment)
