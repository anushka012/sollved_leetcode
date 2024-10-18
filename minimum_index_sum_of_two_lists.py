class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_words = set(list1) & set(list2)
        index_1 = {}
        index_2 = {}
        min_sum = float('inf')

        for i in range(len(list1)):
            if list1[i] in common_words:
                index_1[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in common_words:
                index_2[list2[i]] = i

        for i in common_words:
            index_sum = index_1[i] + index_2[i]

            if index_sum < min_sum:
                min_sum = index_sum
                result = [i]
            elif index_sum == min_sum:
                result.append(i)
            
        return result