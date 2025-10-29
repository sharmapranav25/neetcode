class Solution:
    def twoSum(self, numbers, target: int):
        start, end = 0 , len(numbers)-1

        def check_back_side(start, end):
            remainder = target - numbers[start]
            if remainder > numbers[end]:
                return check_back_side(start +1, end)
            elif remainder == numbers[end]:
                return [start+1, end+1]
            else:
                return check_back_side(start, end -1)

        return check_back_side(start, end)
        