class config:
    global token; token = '' # Your token
    global prefix; prefix = [
        's.'
    ] # List of prefixes. Can be one or multiple
    global logging; logging = True # Whether to log stuff like people leaving, joining etc.
    global errorLogging; errorLogging = "channel" # 'channel', 'console' or None
# NOTE: Anything other than 'channel' or 'console' will disable error logging
    global timestamps; timestamps = False # Whether to show timestamps in the log

    global nitro_sniper; nitro_sniper = True
    global nitro_sniper_url; nitro_sniper_url = '' # Nitro sniper URL
