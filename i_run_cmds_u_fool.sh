#!/bin/bash

# Read input list of commands from file
while read command; do
    # Execute command and wait for it to finish
    $command &
    wait $!
done < "$1"
