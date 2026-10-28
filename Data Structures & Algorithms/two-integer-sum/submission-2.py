class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        potential_no = {}
        index = 0
        output = []

        for i in nums:
            complement = target - i
            if complement in potential_no:
                output.append(potential_no.get(complement))
                output.append(index)
                return output
            else:
                potential_no.update({i: index}) 
            index +=1

                        





        