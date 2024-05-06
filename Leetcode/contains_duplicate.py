def containsDuplicate(nums: list[int]) -> bool:
        obj = {}
        isDuplicate:[bool] = False
        for num in nums:
                # print('num', num)
                # print('isFound', obj.get(num) != None)
                if obj.get(num) != None:
                        isDuplicate = True
                        break;
                else:
                        obj[num] = True


        return isDuplicate

print(containsDuplicate([1,2,3,1,6,7]))