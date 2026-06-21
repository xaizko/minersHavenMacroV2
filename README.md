# Miners Haven Auto Rebirth Macro

This project is an automatic rebirth macro for Miners Haven. It watches a specific pixel on the screen and runs the rebirth sequence when the target color appears.

## What It Does

- Starts scanning the chosen monitor for a target pixel color.
- Triggers `rebirth()` when that color is detected.
- Uses configurable mouse coordinates and keyboard hotkeys.

## Setup

1. Run [getMousePosition.py](getMousePosition.py) to record the screen coordinates for each button you want to use.
2. Fill in the button positions in [settings.py](settings.py).
3. Set the correct monitor number in [settings.py](settings.py).
4. Make sure the target color in [settings.py](settings.py) matches the pixel you want to detect.
5. Start the macro with [macroV2.py](macroV2.py).

## Dependencies

Install these Python packages before running the macro:

- `pynput`
- `mss`
- `numpy`
 - `requests`

Install them with:

```bash
pip install pynput mss numpy requests
```

### Required Coordinates

Use [getMousePosition.py](getMousePosition.py) to get the coordinates for these points:

- Rebirth button
- Confirm rebirth button
- Open layouts / settings button
- Loadout 1 button
- Loadout 2 button
- Progress point being scanned

### Webhook screenshots

This project can optionally send a screenshot to a Discord webhook URL when you've successfully rebirthed. Add `WEBHOOK_URL` (your Discord webhook) to your `settings.py` if you want webhook support.


### Loadout Notes

The loading steps in [rebirth.py](rebirth.py) may need to be adjusted for your own setup.

Not everyone uses the same layouts or loadouts, so if your buttons or flow are different, you may need to edit the loadout section in [rebirth.py](rebirth.py) to match your game.

## Hotkeys

- `r` starts scanning.
- `q` pauses scanning.

These are defined in [settings.py](settings.py).

## Settings Reference

The main options live in [settings.py](settings.py):

- `BUTTON_COORDINATES`: Stores the x/y positions for all clickable UI elements.
- `START_KEY`: Key that begins scanning.
- `END_KEY`: Key that pauses scanning.
- `MONITOR_NUMBER`: Which monitor to capture with `mss`.
- `TARGET_COLOR`: The RGB color the scanner looks for.
- `SCAN_INTERVAL_SECONDS`: How often the scanner checks the pixel.
- `SCAN_TOLERANCE`: How close the detected color must be to `TARGET_COLOR`.
- `MONEY_DELAY_TIME`: Wait time used in the rebirth sequence before the next loadout click.
- `WEBHOOK_URL`: Your webhook url.
- `REGION`: The region in which your webhook screenshot will be taken

### Button Coordinates

The current coordinate names are:

- `REBIRTH`
- `REBIRTH_CONFIRM`
- `SETTINGS_OPEN`
- `LOAD1`
- `LOAD2`
- `PROGRESS_POINT`

## Monitor Check

If the scanner is not working, use [monitorCheck.py](monitorCheck.py) to verify which monitor number matches your display.

That script prints every monitor index and its screen bounds. In `mss`:

- `0` is the full virtual desktop
- `1` is the first monitor
- `2` is the second monitor
- and so on

If your game is on the wrong monitor, update `MONITOR_NUMBER` in [settings.py](settings.py) and try again.

## Notes

- Keep the game window focused when running the macro.
- If the scanner misses the target color, adjust `TARGET_COLOR` and `SCAN_TOLERANCE`.
- If clicks miss the UI, re-check the coordinates with [getMousePosition.py](getMousePosition.py).