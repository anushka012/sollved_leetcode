import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = datetime.date(year, month, day)

        # Get the day of the week in string format
        day_name = date.strftime("%A")
        return day_name