#!/bin/bash

# Rover Pre Mission Checks
#1. Battery Failure Check

battery=$((RANDOM%101))
echo "Currently, the battery is: $battery%"

if [ $battery -lt 20 ]; then
    echo "Battery low! Return to base!"
    exit 1
fi #Bash using fi to end if block

#2. Checking Network connectivity by pinging Google.com

if ping -c 1 -q google.com > /dev/null 2>&1; then
    echo "Communication Established Successfully"
else
    echo "Communication failure!"
    exit 1;

fi

#3. Final Message to check if all operations are successful
echo "All systems operational!"