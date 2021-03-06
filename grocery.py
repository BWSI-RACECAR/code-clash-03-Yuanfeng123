"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #3 - Combined Grocery List (grocery.py)


Author: Ainsley Ward

Difficulty Level: 2/10

Prompt: Sarah’s parents each gave her a grocery list to take with her to Trader Joes. 
She wants to quickly combine the lists into one, getting rid of duplicate items. 
Write a function that takes the two grocery lists (two strings) and returns the final 
grocery list (a list) that does not include duplicate items.

Test Cases:

Input: str1 = 'apples bananas bread sauce onions'; str2 = 'chocolate apples grapes bread';
Output: [apples, bananas, bread, sauce, onions, chocolate, grapes]

Input: str1 = 'apples bananas bread bananas'; str2 = 'grapes';
Output: [apples, bananas, bread, grapes]

Input: str1 = 'apples bananas bread bananas'; str2 = '';
Output: [apples, bananas, bread]
"""

class Solution:
    def my_grocery_list(self,str1,str2):
        # type str1:string
        # type str2: string
        # return: list

        # TODO: Write code below to return a list with the solution to the prompt
        # arr1 = str1.split(" ")
        # arr2 = str2.split(" ")
        # res = []
        # for i in range(len(arr1)):
        #     arr1[i] = arr1[i].strip("\r")
        #     res.append(arr1[i])
        # for j in range(len(arr2)):
        #     arr2[j] = arr2[j].strip("\r")
        #     if arr2[j] not in res:
        #         res.append(arr2[j])
        # return res
        res = []
        arr1 = str1.split(" ")
        arr1[len(arr1)-1] = arr1[len(arr1) - 1].strip()
        arr2 = str2.split(" ")
        arr2[len(arr2) - 1] = arr2[len(arr2) - 1].strip()
        for item in arr1:
            if item not in res and item != "":
                res.append(item)
        for item in arr2:
            if item not in res and item != "":
                res.append(item)
        return res

        

def main():
    string1 = input()
    string2 = input()

    tc1 = Solution()
    ans = tc1.my_grocery_list(string1,string2)
    print(ans)

if __name__ == "__main__":
     main()