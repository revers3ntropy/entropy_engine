import time
import renderer

target_fps = renderer.run_FPS

clock = renderer.clock

current_fps = 0

tick = 0


def update_fps(start_time):
    global current_fps
    current_fps = round(1.0 / (time.time() - start_time))
