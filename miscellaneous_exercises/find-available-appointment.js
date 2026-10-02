// Imagine the backend has a practitioner's available appointment times.
// A patient requests an appointment starting at or after a particular time. For example: requested_time = "10:15"

// Return the first available appointment slot that is at or after the patient's requested time.
// If there is no available slot after that time, return null.

let slots = [
    "09:00",
    "09:30",
    "10:00",
    "11:00",
    "14:00",
    "14:30",
    "15:00"
]

let requestedSlot = "10:15"

let appointment = null

for(let slot of slots) {
  if(slot >= requestedSlot){
    appointment = slot;
    break;
  }
}

console.log(appointment)
