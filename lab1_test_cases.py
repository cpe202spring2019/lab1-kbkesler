import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        list1 = []
        self.assertEqual(max_list_iter(list1), None) #to check for empty list       
        list2 = [1, 3, 8, 19, 42, 86, 4, 16]
        self.assertEqual(max_list_iter(list2), 86) #to check if function can find random max num
        list3 = [5, 5, 5]
        self.assertEqual(max_list_iter(list3), 5) #used to check if multiple of max number in list
        list4 = [-1, -16, -12, -8]
        self.assertEqual(max_list_iter(list4), -1) #used to check for negative numbers in list
        list5 = [0]
        self.assertEqual(max_list_iter(list5), 0) #used to check if only one number in list
        list6 = [1.6, 32.8, 41.1, 16.0]
        self.assertEqual(max_list_iter(list6), 41.1) #used to check for float max in list 
        list7 = [12, 4.1, 18, 18.1, 32.146]
        self.assertEqual(max_list_iter(list7), 32.146) #used to check for max at end of list
        list8 = [22, -8.5, 11, 0, 3.1]
        self.assertEqual(max_list_iter(list8), 22) #used to check for max at beggining of list

    def test_reverse_rec(self):
        list1 = None 
        with self.assertRaises(ValueError): #used to check for exception
            reverse_rec(list1)
        self.assertEqual(reverse_rec([]), []) #used to check for empty list 
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) #used to check if function can reverse list
        self.assertEqual(reverse_rec([4]), [4]) #used to check if only one number in list
        self.assertEqual(reverse_rec([16, -4, 11, 2, -18, -4]), [-4, -18, 2, 11, -4, 16]) # used to check if negative numbers in the list work
        self.assertEqual(reverse_rec([3.2, 4.6, 1, 12, 11.8, -11.8]), [-11.8, 11.8, 12, 1, 4.6, 3.2]) #used to check for float numbers in list
        self.assertEqual(reverse_rec([8, 8, 8, 8]), [8, 8, 8, 8]) #used to check for multiple pf the same number in list
        self.assertEqual(reverse_rec([-3, -3, -3]), [-3, -3, -3]) #used to check for multiple negative numbers in list
        self.assertEqual(reverse_rec([2.4, 2.4, 2.4]), [2.4, 2.4, 2.4]) #used to check for multiple float numbers in list

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) #used to check if binary search function works
        list1 = None
        with self.assertRaises(ValueError): #used to check for exception
            bin_search(6, 0, 6, list1)
        self.assertEqual(bin_search(6, 0, 5, [1, 8, 12, 14, 22, 36]), None) #used to check if target isn't in list
        self.assertEqual(bin_search(48, 0, 6, [-5, 0, 1, 16, 26, 29, 48]), 6) #used to check if target is at the end of the list
        self.assertEqual(bin_search(4, 0, 6, [-14, -9, -8, 4, 8, 11, 14]), 3) #used to check for target at the middle of the list
        self.assertEqual(bin_search(-6.2, 0, 4, [-6.2, 1.8, 3.1, 16.4, 28.9]), 0) #used to check for target at the beggining of the list
        self.assertEqual(bin_search(8.1, 0, 3, [8.1, 8.1, 8.1, 8.1]), 1) #used to check for an even number of multiple of the target number in the list
        self.assertEqual(bin_search(3, 0, 4, [3, 3, 3, 3, 3]), 2) #used to check for an odd number of multiple of the target number in the list

if __name__ == "__main__":
        unittest.main()

    
