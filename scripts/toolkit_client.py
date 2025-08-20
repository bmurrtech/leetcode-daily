import os
import requests
from typing import Dict, Any
import asyncio
import aiohttp

class OpticodegenClient:
    def __init__(self):
        self.base_url = os.getenv("OPTICODEGEN_API_URL", "https://your-opticodegen.railway.app")
        self.timeout = 120  # 2 minutes for complex problems
    
    async def solve_problem(self, problem_data: Dict[str, Any]) -> Dict[str, Any]:
        """Call the opticodegen toolkit to solve the problem"""
        
        async with aiohttp.ClientSession() as session:
            # Step 1: Analyze the problem
            analysis = await self._analyze_problem(session, problem_data)
            
            # Step 2: Generate solution
            solution = await self._generate_solution(session, analysis, problem_data)
            
            # Step 3: Optimize solution
            optimized = await self._optimize_solution(session, solution)
            
            return {
                'code': optimized.get('final_solution', solution.get('code', '')),
                'explanation': optimized.get('explanation', solution.get('explanation', '')),
                'complexity_analysis': optimized.get('complexity_analysis', ''),
                'approach': analysis.get('best_approach', ''),
                'optimization_notes': optimized.get('optimization_notes', [])
            }
    
    async def _analyze_problem(self, session, problem_data):
        """Analyze problem using opticodegen API"""
        payload = {
            "problem_text": problem_data['content'],
            "constraints": f"Difficulty: {problem_data['difficulty']}, Tags: {', '.join(problem_data['topic_tags'])}"
        }
        
        async with session.post(
            f"{self.base_url}/api/analyze-problem",
            json=payload,
            timeout=self.timeout
        ) as response:
            response.raise_for_status()
            return await response.json()
    
    async def _generate_solution(self, session, analysis, problem_data):
        """Generate solution using opticodegen API"""
        payload = {
            "problem_analysis": analysis,
            "language": "python3"
        }
        
        async with session.post(
            f"{self.base_url}/api/generate-solution", 
            json=payload,
            timeout=self.timeout
        ) as response:
            response.raise_for_status()
            return await response.json()
    
    async def _optimize_solution(self, session, solution):
        """Optimize solution using opticodegen API"""
        payload = {
            "code": solution.get('code', ''),
            "test_results": {},
            "optimization_target": "readability"
        }
        
        async with session.post(
            f"{self.base_url}/api/optimize-solution",
            json=payload, 
            timeout=self.timeout
        ) as response:
            response.raise_for_status()
            return await response.json()
