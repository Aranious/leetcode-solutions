class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day(date: str) -> int:
            m = int(date[:2])
            d = int(date[3:])
            return sum(days_in_month[:m - 1]) + d

        a_start = to_day(arriveAlice)
        a_end   = to_day(leaveAlice)
        b_start = to_day(arriveBob)
        b_end   = to_day(leaveBob)

        start = max(a_start, b_start)
        end   = min(a_end, b_end)

        return max(0, end - start + 1)