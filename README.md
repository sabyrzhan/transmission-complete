# ▶️ ⏯ ✅ Move torrents to another folder downloaded by Transmission
This just moves downloaded Transmission torrents to another folder. It calls Transmission RPC using `transmission-rpc` library.

## Requirements
1. `python3`
2. Transmission client with enabled Remote support

## Usage
1. In `move.py` change:
    1. `TORRENTS_FOLDER` - source torrents folder
    2. `TARGET_FOLDER` - destination folder to move to
2. Execute `./run.sh`
