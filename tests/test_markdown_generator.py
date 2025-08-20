import pytest
from datetime import datetime
from scripts.markdown_generator import MarkdownGenerator

class TestMarkdownGenerator:
    
    def test_generate_solution_file_basic(self):
        """Test basic markdown generation for solution file"""
        problem_data = {
            'question_id': '1',
            'title': 'Two Sum',
            'link': 'https://leetcode.com/problems/two-sum/',
            'topic_tags': ['Array', 'Hash Table'],
            'difficulty': 'Easy'
        }
        
        solution_data = {
            'code': 'def two_sum(nums, target):\n    return []',
            'explanation': 'This is a test explanation',
            'approach': 'Use hash table for O(n) solution',
            'complexity_analysis': 'Time: O(n), Space: O(n)'
        }
        
        result = MarkdownGenerator.generate_solution_file(problem_data, solution_data)
        
        # Verify required sections are present
        assert f"## {problem_data['question_id']}. {problem_data['title']}" in result
        assert problem_data['link'] in result
        assert solution_data['explanation'] in result
        assert solution_data['approach'] in result
        assert solution_data['complexity_analysis'] in result
        assert '### Python' in result
        assert solution_data['code'] in result
        assert f"**Tags:** {', '.join(problem_data['topic_tags'])}" in result
        assert f"**Difficulty:** {problem_data['difficulty']}" in result
        assert "**Generated:**" in result
        assert "opticodegen toolkit" in result

    def test_generate_solution_file_with_optimization_notes(self):
        """Test markdown generation with optimization notes"""
        problem_data = {
            'question_id': '2',
            'title': 'Add Two Numbers',
            'link': 'https://leetcode.com/problems/add-two-numbers/',
            'topic_tags': ['Linked List', 'Math'],
            'difficulty': 'Medium'
        }
        
        solution_data = {
            'code': 'def add_two_numbers(l1, l2):\n    return None',
            'explanation': 'Add two linked lists',
            'optimization_notes': [
                'Consider edge cases with different lengths',
                'Handle carry properly'
            ]
        }
        
        result = MarkdownGenerator.generate_solution_file(problem_data, solution_data)
        
        assert "**Optimization Notes:**" in result
        assert "- Consider edge cases with different lengths" in result
        assert "- Handle carry properly" in result

    def test_update_readme_empty_list(self):
        """Test README generation with empty solutions list"""
        solutions = []
        
        result = MarkdownGenerator.update_readme(solutions)
        
        assert "# LeetCode Solutions" in result
        assert "**Total Problems Solved:** 0" in result
        assert "**Easy:** 0 | **Medium:** 0 | **Hard:** 0" in result
        assert "**Current Streak:** 0 days" in result
        assert "**Last Updated:**" in result
        assert "### Easy (0)" in result
        assert "### Medium (0)" in result  
        assert "### Hard (0)" in result
        assert "opticodegen toolkit" in result

    def test_update_readme_with_solutions(self):
        """Test README generation with various difficulty solutions"""
        solutions = [
            {
                'question_id': '1',
                'title': 'Two Sum',
                'filename': '001-two-sum.md',
                'difficulty': 'Easy'
            },
            {
                'question_id': '2',
                'title': 'Add Two Numbers', 
                'filename': '002-add-two-numbers.md',
                'difficulty': 'Medium'
            },
            {
                'question_id': '4',
                'title': 'Median of Two Sorted Arrays',
                'filename': '004-median-of-two-sorted-arrays.md', 
                'difficulty': 'Hard'
            }
        ]
        
        result = MarkdownGenerator.update_readme(solutions)
        
        assert "**Total Problems Solved:** 3" in result
        assert "**Easy:** 1 | **Medium:** 1 | **Hard:** 1" in result
        assert "**Current Streak:** 3 days" in result
        
        # Check that each solution is listed in correct section
        assert "### Easy (1)" in result
        assert "- [1. Two Sum](./solutions/001-two-sum.md)" in result
        
        assert "### Medium (1)" in result
        assert "- [2. Add Two Numbers](./solutions/002-add-two-numbers.md)" in result
        
        assert "### Hard (1)" in result
        assert "- [4. Median of Two Sorted Arrays](./solutions/004-median-of-two-sorted-arrays.md)" in result
