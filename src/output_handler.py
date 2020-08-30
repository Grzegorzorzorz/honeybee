import time
import sys

def progress_bar(width, numerator, denominator):
    # Find how much each '#' represents on the progress bar.
    point_representation = denominator / width
    bar_current = int(numerator / point_representation)
    bar_total = int(denominator / point_representation) - bar_current
    rendered_bar = "["
    for x in range(0 , bar_current):
        rendered_bar = rendered_bar + "#"
    for x in range(0, bar_total):
        rendered_bar = rendered_bar + "-"
    rendered_bar = rendered_bar + "]"
    return rendered_bar

def full_bar(width, numerator, denominator, current_file):
    clear_lines(2)
    built_bar = progress_bar(width, numerator, denominator)
    percentage = round((numerator / denominator) * 100, 1)
    built_bar = built_bar + f" {percentage}% | {numerator}/{denominator}"
    built_bar = built_bar + f"\nCurrent file: '{current_file}'"
    return built_bar

def clear_lines(amount=1):
    up_character_code = '\x1b[1A'
    erase_character_code = '\x1b[2K'
    for x in range(0, amount):
        sys.stdout.write(up_character_code + erase_character_code)