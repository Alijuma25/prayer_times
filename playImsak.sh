#!/usr/bin/env bash

# Define the script directory
root_dir=`dirname $0`

# Run before hooks
for hook in $root_dir/before-hooks.d/*; do
    echo "Running before hook: $hook"
    $hook
done

# Play Imsak audio
python3 /usr/local/bin/castImsak.py

# Run after hooks
for hook in $root_dir/after-hooks.d/*; do
    echo "Running after hook: $hook"
    $hook
done
