"""
Add Two Numbers (LeetCode 2)
=============================
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Add the two numbers and return the sum as a linked list, also in reverse order.

I solved this by walking through both lists at the same time, adding the digits
position by position and carrying over when the sum reaches 10 — the same way you
add numbers by hand.

Author: Mohamed Farouk Ben Salem
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # noeud fictif pour commencer
        current = dummy
        retenue = 0

        while l1 or l2 or retenue:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            somme = val1 + val2 + retenue
            chiffre = somme % 10
            retenue = somme // 10

            current.next = ListNode(chiffre)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# --- helpers to build and print linked lists for testing ---
def liste_vers_listnode(liste):
    dummy = ListNode(0)
    current = dummy
    for val in liste:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def afficher_listnode(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next


if __name__ == "__main__":
    l1 = liste_vers_listnode([2, 4, 3])  # représente 342
    l2 = liste_vers_listnode([5, 6, 4])  # représente 465

    resultat = Solution().addTwoNumbers(l1, l2)
    afficher_listnode(resultat)          # 7 -> 0 -> 8  (807 = 342 + 465)
