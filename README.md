# Miners Haven Auto Rebirth Macro

Automatic rebirth macro and helper scripts for Miners Haven. It scans a pixel on your screen and runs a rebirth + loadout sequence when the configured progress color appears. Optional features include webhook screenshots, auto-rejoin, and auto-pulse.

**Quick features:**
- Pixel-based progress detection and automatic rebirth flow
- Optional Discord webhook screenshots on rebirth/resync (optional)
- Auto-rejoin when player is not detected in-game (optional)
- Auto-pulse after rebirth (optional)

## Quick Start

1. Install dependencies: see `requirements.txt`.
2. Run `getMousePosition.py` to collect coordinates.
3. Update `settings.py` (coordinates, monitor, target color, optional `.env` values).
4. (Optional) create a `.env` file from `.env.example` and set `WEBHOOK_URL` and `PLAYER_ID`.
5. Start the macro with `python macroV2.py` and press `r` to start scanning.

## Dependencies

Install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Packages used:
- `pynput` (keyboard/mouse controls)
- `mss` (screen capture)
- `numpy` (pixel processing)
- `requests` (optional webhooks & Roblox presence API)
- `python-dotenv` (optional `.env` support)

## Configuration

- `settings.py` holds coordinates, keys, colors, and toggles.
- `WEBHOOK_URL` and `PLAYER_ID` can be provided via environment variables (use `.env` with `python-dotenv`) or set directly in `settings.py`.

### Recommended workflow
1. Run `python getMousePosition.py` and click the UI elements to gather coordinates.
2. Paste coordinates into `settings.py` under `BUTTON_COORDINATES`.
3. Use `monitorCheck.py` if unsure which monitor index to use.
4. Adjust `TARGET_COLOR` and `SCAN_TOLERANCE` for reliable detection.

## Hotkeys
- `r`: Start scanning
- `q`: Pause scanning

## Optional environment variables (.env)
Create a `.env` file in the project root or use the provided `.env.example` with:

```
WEBHOOK_URL=https://discord.com/api/webhooks/your/webhook
PLAYER_ID=12345678
```

## Webhook screenshots
When `USE_WEBHOOK` is enabled and `WEBHOOK_URL` is set, the macro will capture the configured `REGION` and upload a PNG to the webhook on successful rebirth or resync events.

## Auto Rejoin
`autoRejoin.py` queries the Roblox presence API using `PLAYER_ID`. If the player is not in-game it will open the game link and attempt to resync the macro after joining. Use `AUTO_REJOIN_CHECK_INTERVAL_SECONDS` to control how often presence is checked.

## Safety and notes
- Keep the game window focused when running the macro.
- If detection fails, tweak `TARGET_COLOR`, `SCAN_TOLERANCE`, and `PROGRESS_POINT`.

## Troubleshooting
- Webhook errors: verify `WEBHOOK_URL` and network connectivity.
- Rate limits: the presence API can be rate limited; `autoRejoin.py` handles exceptions and reports via webhook if enabled.

## License & Attribution
This repo is provided as-is for personal use. Modify at your own risk.