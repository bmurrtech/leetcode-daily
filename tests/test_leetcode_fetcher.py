import pytest
import responses
from scripts.leetcode_fetcher import LeetCodeFetcher

class TestLeetCodeFetcher:
    def setup_method(self):
        self.fetcher = LeetCodeFetcher()

    @responses.activate
    def test_fetch_daily_problem_success(self):
        """Test successful fetching of daily problem"""
        mock_response = {
            "data": {
                "activeDailyCodingChallengeQuestion": {
                    "date": "2023-08-20",
                    "link": "/problems/two-sum/",
                    "question": {
                        "questionId": "1",
                        "frontendQuestionId": "1",
                        "title": "Two Sum", 
                        "titleSlug": "two-sum",
                        "content": "<p>Given an array of integers...</p>",
                        "difficulty": "Easy",
                        "topicTags": [
                            {"name": "Array", "slug": "array"},
                            {"name": "Hash Table", "slug": "hash-table"}
                        ]
                    }
                }
            }
        }
        
        responses.add(
            responses.POST,
            "https://leetcode.com/graphql",
            json=mock_response,
            status=200
        )
        
        result = self.fetcher.fetch_daily_problem()
        
        # Verify all required fields are present
        assert 'date' in result
        assert 'question_id' in result
        assert 'title' in result
        assert 'slug' in result
        assert 'content' in result
        assert 'difficulty' in result
        assert 'link' in result
        assert 'topic_tags' in result
        assert 'filename' in result
        
        # Verify specific values
        assert result['date'] == "2023-08-20"
        assert result['question_id'] == "1"
        assert result['title'] == "Two Sum"
        assert result['slug'] == "two-sum"
        assert result['difficulty'] == "Easy"
        assert result['link'] == "https://leetcode.com/problems/two-sum/"
        assert result['topic_tags'] == ["Array", "Hash Table"]
        assert result['filename'] == "001-two-sum.md"

    @responses.activate  
    def test_fetch_daily_problem_api_error(self):
        """Test handling of API errors"""
        responses.add(
            responses.POST,
            "https://leetcode.com/graphql",
            status=500
        )
        
        with pytest.raises(Exception):
            self.fetcher.fetch_daily_problem()
