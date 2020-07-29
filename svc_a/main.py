from src.app import app
from src.log_backup import backup_file_to_azure
from apscheduler.schedulers.background import BackgroundScheduler
import atexit


if __name__ == "__main__":
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(func=backup_file_to_azure, trigger="interval", seconds=6)
    sched.start()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: sched.shutdown())
    # Start the Flask app
    app.run(host="0.0.0.0")
