import time, random
import picoexplorer as explorer

width = explorer.get_width()
height = explorer.get_height()

display_buffer = bytearray(width * height * 2)
explorer.init(display_buffer)

explorer.set_audio_pin(0) # buzzer alarm for dangerous air quality