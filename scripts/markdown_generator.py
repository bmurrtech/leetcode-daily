from datetime import datetime
from typing import Dict, Any

class MarkdownGenerator:
    @staticmethod
    def generate_solution_file(problem_data: Dict[str, Any], solution_data: Dict[str, Any]) -> str:
        """Generate markdown content matching the existing repo format"""
        
        optimization_notes = ""
        if solution_data.get('optimization_notes'):
            optimization_notes = f"\n\n**Optimization Notes:**\n" + "\n".join(
                f"- {note}" for note in solution_data['optimization_notes']
            )
        
        markdown_content = f"""## {problem_data['question_id']}. {problem_data['title']}
[{problem_data['question_id']} LeetCode Link]({problem_data['link']})

{solution_data.get('explanation', 'Optimal solution approach selected based on problem constraints.')}

{solution_data.get('approach', '')}

Key considerations:
{solution_data.get('complexity_analysis', 'This solution provides an optimal approach with careful consideration of time and space complexity.')}

### Python
Here is the Python code implementing the solution:

```python
{solution_data.get('code', '# Solution code will be generated')}
```

#### Understanding the Code
{solution_data.get('detailed_explanation', solution_data.get('explanation', 'This solution implements the optimal approach to solve the problem efficiently.'))}
{optimization_notes}

> **Tags:** {', '.join(problem_data['topic_tags'])}  
> **Difficulty:** {problem_data['difficulty']}  
> **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}  
> **Solved by:** [opticodegen toolkit](https://github.com/yourusername/opticodegen)

"""
        return markdown_content
    
    @staticmethod
    def update_readme(solutions_list: list) -> str:
        """Generate/update README.md with problem index"""
        
        # Group by difficulty
        easy = [s for s in solutions_list if s['difficulty'] == 'Easy']
        medium = [s for s in solutions_list if s['difficulty'] == 'Medium'] 
        hard = [s for s in solutions_list if s['difficulty'] == 'Hard']
        
        readme_content = f"""# LeetCode Solutions

![LeetCode Badges](https://leetcode-badge-showcase.vercel.app/api?username=bmurrtech&animated=true)

![Python](https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automation-2088ff?style=for-the-badge&logo=github-actions&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-Daily_Solver-ffa116?style=for-the-badge&logo=leetcode&logoColor=white)
![Automated](https://img.shields.io/badge/Automated-✅-success?style=for-the-badge)

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=bmurrtech&show_icons=true&theme=default&hide_border=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=bmurrtech&layout=compact&theme=default&hide_border=true)

Automated daily LeetCode problem solving using [opticodegen toolkit](https://github.com/yourusername/opticodegen).

## Statistics
- **Total Problems Solved:** {len(solutions_list)}
- **Easy:** {len(easy)} | **Medium:** {len(medium)} | **Hard:** {len(hard)}
- **Current Streak:** {len(solutions_list)} days
- **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

## Solutions by Difficulty

### Easy ({len(easy)})
{chr(10).join(f"- [{s['question_id']}. {s['title']}](./solutions/{s['filename']})" for s in easy)}

### Medium ({len(medium)})
{chr(10).join(f"- [{s['question_id']}. {s['title']}](./solutions/{s['filename']})" for s in medium)}

### Hard ({len(hard)})
{chr(10).join(f"- [{s['question_id']}. {s['title']}](./solutions/{s['filename']})" for s in hard)}

## About

This repository is automatically maintained using:
- **Problem Fetching:** LeetCode GraphQL API
- **Solution Generation:** Custom opticodegen toolkit deployed on Railway
- **Automation:** GitHub Actions with daily scheduling
- **Notifications:** Self-hosted ntfy service

Each solution includes:
- ✅ Optimized Python code
- 📝 Detailed explanation and approach
- 🔍 Complexity analysis
- 🏷️ Topic tags and difficulty rating

---
*Automation powered by [opticodegen](https://github.com/yourusername/opticodegen)*
"""
        return readme_content
