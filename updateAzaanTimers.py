import datetime
import pytz

# Set the correct timezone
LOCAL_TZ = pytz.timezone("America/New_York")

# Prayer times indexed by (month, day) in 24-hour format
prayer_times = {
    (3, 1): {"Imsac": "5:26", "Fajr": "5:31", "Sunrise": "6:55", "Zuhr": "12:30", "Sunset": "18:06", "Maghrib": "18:21"},
    (3, 2): {"Imsac": "5:24", "Fajr": "5:29", "Sunrise": "6:54", "Zuhr": "12:30", "Sunset": "18:07", "Maghrib": "18:22"},
    (3, 3): {"Imsac": "5:22", "Fajr": "5:27", "Sunrise": "6:52", "Zuhr": "12:30", "Sunset": "18:08", "Maghrib": "18:23"},
    (3, 4): {"Imsac": "5:21", "Fajr": "5:26", "Sunrise": "6:50", "Zuhr": "12:30", "Sunset": "18:10", "Maghrib": "18:25"},
    (3, 5): {"Imsac": "5:19", "Fajr": "5:24", "Sunrise": "6:48", "Zuhr": "12:29", "Sunset": "18:11", "Maghrib": "18:26"},
    (3, 6): {"Imsac": "5:17", "Fajr": "5:22", "Sunrise": "6:47", "Zuhr": "12:29", "Sunset": "18:12", "Maghrib": "18:27"},
    (3, 7): {"Imsac": "5:15", "Fajr": "5:20", "Sunrise": "6:45", "Zuhr": "12:29", "Sunset": "18:14", "Maghrib": "18:29"},
    (3, 8): {"Imsac": "5:14", "Fajr": "5:19", "Sunrise": "6:43", "Zuhr": "12:29", "Sunset": "18:15", "Maghrib": "18:30"},
    (3, 9): {"Imsac": "5:12", "Fajr": "5:17", "Sunrise": "6:41", "Zuhr": "12:28", "Sunset": "18:16", "Maghrib": "18:31"},
    (3, 10): {"Imsac": "6:10", "Fajr": "6:15", "Sunrise": "7:40", "Zuhr": "1:28", "Sunset": "19:17", "Maghrib": "19:32"},
    (3, 11): {"Imsac": "6:08", "Fajr": "6:13", "Sunrise": "7:38", "Zuhr": "1:28", "Sunset": "19:19", "Maghrib": "19:34"},
    (3, 12): {"Imsac": "6:06", "Fajr": "6:11", "Sunrise": "7:36", "Zuhr": "1:28", "Sunset": "19:20", "Maghrib": "19:35"},
    (3, 13): {"Imsac": "6:05", "Fajr": "6:10", "Sunrise": "7:34", "Zuhr": "1:27", "Sunset": "19:21", "Maghrib": "19:36"},
    (3, 14): {"Imsac": "6:03", "Fajr": "6:08", "Sunrise": "7:32", "Zuhr": "1:27", "Sunset": "19:22", "Maghrib": "19:37"},
    (3, 15): {"Imsac": "6:01", "Fajr": "6:06", "Sunrise": "7:31", "Zuhr": "1:27", "Sunset": "19:24", "Maghrib": "19:39"},
    (3, 16): {"Imsac": "5:59", "Fajr": "6:04", "Sunrise": "7:29", "Zuhr": "1:26", "Sunset": "19:25", "Maghrib": "19:40"},
    (3, 17): {"Imsac": "5:57", "Fajr": "6:02", "Sunrise": "7:27", "Zuhr": "1:26", "Sunset": "19:26", "Maghrib": "19:41"},
    (3, 18): {"Imsac": "5:55", "Fajr": "6:00", "Sunrise": "7:25", "Zuhr": "1:26", "Sunset": "19:27", "Maghrib": "19:42"},
    (3, 19): {"Imsac": "5:53", "Fajr": "5:58", "Sunrise": "7:23", "Zuhr": "1:26", "Sunset": "19:29", "Maghrib": "19:44"},
    (3, 20): {"Imsac": "5:51", "Fajr": "5:56", "Sunrise": "7:22", "Zuhr": "1:25", "Sunset": "19:30", "Maghrib": "19:45"},
    (3, 21): {"Imsac": "5:49", "Fajr": "5:54", "Sunrise": "7:20", "Zuhr": "1:25", "Sunset": "19:31", "Maghrib": "19:46"},
    (3, 22): {"Imsac": "5:47", "Fajr": "5:52", "Sunrise": "7:18", "Zuhr": "1:25", "Sunset": "19:32", "Maghrib": "19:47"},
    (3, 23): {"Imsac": "5:45", "Fajr": "5:50", "Sunrise": "7:16", "Zuhr": "1:24", "Sunset": "19:33", "Maghrib": "19:48"},
    (3, 24): {"Imsac": "5:43", "Fajr": "5:48", "Sunrise": "7:14", "Zuhr": "1:24", "Sunset": "19:35", "Maghrib": "19:50"},
    (3, 25): {"Imsac": "5:41", "Fajr": "5:46", "Sunrise": "7:13", "Zuhr": "1:24", "Sunset": "19:36", "Maghrib": "19:51"},
    (3, 26): {"Imsac": "5:39", "Fajr": "5:44", "Sunrise": "7:11", "Zuhr": "1:24", "Sunset": "19:37", "Maghrib": "19:52"},
    (3, 27): {"Imsac": "5:37", "Fajr": "5:42", "Sunrise": "7:09", "Zuhr": "1:23", "Sunset": "19:38", "Maghrib": "19:53"},
    (3, 28): {"Imsac": "5:35", "Fajr": "5:40", "Sunrise": "7:07", "Zuhr": "1:23", "Sunset": "19:39", "Maghrib": "19:54"},
    (3, 29): {"Imsac": "5:33", "Fajr": "5:38", "Sunrise": "7:05", "Zuhr": "1:23", "Sunset": "19:41", "Maghrib": "19:56"},
    (3, 30): {"Imsac": "5:31", "Fajr": "5:36", "Sunrise": "7:03", "Zuhr": "1:22", "Sunset": "19:42", "Maghrib": "19:57"},
    (3, 31): {"Imsac": "5:29", "Fajr": "5:34", "Sunrise": "7:02", "Zuhr": "1:22", "Sunset": "19:43", "Maghrib": "19:58"},
}

def get_current_date():
    """Returns the current month and day in the correct timezone."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)  # Get UTC time
    local_now = now_utc.astimezone(LOCAL_TZ)  # Convert to local timezone
    return local_now, (local_now.month, local_now.day)

def get_prayer_times():
    """Fetch and print prayer times in 24-hour format."""
    local_now, date_key = get_current_date()

    if date_key not in prayer_times:
        return

    times = prayer_times[date_key]

    for time in times.values():
        # Convert to 24-hour format explicitly to avoid issues
        formatted_time = datetime.datetime.strptime(time, "%H:%M").strftime("%H:%M")
        print(formatted_time)

if __name__ == "__main__":
    get_prayer_times()
