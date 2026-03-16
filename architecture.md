# System Architecture

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/4865a8f0-e79e-4674-a57f-89e16a3a5c30" />

## Overview
The Contactless IoT Doorbell & Security System detects a visitor near the door using a PIR motion sensor. The signal is sent to the Raspberry Pi, which processes the input and activates alert devices.

## Architecture Flow
Visitor → PIR Motion Sensor → Raspberry Pi → Buzzer & LED

## Components

| Component | Function |
|-----------|----------|
| PIR Motion Sensor | Detects motion near the door |
| Raspberry Pi | Processes the sensor signal |
| Buzzer | Produces doorbell alert sound |
| LED | Indicates visitor detection |
