problems = [
    {
        "id": 1,
        "title": "Two Sum",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
        "test_cases": ["[2,7,11,15]\n9", "[3,2,4]\n6", "[3,3]\n6"],
        "expected_outputs": ["[0,1]", "[1,2]", "[0,1]"]
    },
    {
        "id": 2,
        "title": "Reverse String",
        "description": "Write a function that reverses a string. The input string is given as an array of characters s.",
        "test_cases": ['["h","e","l","l","o"]', '["H","a","n","n","a","h"]'],
        "expected_outputs": ['["o","l","l","e","h"]', '["h","a","n","n","a","H"]']
    },
    {
        "id": 3,
        "title": "Fibonacci Number",
        "description": "Given n, calculate F(n), where F(n) is the n-th Fibonacci number.",
        "test_cases": ["2", "3", "4"],
        "expected_outputs": ["1", "2", "3"]
    },
    {
        "id": 4,
        "title": "Valid Parentheses",
        "description": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        "test_cases": ['"{()}"', '"({[)]"', '"()[]{}?"'],
        "expected_outputs": ["true", "false", "false"]
    },
    {
        "id": 5,
        "title": "Maximum Subarray",
        "description": "Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.",
        "test_cases": ["[-2,1,-3,4,-1,2,1,-5,4]", "[1]", "[5,4,-1,7,8]"],
        "expected_outputs": ["6", "1", "23"]
    },
    {
        "id": 6,
        "title": "Merge Two Sorted Lists",
        "description": "Merge two sorted linked lists and return it as a sorted list.",
        "test_cases": ["[1,2,4]\n[1,3,4]", "[]\n[]", "[]\n[0]"],
        "expected_outputs": ["[1,1,2,3,4,4]", "[]", "[0]"]
    },
    {
        "id": 7,
        "title": "Binary Search",
        "description": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.",
        "test_cases": ["[-1,0,3,5,9,12]\n9", "[-1,0,3,5,9,12]\n2"],
        "expected_outputs": ["4", "-1"]
    },
    {
        "id": 8,
        "title": "Climbing Stairs",
        "description": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
        "test_cases": ["2", "3", "4"],
        "expected_outputs": ["2", "3", "5"]
    },
    {
        "id": 9,
        "title": "Longest Palindromic Substring",
        "description": "Given a string s, return the longest palindromic substring in s.",
        "test_cases": ['"babad"', '"cbbd"', '"a"'],
        "expected_outputs": ['"bab"', '"bb"', '"a"']
    },
    {
        "id": 10,
        "title": "Container With Most Water",
        "description": "Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.",
        "test_cases": ["[1,8,6,2,5,4,8,3,7]", "[1,1]", "[4,3,2,1,4]"],
        "expected_outputs": ["49", "1", "16"]
    },
    {
        "id": 11,
        "title": "Rotate Image",
        "description": "You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).",
        "test_cases": ["[[1,2,3],[4,5,6],[7,8,9]]", "[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]"],
        "expected_outputs": ["[[7,4,1],[8,5,2],[9,6,3]]", "[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]"]
    },
    {
        "id": 12,
        "title": "Group Anagrams",
        "description": "Given an array of strings strs, group the anagrams together. You can return the answer in any order.",
        "test_cases": ['["eat","tea","tan","ate","nat","bat"]', '[""]', '["a"]'],
        "expected_outputs": ['[["bat"],["nat","tan"],["ate","eat","tea"]]', '[[""]]', '[["a"]]']
    },
    {
        "id": 13,
        "title": "Trapping Rain Water",
        "description": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
        "test_cases": ["[0,1,0,2,1,0,1,3,2,1,2,1]", "[4,2,0,3,2,5]"],
        "expected_outputs": ["6", "9"]
    }
]

def add_problem(problem):
    problem['id'] = len(problems) + 1
    problems.append(problem)