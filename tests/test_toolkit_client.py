import pytest
import asyncio
from aioresponses import aioresponses
from scripts.toolkit_client import OpticodegenClient

class TestOpticodegenClient:
    
    def setup_method(self):
        self.client = OpticodegenClient()
        # Override base URL for testing
        self.client.base_url = "https://test-api.example.com"
        
    @pytest.mark.asyncio
    async def test_solve_problem_success(self):
        """Test successful problem solving workflow"""
        problem_data = {
            'content': '<p>Given an array of integers...</p>',
            'difficulty': 'Easy',
            'topic_tags': ['Array', 'Hash Table']
        }
        
        mock_analysis = {
            'best_approach': 'Use hash table for O(n) lookup',
            'complexity': 'O(n) time, O(n) space'
        }
        
        mock_solution = {
            'code': 'def two_sum(nums, target):\n    return []',
            'explanation': 'Hash table approach explanation'
        }
        
        mock_optimized = {
            'final_solution': 'def two_sum(nums, target):\n    # Optimized version\n    return []',
            'explanation': 'Optimized explanation',
            'complexity_analysis': 'Time: O(n), Space: O(n)',
            'optimization_notes': ['Added early exit', 'Improved readability']
        }
        
        with aioresponses() as mock:
            # Mock analyze endpoint
            mock.post(
                f"{self.client.base_url}/api/analyze-problem",
                payload=mock_analysis
            )
            
            # Mock generate endpoint  
            mock.post(
                f"{self.client.base_url}/api/generate-solution",
                payload=mock_solution
            )
            
            # Mock optimize endpoint
            mock.post(
                f"{self.client.base_url}/api/optimize-solution", 
                payload=mock_optimized
            )
            
            result = await self.client.solve_problem(problem_data)
            
            # Verify result structure
            assert 'code' in result
            assert 'explanation' in result
            assert 'complexity_analysis' in result
            assert 'approach' in result
            assert 'optimization_notes' in result
            
            # Verify specific values
            assert result['code'] == mock_optimized['final_solution']
            assert result['explanation'] == mock_optimized['explanation']
            assert result['complexity_analysis'] == mock_optimized['complexity_analysis']
            assert result['approach'] == mock_analysis['best_approach']
            assert result['optimization_notes'] == mock_optimized['optimization_notes']

    @pytest.mark.asyncio
    async def test_solve_problem_fallback_to_solution(self):
        """Test fallback when optimization fails"""
        problem_data = {
            'content': '<p>Test problem</p>',
            'difficulty': 'Medium',
            'topic_tags': ['Dynamic Programming']
        }
        
        mock_analysis = {'best_approach': 'DP approach'}
        mock_solution = {
            'code': 'def solution():\n    pass',
            'explanation': 'Basic explanation'
        }
        
        with aioresponses() as mock:
            mock.post(
                f"{self.client.base_url}/api/analyze-problem",
                payload=mock_analysis
            )
            
            mock.post(
                f"{self.client.base_url}/api/generate-solution",
                payload=mock_solution
            )
            
            # Mock optimize endpoint to return empty response (fallback case)
            mock.post(
                f"{self.client.base_url}/api/optimize-solution",
                payload={}
            )
            
            result = await self.client.solve_problem(problem_data)
            
            # Should fallback to solution data when optimization is empty
            assert result['code'] == mock_solution['code']
            assert result['explanation'] == mock_solution['explanation']
            assert result['approach'] == mock_analysis['best_approach']
            assert result['optimization_notes'] == []

    @pytest.mark.asyncio
    async def test_solve_problem_api_error(self):
        """Test handling of API errors"""
        problem_data = {
            'content': '<p>Test problem</p>',
            'difficulty': 'Hard',
            'topic_tags': ['Graph']
        }
        
        with aioresponses() as mock:
            # Mock analyze endpoint to return 500 error
            mock.post(
                f"{self.client.base_url}/api/analyze-problem",
                status=500
            )
            
            with pytest.raises(Exception):
                await self.client.solve_problem(problem_data)
