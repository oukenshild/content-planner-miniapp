import hmac, hashlib, os
from urllib.parse import parse_qsl

BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "")

def verify_init_data(init_data: str) -> bool:
    data = dict(parse_qsl(init_data, keep_blank_values=True))
    hash_ = data.pop("hash", None)
    check_str = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))
    secret = hmac.new(b"WebAppData", BOT_TOKEN.encode(), hashlib.sha256).digest()
    calc = hmac.new(secret, check_str.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(calc, hash_ or "")