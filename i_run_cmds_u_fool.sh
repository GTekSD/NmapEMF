#!/bin/bash

# Read input list of commands from file
while IFS= read -r command; do
    # Execute command and wait for it to finish
    $command &
    command_pid=$!
    wait $command_pid
done < "$1"
