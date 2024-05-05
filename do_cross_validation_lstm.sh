#!/bin/bash

launch_script() {
    script_path="$1"
    script_name="$2"
    log_file="$script_path/error_log.txt"

    echo "Launching script: $script_name"
    (cd "$script_path" && ./"$script_name") 2>&1 | tee -a "$log_file"

    if [ $? -eq 0 ]; then
        echo "Script completed successfully."
    else
        echo "Script encountered an error. Check $log_file for details."
    fi
}

for i in {1..10}; do
    script_path="$i/baselines/encoder-decoder"
    script_name="preprocess"
    launch_script "$script_path" "$script_name"
done

for i in {1..10}; do
    script_path="$i/baselines/encoder-decoder"
    script_name="sweep"
    launch_script "$script_path" "$script_name"
done
