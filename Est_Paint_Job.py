###########################################################################
# Module: Est_Paint_Job.py
# Exercise: Ch5_Exercise_8
# Purpose: Paint Job Estimater
# Author: Lisa Nydick
# Last Update: 10/09/2018
###########################################################################

LABOR_COST_PER_HOUR = 35
WALL_SPACE_METRIC = 112
LABOR_PER_GALLON = 8
LABOR_RATE = 35

wall_space = 0
wall_space_coverage = 0
labor_hours_required = 0
paint_cost = 0
sq_ft_wall_space = 0
total_cost = 0
gallons_paint = 0

def main():
    wall_space_coverage, paint_cost = get_input()
    paint_gallons_needed, total_paint_cost, total_labor_hours_needed, total_labor_cost = compute_cost(wall_space_coverage, paint_cost)
    display_info(wall_space_coverage, paint_cost, paint_gallons_needed, total_paint_cost, total_labor_hours_needed, total_labor_cost)

main()

def get_input():
    wall_space = int(input('Enter wall space to be covered (in sq feet)'))
    paint_cost = int(input('Enter paint cost per gallon'))
    return wall_space, paint_cost

def compute_cost(wall, paint):
    paint_cost = PAINT_METRIC
    labor_cost = LABOR_METRIC
    wall_space = WALL_SPACE_METRIC

    wall_space_coverage = wall
    paint_cost = paint

    total_paint_gallons_needed = wall_space_coverage / WALL_SPACE_METRIC
    total_paint_cost = total_paint_gallons_needed * paint_cost
    total_labor_hours_needed = wall_space_coverage / WALL_SPACE_METRIC
    total_labor_cost = total_labor_hours_needed * LABOR_METRIC
    return paint_gallons_needed, total_paint_cost, total_labor_hours_needed, total_labor_cost

def display_info(wall_space_coverage, paint_cost, paint_gallons_needed, total_paint_cost, total_labor_hours_needed, total_labor_cost):
    print('Number of gallons required =', paint_gallons_needed)

