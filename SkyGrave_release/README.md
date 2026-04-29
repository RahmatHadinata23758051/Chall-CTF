# SkyGrave

Category: Forensics

Difficulty: Medium

I got inspired by some firmware-flavored reversing tasks and wanted to make a small drone recovery exercise. Nothing too wild, probably just a little artifact triage, a bit of telemetry cleanup, and maybe one annoying proprietary format if you are unlucky.

The drone is gone. What survived is a companion module image, a telemetry log, a calibration export, and a radio capture from the last flight. Recover the note that the operator thought was no longer recoverable.

Files:
- `companion_firmware.bin`
- `telemetry.log`
- `calibration.json`
- `radio_frames.bin`
