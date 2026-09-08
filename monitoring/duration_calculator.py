from datetime import datetime, timezone


class DurationCalculator:

    @staticmethod
    def ms_to_datetime(milliseconds):

        if milliseconds is None:
            return None

        # Convert to UTC datetime
        return datetime.fromtimestamp(milliseconds / 1000, tz=timezone.utc)

    @staticmethod
    def calculate_duration(start, end):

        if start is None or end is None:
            return None

        # Ensure timezone-aware
        if start.tzinfo is None:
            start = start.replace(tzinfo=timezone.utc)

        if end.tzinfo is None:
            end = end.replace(tzinfo=timezone.utc)

        diff = end - start

        total_seconds = int(diff.total_seconds())

        minutes = total_seconds // 60
        seconds = total_seconds % 60

        return f"{minutes}m {seconds:02}s"