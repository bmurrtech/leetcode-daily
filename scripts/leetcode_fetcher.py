import requests
from datetime import datetime
from typing import Dict, Any

class LeetCodeFetcher:
    def __init__(self):
        self.api_url = "https://leetcode.com/graphql"
        self.query = '''
        query questionOfToday {
          activeDailyCodingChallengeQuestion {
            date
            link
            question {
              questionId
              frontendQuestionId
              title
              titleSlug
              content
              difficulty
              topicTags {
                name
                slug
              }
            }
          }
        }'''
    
    def fetch_daily_problem(self) -> Dict[str, Any]:
        """Fetch today's LeetCode problem"""
        response = requests.post(
            self.api_url,
            json={"query": self.query, "operationName": "questionOfToday"},
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        
        data = response.json()
        problem = data["data"]["activeDailyCodingChallengeQuestion"]
        
        return {
            'date': problem['date'],
            'question_id': problem['question']['frontendQuestionId'],
            'title': problem['question']['title'],
            'slug': problem['question']['titleSlug'],
            'content': problem['question']['content'],
            'difficulty': problem['question']['difficulty'],
            'link': f"https://leetcode.com{problem['link']}",
            'topic_tags': [tag['name'] for tag in problem['question']['topicTags']],
            'filename': f"{int(problem['question']['frontendQuestionId']):03d}-{problem['question']['titleSlug']}.md"
        }
