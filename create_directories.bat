@echo off
mkdir data\raw data\processed data\external
mkdir notebooks src outputs\figures outputs\tables outputs\models docs reports
type nul > data\raw\.gitkeep
type nul > data\processed\.gitkeep
type nul > data\external\.gitkeep
type nul > outputs\figures\.gitkeep
type nul > outputs\tables\.gitkeep
type nul > outputs\models\.gitkeep
echo GitHub directory structure created.
