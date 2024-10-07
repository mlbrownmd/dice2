input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
    music.play(music.stringPlayable("C5 G F G E G F G ", 220), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("A F E F D F E F ", 220), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("G E D E C E D E ", 220), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("F D C D C D E C ", 220), music.PlaybackMode.UntilDone)
})
