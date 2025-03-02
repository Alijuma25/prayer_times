import datetime
import pytz

# Set the correct timezone
LOCAL_TZ = pytz.timezone("America/New_York")

# Prayer times indexed by (month, day) in 24-hour format
prayer_times = {
    (3, 1): {"Fajr": "05:31", "Sunrise": "06:55", "Dhuhr": "12:30", "Maghrib": "18:21", "Isha": "19:23"},
    (3, 2): {"Fajr": "05:29", "Sunrise": "06:54", "Dhuhr": "12:30", "Maghrib": "18:22", "Isha": "19:23"},
    (3, 3): {"Fajr": "05:27", "Sunrise": "06:52", "Dhuhr": "12:30", "Maghrib": "18:23", "Isha": "19:23"},
    (3, 4): {"Fajr": "05:26", "Sunrise": "06:50", "Dhuhr": "12:30", "Maghrib": "18:25", "Isha": "19:23"},
    (3, 5): {"Fajr": "05:24", "Sunrise": "06:48", "Dhuhr": "12:29", "Maghrib": "18:26", "Isha": "19:23"},
    (3, 6): {"Fajr": "05:22", "Sunrise": "06:47", "Dhuhr": "12:29", "Maghrib": "18:27", "Isha": "19:23"},
    (3, 7): {"Fajr": "05:20", "Sunrise": "06:45", "Dhuhr": "12:29", "Maghrib": "18:29", "Isha": "19:23"},
    (3, 8): {"Fajr": "05:19", "Sunrise": "06:43", "Dhuhr": "12:29", "Maghrib": "18:30", "Isha": "19:23"},
    (3, 9): {"Fajr": "05:17", "Sunrise": "06:41", "Dhuhr": "12:28", "Maghrib": "18:31", "Isha": "19:23"},
    (3, 10): {"Fajr": "06:15", "Sunrise": "07:40", "Dhuhr": "13:28", "Maghrib": "19:32", "Isha": "19:23"},
    (3, 11): {"Fajr": "06:13", "Sunrise": "07:38", "Dhuhr": "13:28", "Maghrib": "19:34", "Isha": "19:23"},
    (3, 12): {"Fajr": "06:11", "Sunrise": "07:36", "Dhuhr": "13:28", "Maghrib": "19:35", "Isha": "19:23"},
    (3, 13): {"Fajr": "06:10", "Sunrise": "07:34", "Dhuhr": "13:27", "Maghrib": "19:36", "Isha": "19:23"},
    (3, 14): {"Fajr": "06:08", "Sunrise": "07:32", "Dhuhr": "13:27", "Maghrib": "19:37", "Isha": "19:23"},
    (3, 15): {"Fajr": "06:06", "Sunrise": "07:31", "Dhuhr": "13:27", "Maghrib": "19:39", "Isha": "19:23"},
    (3, 16): {"Fajr": "06:04", "Sunrise": "07:29", "Dhuhr": "13:26", "Maghrib": "19:40", "Isha": "19:23"},
    (3, 17): {"Fajr": "06:02", "Sunrise": "07:27", "Dhuhr": "13:26", "Maghrib": "19:41", "Isha": "19:23"},
    (3, 18): {"Fajr": "06:00", "Sunrise": "07:25", "Dhuhr": "13:26", "Maghrib": "19:42", "Isha": "19:23"},
    (3, 19): {"Fajr": "05:58", "Sunrise": "07:23", "Dhuhr": "13:26", "Maghrib": "19:44", "Isha": "19:23"},
    (3, 20): {"Fajr": "05:56", "Sunrise": "07:21", "Dhuhr": "13:26", "Maghrib": "19:45", "Isha": "19:23"},
    (3, 21): {"Fajr": "05:54", "Sunrise": "07:19", "Dhuhr": "13:25", "Maghrib": "19:46", "Isha": "19:23"},
    (3, 22): {"Fajr": "05:52", "Sunrise": "07:17", "Dhuhr": "13:25", "Maghrib": "19:48", "Isha": "19:23"},
    (3, 23): {"Fajr": "05:50", "Sunrise": "07:15", "Dhuhr": "13:25", "Maghrib": "19:49", "Isha": "19:23"},
    (3, 24): {"Fajr": "05:48", "Sunrise": "07:13", "Dhuhr": "13:25", "Maghrib": "19:50", "Isha": "19:23"},
    (3, 25): {"Fajr": "05:46", "Sunrise": "07:11", "Dhuhr": "13:24", "Maghrib": "19:51", "Isha": "19:23"},
    (3, 26): {"Fajr": "05:44", "Sunrise": "07:09", "Dhuhr": "13:24", "Maghrib": "19:53", "Isha": "19:23"},
    (3, 27): {"Fajr": "05:42", "Sunrise": "07:07", "Dhuhr": "13:24", "Maghrib": "19:54", "Isha": "19:23"},
    (3, 28): {"Fajr": "05:40", "Sunrise": "07:05", "Dhuhr": "13:24", "Maghrib": "19:55", "Isha": "19:23"},
    (3, 29): {"Fajr": "05:38", "Sunrise": "07:03", "Dhuhr": "13:24", "Maghrib": "19:56", "Isha": "19:23"},
    (3, 30): {"Fajr": "05:36", "Sunrise": "07:01", "Dhuhr": "13:23", "Maghrib": "19:58", "Isha": "19:23"},
    (3, 31): {"Fajr": "05:34", "Sunrise": "06:59", "Dhuhr": "13:23", "Maghrib": "19:59", "Isha": "19:23"},
}

def get_current_date():
    """Returns the current month and day in the correct timezone."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)  
    local_now = now_utc.astimezone(LOCAL_TZ)  
    return local_now, (local_now.month, local_now.day)

def get_prayer_times():
    """Fetch and print prayer times in the required format."""
    local_now, date_key = get_current_date()

    if date_key not in prayer_times:
        print("No prayer times available for today.")
        return

    times = prayer_times[date_key]

    print("Prayer Times for today in Toronto/Canada:")
    print("=========================================")
    for name, time in times.items():
        print(f"{name}: {time}")

if __name__ == "__main__":
    get_prayer_times()
