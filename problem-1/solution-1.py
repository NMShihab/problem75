class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        # ToDo: Write Your Code Here.
        maximumCandies = self.kidWithMaximumCandies(candies)

        for numOfCadies in candies:
            if numOfCadies+extraCandies >= maximumCandies:
                result.append(True)
            else:
                result.append(False)

        return result


    def kidWithMaximumCandies(self,candies):
        max = 0

        for numOfCadies in candies:
            if max < numOfCadies:
                max = numOfCadies

        return max
