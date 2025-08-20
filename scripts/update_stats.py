#!/usr/bin/env python3

import json
from pathlib import Path
from typing import Dict, List

def extract_difficulty(content: str) -> str:
    """Extract difficulty from solution file content."""
    for line in content.split('\n'):
        if line.startswith('## Difficulty:'):
            return line.split(':')[1].strip()
    return 'Unknown'

def generate_stats() -> Dict[str, int]:
    """Generate statistics from solution files."""
    stats = {
        'total': 0,
        'easy': 0,
        'medium': 0,
        'hard': 0
    }

    solves_dir = Path('solves')
    if not solves_dir.exists():
        return stats

    for solution_file in solves_dir.glob('*.md'):
        try:
            content = solution_file.read_text()
            difficulty = extract_difficulty(content).lower()
            
            stats['total'] += 1
            if difficulty in stats:
                stats[difficulty] += 1

        except Exception as e:
            print(f"Error processing {solution_file}: {e}")

    return stats

def main():
    try:
        # Generate stats
        stats = generate_stats()
        
        # Save to stats.json
        with open('stats.json', 'w') as f:
            json.dump(stats, f, indent=2)
            
        print(f"Updated stats: {json.dumps(stats, indent=2)}")
        
    except Exception as e:
        print(f"Error updating stats: {e}")
        exit(1)

if __name__ == '__main__':
    main()
