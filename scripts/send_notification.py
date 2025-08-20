#!/usr/bin/env python3

import argparse
import json
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

def send_email_notification(status: str, problem_data: dict, solution_path: str):
    """Send email notification about solution status."""
    # Email configuration
    smtp_server = os.getenv('MAILGUN_SMTP_SERVER')
    smtp_port = int(os.getenv('MAILGUN_SMTP_PORT', '587'))
    smtp_username = os.getenv('MAILGUN_SMTP_USERNAME')
    smtp_password = os.getenv('MAILGUN_SMTP_PASSWORD')
    sender = f"LeetCode Bot <{smtp_username}>"
    recipient = os.getenv('EMAIL_RECIPIENT')

    if not all([smtp_server, smtp_port, smtp_username, smtp_password, recipient]):
        print("Missing email configuration")
        return

    # Create message
    msg = MIMEMultipart('alternative')
    
    if status == 'success':
        solution_file = None
        if problem_data:
            problem_id = problem_data.get('questionFrontendId', '')
            title = problem_data.get('title', '')
            if problem_id and title:
                filename = f"{problem_id}-{title.lower().replace(' ', '-')}.md"
                solution_file = Path(solution_path) / filename
        
        if solution_file and solution_file.exists():
            solution_content = solution_file.read_text()
            msg['Subject'] = f"✅ LeetCode Daily: {problem_data.get('title', 'Solution Ready')}"
            
            text_content = f"""
LeetCode Daily Solution Ready!

Problem: {problem_data.get('title')}
Difficulty: {problem_data.get('difficulty')}
Status: Solution Generated Successfully

Check the repository for the complete solution!
            """
            
            html_content = f"""
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">
    <h2 style="color: #2e7d32;">✅ LeetCode Daily Solution Ready!</h2>
    
    <div style="background: #f5f5f5; padding: 15px; border-radius: 8px;">
        <h3>📋 Problem Details</h3>
        <p><strong>Title:</strong> {problem_data.get('title')}</p>
        <p><strong>Difficulty:</strong> {problem_data.get('difficulty')}</p>
        <p><strong>Topics:</strong> {', '.join(problem_data.get('topicTags', []))}</p>
    </div>

    <div style="margin-top: 20px;">
        <p>The solution has been successfully generated and committed to the repository.</p>
        <p>Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
    </div>
</body>
</html>
            """
        else:
            msg['Subject'] = "✅ LeetCode Daily: Task Completed"
            text_content = "Daily LeetCode task completed successfully."
            html_content = "<h2>Daily LeetCode task completed successfully.</h2>"
    else:
        msg['Subject'] = "❌ LeetCode Daily: Task Failed"
        text_content = f"""
LeetCode Daily Task Failed

Status: {status}
Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}

Please check the GitHub Actions logs for more details.
        """
        html_content = f"""
<html>
<body style="font-family: Arial, sans-serif;">
    <h2 style="color: #f44336;">❌ LeetCode Daily Task Failed</h2>
    <div style="background: #ffebee; padding: 15px; border-radius: 8px;">
        <p><strong>Status:</strong> {status}</p>
        <p><strong>Time:</strong> {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
    </div>
    <p>Please check the GitHub Actions logs for more details.</p>
</body>
</html>
        """

    msg['From'] = sender
    msg['To'] = recipient

    msg.attach(MIMEText(text_content, 'plain'))
    msg.attach(MIMEText(html_content, 'html'))

    # Send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        print("Notification email sent successfully")
    except Exception as e:
        print(f"Failed to send notification email: {e}")

def main():
    parser = argparse.ArgumentParser(description='Send notification about LeetCode solution status')
    parser.add_argument('--status', required=True, help='Job status (success/failure)')
    parser.add_argument('--problem', type=str, help='JSON string containing problem data')
    parser.add_argument('--solution-path', default='solves', help='Path to solutions directory')
    args = parser.parse_args()

    problem_data = {}
    if args.problem:
        try:
            problem_data = json.loads(args.problem)
        except json.JSONDecodeError:
            print("Warning: Invalid problem data JSON")

    send_email_notification(args.status, problem_data, args.solution_path)

if __name__ == '__main__':
    main()
