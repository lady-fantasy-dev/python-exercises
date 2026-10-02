// Detect a gap in a patient's medication record:
// The patient is supposed to take the medication every day.
// Return the first date on which they missed a dose.
// If there are no missing days, return None.
// Expected output: 2026-09-04

let medications = [
    {"name": "Vitamin D", "date": "2026-09-01"},
    {"name": "Vitamin D", "date": "2026-09-02"},
    {"name": "Vitamin D", "date": "2026-09-03"},
    {"name": "Vitamin D", "date": "2026-09-06"},
    {"name": "Vitamin D", "date": "2026-09-07"},
]

let missedDay = null;

for(let i = 1; i < medications.length; i++){
  let currentDate = Date.parse(medications[i].date);
  let previousDate = Date.parse(medications[i-1].date);

  let timeDifference = currentDate - previousDate;
  let day = 1000 * 60 * 60 * 24;
  let daysDifference = timeDifference / day;

  if(daysDifference > 1){
    missedDay = new Date(previousDate + day)
      .toISOString()
      .split("T")[0];

    break;
  }
}
