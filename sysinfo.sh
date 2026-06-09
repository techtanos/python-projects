#!/bin/bash

echo "===== SYSTEM INFO ====="
echo "User: $(whoami)"
echo "Date: $(date)"
echo "Disk space: $(df -h / | tail -1 |awk '{print $4}') free"
echo "IP Address: $(hostname -I)"
echo "========================"

