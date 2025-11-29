from messages import ADVENT_MESSAGES

# Store of opened doors per user { user_id: [days opened] }
opened = {}


def open_door(user_id: int, day: int):
    """
    Returns:
    {
        "status": "ok" | "already_opened",
        "content": "<text>"
    }
    """

    if user_id not in opened:
        opened[user_id] = []

    if day in opened[user_id]:
        return {"status": "already_opened"}

    opened[user_id].append(day)

    return {
        "status": "ok",
        "content": ADVENT_MESSAGES.get(day, "🎁 Nothing here (yet)! Add content in messages.py.")
    }

