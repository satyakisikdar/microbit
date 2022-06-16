import microbit
import radio
import random
import audio 

# Turn on the radio
radio.on()

group = 0
radio.config(group=group)
num_groups = 4 
group_sounds = [microbit.Sound.HAPPY, microbit.Sound.SAD, microbit.Sound.HELLO, microbit.Sound.MYSTERIOUS]

while True:
    if microbit.button_b.is_pressed():
        group = (group + 1) % num_groups
        # audio.play(group_sounds[group])
        microbit.display.scroll('G:' + str(group))
        radio.config(group=group)

    # check for incoming messages 
    inc_msg = radio.receive()

    if inc_msg is not None:
        # display the message
        microbit.sleep(100 + random.randint(100, 500))
        text = 'R:' + str(inc_msg)
        microbit.display.scroll(text, delay=100)
        audio.play(group_sounds[group])
    
    if microbit.button_a.is_pressed():
        # send message
        out_msg = str(group)
        microbit.display.scroll('S:' + out_msg)
        audio.play((group_sounds[group]))
        microbit.sleep(1_000)
        radio.send(out_msg)

    if microbit.pin_logo.is_touched():
        microbit.display.scroll('G:' + str(group))
