def on_gesture_shake():
    basic.show_number(randint(1, 6))
    music.play(music.string_playable("C5 G F G E G F G ", 220),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("A F E F D F E F ", 220),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G E D E C E D E ", 220),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("F D C D C D F D ", 220),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
