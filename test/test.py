# Sample Usage
import shutil, time
from ProgressLite import ProgressLite

# A List of Items
items = list(range(0, 100))
l = len(items)

# Initial call to print 0% progress
tracker = ProgressLite()
tracker.printProgress(0, l, prefix = 'Progress:', suffix = 'Complete')
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.1)
    # Update Progress Bar
    tracker.printProgress(i + 1, l, prefix = 'Progress:', suffix = 'Complete')