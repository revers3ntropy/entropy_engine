import time
import pygame as py

run_fps = 60

clock = py.time.Clock()

current_fps = 0

tick = 0


def update_fps(start_time):
    global current_fps
    current_fps = round(1.0 / (time.time() - start_time))


def clock_tick():
    clock.tick(run_fps)
