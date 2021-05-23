input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
})
//  Here is a comment I want to save.
basic.forever(function on_forever() {
    if (input.isGesture(Gesture.TiltLeft) && input.buttonIsPressed(Button.A)) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # # # # #
            # . . . #
            # . . . #
            `)
    } else {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
    
})
