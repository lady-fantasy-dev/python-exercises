// You have a baby's health-record entries:
// We want to find all temperature measurements that are 38°C or higher.
// Expected output:
//   [
//     {"type": "temperature", "value": 38.2, "unit": "C"},
//     {"type": "temperature", "value": 38.7, "unit": "C"}
//   ]
// If there are no such measurements, return an empty list.

const records = [
  {"type": "temperature", "value": 38.2, "unit": "C"},
  {"type": "weight", "value": 5.4, "unit": "kg"},
  {"type": "temperature", "value": 37.1, "unit": "C"},
  {"type": "weight", "value": 5.6, "unit": "kg"},
  {"type": "temperature", "value": 38.7, "unit": "C"},
  {"type": "height", "value": 61, "unit": "cm"},
]

const results = records.filter(
  (records) => records.type === "temperature" && records.value >= 38
);
