
from datetime import datetime


def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
