def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# Here is a comment I want to save.

def on_forever():
    if input.is_gesture(Gesture.TILT_LEFT) and input.button_is_pressed(Button.A):
        basic.show_leds("""
            # # # # #
            # . . . #
            # # # # #
            # . . . #
            # . . . #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
basic.forever(on_forever)
