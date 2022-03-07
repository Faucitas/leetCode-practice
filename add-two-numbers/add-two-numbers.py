# from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list_1 = [2,4,3]
list_2 = [5,6,4]

#
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#

def add_two_numbers(l1: list, l2: list):
    num1 = list_to_number(l1)
    num2 = list_to_number(l2)
    total = str(num1 + num2)
    final_list = [int(n) for n in total]
    final_list.reverse()
    print(final_list)
    return



def list_to_number(num_list):
    num_list.reverse()
    number = ""
    for num in num_list:
        number_str = str(num)
        number += number_str
    return int(number)


add_two_numbers(list_1, list_2)