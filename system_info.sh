#!/bin/bash
# Assignment 1: Basic System Info

echo "==================================="
echo "       System Information"
echo "==================================="

# 1. Operating System name and kernel version
echo "OS & Kernel version : $(uname -a)"

# 2. Current logged-in user
echo "Current User        : $(whoami)"

# 3. Current working directory
echo "Working Directory   : $(pwd)"
