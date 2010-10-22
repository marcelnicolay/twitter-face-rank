import base64
import hashlib
import hmac
import time
from twittface import settings

def set_secure_value(value, expires_days=30, **kwargs):
    timestamp = str(int(time.time()))
    value = base64.b64encode(value)
    signature = _signature(value, timestamp)
    value = "|".join([value, timestamp, signature])
    return value
        
def get_secure_value(value):
    parts = value.split("|")
    if len(parts) != 3: return None
    if _signature(parts[0], parts[1]) != parts[2]:
        logging.warning("Invalid cookie signature %r", value)
        return None
    timestamp = int(parts[1])
    if timestamp < time.time() - 31 * 86400:
        logging.warning("Expired value %r", value)
        return None
    try:
        return base64.b64decode(parts[0])
    except:
        return None

def _signature(*parts):
    
    hash = hmac.new(settings.COOKIE_SECRET, digestmod=hashlib.sha1)
    for part in parts: hash.update(part)
    return hash.hexdigest()
