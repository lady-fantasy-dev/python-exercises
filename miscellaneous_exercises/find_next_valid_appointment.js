// You have a patient's appointment history.
// Return the first booked appointment on or after today.
// If there isn't one, return None.

// Example result: {"date": "2026-10-15", "status": "booked"}

let appointments = [
    {"date": "2026-09-10", "status": "completed"},
    {"date": "2026-09-25", "status": "cancelled"},
    {"date": "2026-10-05", "status": "completed"},
    {"date": "2026-10-15", "status": "booked"},
    {"date": "2026-11-02", "status": "booked"},
]

let today = new Date().toLocaleDateString("fr-CA", {year:"numeric", month: "2-digit", day:"2-digit"})
let firstAppointment = null

for(let appointment of appointments){


  if((appointment.date >= today) && (appointment.status === "booked")){
    firstAppointment = appointment
    break
  }
}
