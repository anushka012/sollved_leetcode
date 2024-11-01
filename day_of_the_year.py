class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))

        days_in_month_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        is_leap_year = (year%4 == 0 and year%100 != 0) or (year%400 == 0) 

        days_in_month = days_in_month_leap if is_leap_year else days_in_month_normal
    
        return sum(days_in_month[:month - 1]) + day   