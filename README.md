# Description
`busywork` is simple automation program that pumps up GitHub contribution stats<br>
by creating pointless edits to itself. It also emulates the feeling of agile, I guess. <br>

If<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a) git is installed, &<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) a cron job or task is scheduled on the user's computer, it'll:<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;run once a day (or less/more) & add a comment at the end of the program file,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;commit & push itself to the GitHub repository,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;revert itself back to its original state (i.e. remove the comment), &<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;commit & push itself again.<br>

A program for slackers who don't want their activities quantified or measured with<br> 
total accuracy.
<br><br>
# Program Instructions
1. Download/clone the repo
2. Create a `secrets.txt` file in the same folder/dir. as the program
3. Write the filepath in the textfile to the `busywork.py` program (e.g. C:\Users\XYZ\busywork\busywork.py)
4. Save the text file
5. Init/set up git/GitHub for your local copy of this repo, same as any other repo you'd want to publish on GitHub
6. Set up a cron job/task scheduler to run the .py file once a day (or less/more depending on how you feel)
7. The very image of success: generating activity everyday to no real end.
<br><br>
# Instructions for Automatically Running the Program:
## Mac/Linux
1. Open the Terminal application.
2. Use the crontab command to edit the cron table:
```sh
crontab -e
```
3. In the text editor that opens, add a new line to specify the schedule and the command you want to run. For example, to run a script every day at 9 AM, you can add:
```sh
0 9 * * * /path/to/your/script.sh
```
4. Replace /path/to/your/script.sh with the actual path to your script.
5. Save the file and exit the text editor.
6. The scheduled task will now run automatically according to the specified schedule.
<br><br>
## Windows
1. Open the Task Scheduler. You can do this by pressing the Windows key, searching for "Task Scheduler," and selecting the appropriate result.
2. In the Task Scheduler window, click on "Create Basic Task" or "Create Task" from the sidebar, depending on your Windows version.
3. Follow the on-screen instructions to set the name, description, and schedule for the task. You can specify the frequency, start time, and other options according to your requirements.
4.  In the "Actions" tab, click "New" to add a new action.
5.  Browse and select the script or program you want to run automatically.
6.  Configure any additional settings as needed and click "OK."
7.  Review the summary and click "Finish" to create the scheduled task.
8.  The task will now run automatically based on the specified schedule.
<br><br>
# Troubleshooting git/GitHub
* If GitHub's GCM(GitHub Credential Manager) keeps showing up & requires manual intervention, try entering 
```
git remote set-url origin https://<your username>@github.com/<your username>/<repo name>
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in the terminal (e.g. Git Bash)

* If you're having trouble using CLI for git/GitHub, I recommend the [GitHub desktop client](https://desktop.github.com/); it's much more intuitive (alhough you give up some control using a GUI).
