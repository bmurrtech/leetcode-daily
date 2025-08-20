import pytest
import asyncio
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import tempfile
import shutil
from scripts.daily_solver import DailyLeetCodeAutomation

class TestDailyLeetCodeAutomation:
    
    def setup_method(self):
        # Create temporary directory for testing
        self.temp_dir = Path(tempfile.mkdtemp())
        self.solutions_dir = self.temp_dir / "solutions"
        self.solutions_dir.mkdir()
        
        # Mock the repo_root to point to our temp directory
        with patch('scripts.daily_solver.Path') as mock_path:
            mock_path.return_value.parent.parent = self.temp_dir
            self.automation = DailyLeetCodeAutomation()
            self.automation.repo_root = self.temp_dir
            self.automation.solutions_dir = self.solutions_dir
    
    def teardown_method(self):
        # Clean up temporary directory
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    @pytest.mark.asyncio
    async def test_run_daily_automation_already_solved(self):
        """Test early exit when problem already solved"""
        # Mock fetcher to return problem data
        mock_problem = {
            'title': 'Two Sum',
            'difficulty': 'Easy',
            'filename': 'test-problem.md'
        }
        self.automation.fetcher.fetch_daily_problem = Mock(return_value=mock_problem)
        
        # Create existing solution file
        solution_file = self.solutions_dir / mock_problem['filename']
        solution_file.write_text("# Existing solution")
        
        result = await self.automation.run_daily_automation()
        
        assert result['success'] is True
        assert result['already_solved'] is True

    @pytest.mark.asyncio
    async def test_run_daily_automation_new_problem_success(self):
        """Test successful automation for new problem"""
        mock_problem = {
            'title': 'New Problem',
            'question_id': '999', 
            'difficulty': 'Medium',
            'filename': 'new-problem.md',
            'topic_tags': ['Array'],
            'link': 'https://leetcode.com/problems/new-problem/'
        }
        
        mock_solution = {
            'code': 'def solution():\n    pass',
            'explanation': 'Test explanation',
            'approach': 'Test approach',
            'complexity_analysis': 'O(1)'
        }
        
        # Mock all dependencies
        self.automation.fetcher.fetch_daily_problem = Mock(return_value=mock_problem)
        
        # Create async mock for solve_problem
        async def mock_solve_problem(problem_data):
            return mock_solution
        self.automation.client.solve_problem = mock_solve_problem
        self.automation.generator.generate_solution_file = Mock(return_value="# Generated markdown")
        self.automation._git_commit_and_push = Mock()
        self.automation._send_notification = Mock()
        
        # Mock _update_readme method
        self.automation._update_readme = Mock()
        
        result = await self.automation.run_daily_automation()
        
        # Verify success
        assert result['success'] is True
        assert result['problem'] == mock_problem['title']
        
        # Verify file was created
        solution_file = self.solutions_dir / mock_problem['filename']
        assert solution_file.exists()
        assert solution_file.read_text() == "# Generated markdown"
        
        # Verify methods were called (can't verify async function calls)
        self.automation.generator.generate_solution_file.assert_called_once_with(mock_problem, mock_solution)
        self.automation._update_readme.assert_called_once()
        self.automation._git_commit_and_push.assert_called_once_with(mock_problem)
        self.automation._send_notification.assert_called_once()

    @pytest.mark.asyncio 
    async def test_run_daily_automation_error_handling(self):
        """Test error handling in automation"""
        # Mock fetcher to raise exception
        self.automation.fetcher.fetch_daily_problem = Mock(side_effect=Exception("API Error"))
        self.automation._send_notification = Mock()
        
        result = await self.automation.run_daily_automation()
        
        assert result['success'] is False
        assert 'error' in result
        assert "API Error" in result['error']
        
        # Verify error notification was sent
        self.automation._send_notification.assert_called_once()

    def test_update_readme_with_existing_solutions(self):
        """Test README update with existing solution files"""
        # Create mock solution files
        solution1 = self.solutions_dir / "001-two-sum.md"
        solution1.write_text("# Two Sum solution")
        
        solution2 = self.solutions_dir / "002-add-numbers.md" 
        solution2.write_text("# Add numbers solution")
        
        # Mock generator
        self.automation.generator.update_readme = Mock(return_value="# Updated README")
        
        # Create README file to write to
        readme_file = self.temp_dir / "README.md"
        
        self.automation._update_readme()
        
        # Verify generator was called with parsed solutions
        call_args = self.automation.generator.update_readme.call_args[0][0]
        assert len(call_args) == 2
        
        # Check that solutions were parsed correctly
        solution_ids = [s['question_id'] for s in call_args]
        assert '001' in solution_ids
        assert '002' in solution_ids
        
        # Verify README was written
        assert readme_file.exists()
        assert readme_file.read_text() == "# Updated README"

    def test_git_commit_and_push_success(self):
        """Test successful git operations"""
        problem_data = {
            'question_id': '1',
            'title': 'Test Problem',
            'difficulty': 'Easy'
        }
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0)
            
            # Should not raise exception
            self.automation._git_commit_and_push(problem_data)
            
            # Verify git commands were called
            assert mock_run.call_count == 3  # add, commit, push
            
            calls = mock_run.call_args_list
            assert calls[0][0][0] == ['git', 'add', '.']
            assert calls[1][0][0][0:2] == ['git', 'commit']
            assert calls[2][0][0] == ['git', 'push']

    def test_git_commit_and_push_failure(self):
        """Test git operation failure handling"""
        problem_data = {'question_id': '1', 'title': 'Test', 'difficulty': 'Easy'}
        
        with patch('subprocess.run') as mock_run:
            mock_run.side_effect = Exception("Git failed")
            
            with pytest.raises(Exception) as exc_info:
                self.automation._git_commit_and_push(problem_data)
            
            assert "Git operation failed" in str(exc_info.value)
