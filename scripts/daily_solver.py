import os
import asyncio
import subprocess
from pathlib import Path
import requests
from datetime import datetime
import json

from .leetcode_fetcher import LeetCodeFetcher
from .toolkit_client import OpticodegenClient  
from .markdown_generator import MarkdownGenerator

class DailyLeetCodeAutomation:
    def __init__(self):
        self.repo_root = Path(__file__).parent.parent
        self.solutions_dir = self.repo_root / "solutions"
        self.solutions_dir.mkdir(exist_ok=True)
        
        self.fetcher = LeetCodeFetcher()
        self.client = OpticodegenClient()
        self.generator = MarkdownGenerator()
        
        self.ntfy_url = os.getenv("NTFY_URL")
    
    async def run_daily_automation(self):
        """Main automation workflow"""
        try:
            print("🚀 Starting daily LeetCode automation...")
            
            # 1. Fetch today's problem
            print("📥 Fetching daily problem...")
            problem_data = self.fetcher.fetch_daily_problem()
            print(f"📋 Problem: {problem_data['title']} ({problem_data['difficulty']})")
            
            # 2. Check if already solved
            solution_file = self.solutions_dir / problem_data['filename']
            if solution_file.exists():
                print("✅ Problem already solved today!")
                return {'success': True, 'already_solved': True}
            
            # 3. Generate solution using opticodegen
            print("🧠 Generating solution using opticodegen toolkit...")
            solution_data = await self.client.solve_problem(problem_data)
            
            # 4. Create markdown file
            print("📝 Generating documentation...")
            markdown_content = self.generator.generate_solution_file(problem_data, solution_data)
            
            # 5. Write solution file
            with open(solution_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            # 6. Update README
            print("📚 Updating README...")
            self._update_readme()
            
            # 7. Git commit and push
            print("📤 Committing to GitHub...")
            self._git_commit_and_push(problem_data)
            
            # 8. Send notification
            print("📱 Sending notification...")
            self._send_notification(problem_data, solution_data, success=True)
            
            print("✅ Daily automation completed successfully!")
            return {'success': True, 'problem': problem_data['title']}
            
        except Exception as e:
            print(f"❌ Automation failed: {str(e)}")
            self._send_notification({}, {}, success=False, error=str(e))
            return {'success': False, 'error': str(e)}
    
    def _update_readme(self):
        """Update README with current solutions index"""
        solutions = []
        for solution_file in self.solutions_dir.glob("*.md"):
            # Parse solution file to get metadata
            # This is simplified - you could parse the actual files
            name_parts = solution_file.stem.split("-", 1)
            if len(name_parts) == 2:
                question_id = name_parts[0]
                title_slug = name_parts[1]
                solutions.append({
                    'question_id': question_id,
                    'title': title_slug.replace("-", " ").title(),
                    'filename': solution_file.name,
                    'difficulty': 'Medium'  # Could parse from file content
                })
        
        readme_content = self.generator.update_readme(solutions)
        with open(self.repo_root / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme_content)
    
    def _git_commit_and_push(self, problem_data):
        """Commit and push changes to GitHub"""
        try:
            os.chdir(self.repo_root)
            
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run([
                'git', 'commit', '-m', 
                f"Add solution for {problem_data['question_id']}: {problem_data['title']} ({problem_data['difficulty']})\n\n🤖 Auto-solved using opticodegen toolkit"
            ], check=True)
            subprocess.run(['git', 'push'], check=True)
            
        except Exception as e:
            raise Exception(f"Git operation failed: {e}")
    
    def _send_notification(self, problem_data, solution_data, success=True, error=None):
        """Send notification via ntfy"""
        if not self.ntfy_url:
            return
            
        if success and not error:
            message = f"""🎯 LeetCode Daily: {problem_data['title']}
🔗 {problem_data['link']}
📊 Difficulty: {problem_data['difficulty']}
🏷️ Tags: {', '.join(problem_data['topic_tags'][:3])}

✅ Auto-solved & committed to GitHub!
📋 Ready to copy & paste:

{solution_data.get('code', '')[:200]}...

🚀 Check your repo for full solution & explanation!"""
        else:
            message = f"❌ Daily LeetCode automation failed: {error}"
            
        try:
            requests.post(
                self.ntfy_url,
                data=message.encode("utf-8"),
                headers={
                    "Title": "LeetCode Daily",
                    "Priority": "default",
                    "Tags": "computer,code"
                }
            )
        except:
            pass  # Don't fail automation if notification fails

if __name__ == "__main__":
    automation = DailyLeetCodeAutomation()
    result = asyncio.run(automation.run_daily_automation())
    print(json.dumps(result, indent=2))
