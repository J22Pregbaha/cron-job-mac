# Running a cron job on Mac

> I recently learnt how to create a cron job on Mac. For those who don't know (like I didn't until just a while ago) a cron job is a scheduled job that runs as often as you want it to without the need for you to trigger it.

## How-to

In order to run this cron job on Mac or any Unix system, you can use crontab as follows:

```bash
crontab -e
```

```bash
39 18 * * * cd ~/path-to cron-job-mac && /usr/bin/php job.php >> ~/path-to cron-job-mac/cron-log.txt 2>&1
15 14 * * 1-5 cd ~/path-to cron-job-mac && /usr/bin/python test-python.py >> ~/path-to cron-job-mac/cron-log.txt 2>&1
```

You can get good tutorials on how the crontab works [here](https://betterprogramming.pub/https-medium-com-ratik96-scheduling-jobs-with-crontab-on-macos-add5a8b26c30) and [here](https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx/)
