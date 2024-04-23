# schedule_trending_posts.py
import os
import sys
import schedule
import time

# Add your Django project path to sys.path
# sys.path.append('/path/to/your/django/project')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsblog.settings')
import django
django.setup()

# Import your management command
from django.core.management import call_command

def update_trending_posts():
    call_command('update_trending_posts')

# Schedule the management command to run every 2 hours
schedule.every(2).minutes.do(update_trending_posts)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 60 seconds before checking again
