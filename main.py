# IMPORTS
import mido
import rtmidi
import time

# # from mido import Message
#
# msg = mido.Message('note_on', note=60)
# # print(msg)
#
# # Open input & output
# input = mido.open_input()
# output = mido.open_output()
#
# # Rtmidi
midiout = rtmidi.MidiOut()
# available_ports = midiout.get_ports()
#
# if available_ports:
#     midiout.open_port(0)
# else:
#     midiout.open_virtual_port("My virtual output")
#
with midiout.open_port(0):
    note_on = [0x90, 60, 112]  # channel 1, middle C, velocity 112
    note_off = [0x80, 60, 0]
    midiout.send_message(note_on)
    time.sleep(0.5)
    midiout.send_message(note_off)
    time.sleep(0.1)

del midiout
