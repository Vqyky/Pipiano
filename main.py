# IMPORTS
import mido
#
# from mido import Message
#
# msg = Message('note_on', note=60)
# print(msg)

# Open input and receive message
maininput = mido.open_input()
msg = maininput.receive()

print(msg)

