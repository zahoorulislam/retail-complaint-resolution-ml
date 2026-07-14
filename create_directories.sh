#!/bin/bash
mkdir -p data/raw data/processed data/external
mkdir -p notebooks src outputs/figures outputs/tables outputs/models docs reports
touch data/raw/.gitkeep data/processed/.gitkeep data/external/.gitkeep
touch outputs/figures/.gitkeep outputs/tables/.gitkeep outputs/models/.gitkeep
echo "GitHub directory structure created."
