# Scratch Files and Logs

## Wednesday, April 11, 2018 9:17 AM

> goals

* track amount of time elapsed between presses of the `ENTER` key, with each key press starting a new "lap" on the timer

* print the lap number, total time and lap time

> code actions

* find the current time by calling `time.time()` and store as a time stamp at program start, and start of each lap

* keep a lap counter and increase every time user hits `ENTER`
* calculate the elapsed time by subtracting time stamps

* handle `KeyboardInterrupt` exception so user can press `CTRL-C` to quit

## Wednesday, April 11, 2018 9:29 AM

> similar programs

advantage of your own programs doing this is that they're free and bloat free

* create simple timesheet app that records when you type a person's name and uses the current time to clock them in or out

* add a feature to your program to show the elapsed time since a process started...  i.e. like a download using `requests`

* periodically check how long a program has been running and offer user a chance to cancel tasks that are taking too long...

