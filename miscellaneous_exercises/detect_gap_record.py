# Detect a gap in a patient's medication record:
# The patient is supposed to take the medication every day.
# Return the first date on which they missed a dose.
# If there are no missing days, return None.
# Expected output: 2026-09-04

medications = [
    {"name": "Vitamin D", "date": "2026-09-01"},
    {"name": "Vitamin D", "date": "2026-09-02"},
    {"name": "Vitamin D", "date": "2026-09-03"},
    {"name": "Vitamin D", "date": "2026-09-06"},
    {"name": "Vitamin D", "date": "2026-09-07"},
]

from datetime import datetime, timedelta

first_day_missed = None

for i in range(1, len(medications)):
  current_date = datetime.strptime(medications[i]["date"],'%Y-%m-%d').date()
  previous_date = datetime.strptime(medications[i-1]["date"], '%Y-%m-%d').date()
  difference = (current_date - previous_date).days

  if difference > 1:
    first_day_missed = previous_date + timedelta(days=1)
    break
