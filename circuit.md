# 🔌 Circuit Connections

## PIR Motion Sensor

| PIR Sensor Pin | Raspberry Pi Pin | GPIO |
|----------------|------------------|------|
| VCC | Pin 2 | 5V |
| GND | Pin 6 | GND |
| OUT | Pin 11 | GPIO17 |

## LED

| LED Pin | Raspberry Pi Pin | GPIO |
|--------|------------------|------|
| Anode (+) | Pin 16 | GPIO23 |
| Cathode (-) | GND via 220Ω resistor | GND |

## Buzzer

| Buzzer Pin | Raspberry Pi Pin | GPIO |
|-----------|------------------|------|
| Positive (+) | Pin 18 | GPIO24 |
| Negative (-) | Pin 14 | GND |

## Connection Summary

| Component | GPIO Pin |
|----------|-----------|
| PIR Motion Sensor | GPIO17 |
| LED | GPIO23 |
| Buzzer | GPIO24 |
