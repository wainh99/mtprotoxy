PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "user1":  "00000000000000000000000000000001",
    # "user2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the service harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the service even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are forwarded there
# Use random existing domain, service checks it on start
# TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from the bot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
