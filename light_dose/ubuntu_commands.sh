#!/bin/bash

#1)Create a new directory called rover_mission and navigate into it.
mkdir rover_mission
cd rover_mission

#2)Create three empty files named log1.txt, log2.txt, and log3.txt inside rover_mission.
touch log1.txt log2.txt log3.txt

#3)Rename log1.txt to mission_log.txt.
mv log1.txt mission_log.txt
#Testing Purposes
echo "System boot successful" >> mission_log.txt
echo "ERROR: sensor timeout" >> mission_log.txt
echo "Navigation online" >> mission_log.txt
echo "ERROR: GPS signal lost" >> mission_log.txt
touch testfile.log

#4)Find all files in the current directory that have a .log extension.
find . -name "*.log"

#5)Display the contents of mission_log.txt without opening it in an editor.
cat mission_log.txt

#6)Find and display all lines containing the word "ERROR" in mission_log.txt.
grep "ERROR" mission_log.txt
#grep -i "error" mission_log.txt for case insensitivity

#7)Count the number of lines in mission_log.txt.
wc -l mission_log.txt

#8)Show the system's current date and time.
date

#9)Display the CPU usage of your system in real time.
top -l 1 | grep "CPU usage" #Cmd for Mac
# top -bn 1 | grep "Cpu(s)" Cmd for Linux....Similar cmd but Slight Differences in wording

#10)Schedule a command to shut down the system in 10 minutes.
#sudo shutdown -h +10 Commented because Shutdown Cmd