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
        
        # Email notification settings
        self.mailgun_api_key = os.getenv("MAILGUN_API_KEY")
        self.mailgun_domain = os.getenv("MAILGUN_DOMAIN")
        self.email_recipient = os.getenv("EMAIL_RECIPIENT")
        
        # Keep ntfy_url for future feature (unused for now)
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
        """Send email notification via Mailgun"""
        if not self.mailgun_api_key or not self.mailgun_domain or not self.email_recipient:
            print("⚠️  Email notification skipped: Missing Mailgun configuration")
            return
            
        try:
            if success and not error:
                subject = f"🎯 LeetCode Daily: {problem_data.get('title', 'Problem Solved')}"
                
                # Create HTML email with copy-pasteable code
                html_body = f"""
                <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <h2 style="color: #2e7d32;">🎯 LeetCode Daily Solution Ready!</h2>
                    
                    <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0;">
                        <h3>📋 Problem Details</h3>
                        <p><strong>Title:</strong> {problem_data.get('title', 'N/A')}</p>
                        <p><strong>Difficulty:</strong> <span style="color: {'#ff9800' if problem_data.get('difficulty') == 'Medium' else '#4caf50' if problem_data.get('difficulty') == 'Easy' else '#f44336'}">{problem_data.get('difficulty', 'N/A')}</span></p>
                        <p><strong>Tags:</strong> {', '.join(problem_data.get('topic_tags', [])[:3])}</p>
                        <p><strong>Link:</strong> <a href="{problem_data.get('link', '#')}" style="color: #1976d2;">{problem_data.get('link', 'N/A')}</a></p>
                    </div>
                    
                    <div style="background: #e8f5e8; padding: 15px; border-left: 4px solid #4caf50; margin: 20px 0;">
                        <h3>✅ Solution (Copy & Paste Ready)</h3>
                        <pre style="background: #263238; color: #fff; padding: 15px; border-radius: 4px; overflow-x: auto;"><code>{solution_data.get('code', '# Solution code not available')}</code></pre>
                    </div>
                    
                    <div style="background: #fff3e0; padding: 15px; border-radius: 8px; margin: 20px 0;">
                        <h3>💡 Approach & Analysis</h3>
                        <p><strong>Approach:</strong> {solution_data.get('approach', 'Standard approach applied')}</p>
                        <p><strong>Complexity:</strong> {solution_data.get('complexity_analysis', 'Optimal time and space complexity')}</p>
                    </div>
                    
                    <div style="text-align: center; margin: 30px 0;">
                        <p>🤖 <strong>Auto-solved and committed to GitHub!</strong></p>
                        <p style="color: #666;">Check your repository for the complete solution with detailed explanation.</p>
                    </div>
                    
                    <hr style="margin: 30px 0; border: none; border-top: 1px solid #ddd;">
                    <p style="font-size: 12px; color: #888; text-align: center;">Generated by LeetCode Daily Automation • {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}</p>
                </body>
                </html>
                """
                
                # Plain text version for copy-paste
                text_body = f"""
🎯 LeetCode Daily: {problem_data.get('title', 'Problem Solved')}

📋 Problem Details:
Title: {problem_data.get('title', 'N/A')}
Difficulty: {problem_data.get('difficulty', 'N/A')}
Tags: {', '.join(problem_data.get('topic_tags', [])[:3])}
Link: {problem_data.get('link', 'N/A')}

✅ Solution (Copy & Paste):
{solution_data.get('code', '# Solution code not available')}

💡 Approach: {solution_data.get('approach', 'Standard approach applied')}
💡 Complexity: {solution_data.get('complexity_analysis', 'Optimal time and space complexity')}

🤖 Auto-solved and committed to GitHub!
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}
                """
            else:
                subject = "❌ LeetCode Daily Automation Failed"
                html_body = f"""
                <html>
                <body style="font-family: Arial, sans-serif; color: #333;">
                    <h2 style="color: #f44336;">❌ LeetCode Daily Automation Failed</h2>
                    <div style="background: #ffebee; padding: 15px; border-radius: 8px; border-left: 4px solid #f44336;">
                        <p><strong>Error:</strong> {error}</p>
                        <p><strong>Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}</p>
                    </div>
                    <p>Please check the GitHub Actions logs for more details.</p>
                </body>
                </html>
                """
                text_body = f"❌ LeetCode Daily Automation Failed\n\nError: {error}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}"
            
            # Send email via Mailgun
            mailgun_url = f"https://api.mailgun.net/v3/{self.mailgun_domain}/messages"
            
            response = requests.post(
                mailgun_url,
                auth=("api", self.mailgun_api_key),
                data={
                    "from": f"LeetCode Bot <noreply@{self.mailgun_domain}>",
                    "to": self.email_recipient,
                    "subject": subject,
                    "text": text_body,
                    "html": html_body
                },
                timeout=30
            )
            
            if response.status_code == 200:
                print(f"📧 Email notification sent successfully to {self.email_recipient}")
            else:
                print(f"⚠️  Email notification failed: {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"⚠️  Email notification error: {str(e)}")
            # Don't fail automation if notification fails

if __name__ == "__main__":
    automation = DailyLeetCodeAutomation()
    result = asyncio.run(automation.run_daily_automation())
    print(json.dumps(result, indent=2))
