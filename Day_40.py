# 228. Summary Ranges

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        range_out = []
        if not nums:
            return range_out

        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    range_out.append(str(start))
                else:
                    range_out.append("{}->{}".format(start, nums[i - 1]))
                start = nums[i]

        # Handle the last range
        if start == nums[-1]:
            range_out.append(str(start))
        else:
            range_out.append("{}->{}".format(start, nums[-1]))

        return range_out

# had to use chat gpt to refine

