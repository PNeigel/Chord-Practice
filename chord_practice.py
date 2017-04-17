import graphics as g
import time as time
import numpy as np

rootdict = {0 : "A",
          1 : "B",
          2 : "C",
          3 : "D",
          4 : "E",
          5 : "F",
          6 : "G",
}

intonationdict = {0: "",
         1: "b",
         2: "#"
}

modedict = {0: "",
             1: "-"
}

class ChordPractice:
    def __init__(self):

        # Create Window
        self.win = g.GraphWin("Chord Practice", 500, 500)

        # Form to enter Beats per Minute
        self.form_bpm = g.Entry(g.Point(370, 50), 5)
        self.form_bpm.setText("12")  # Init as 12
        self.form_bpm.draw(self.win)
        self.bpm = 12

        # Label for bpm
        self.label_bpm = g.Text(g.Point(180, 50), "Beats per minute")
        self.label_bpm.draw(self.win)

        # Root Note Display
        self.root = g.Text(g.Point(240, 250), rootdict[0])
        self.root.draw(self.win)
        self.root.setSize(36)

        # Intonation Display
        self.intonation = g.Text(g.Point(270, 240), "b")
        self.intonation.setSize(30)
        self.intonation.draw(self.win)

        # Mode Display
        self.mode = g.Text(g.Point(270, 260), "-")
        self.mode.setSize(36)
        self.mode.draw(self.win)

        # Seven alterations
        self.seven = g.Text(g.Point(308, 233), "7")
        self.seven.setSize(18)

        # Alteration Symbols to draw
        self.maj = g.Polygon(g.Point(285, 240), g.Point(300, 240), g.Point(292.5, 225))
        self.diminished = g.Circle(g.Point(292.5, 232.5), 7)
        self.halfdim = g.Line(g.Point(285, 240), g.Point(301, 224))

        self.sevendrawn = False
        self.dimdrawn = False
        self.halfdimdrawn = False
        self.majdrawn = False

    def undrawSevens(self):
        if self.sevendrawn:
            self.seven.undraw()
            self.sevendrawn = False
        if self.dimdrawn:
            self.diminished.undraw()
            self.dimdrawn = False
        if self.halfdimdrawn:
            self.halfdim.undraw()
            self.halfdimdrawn = False
        if self.majdrawn:
            self.maj.undraw()
            self.majdrawn = False

    def programLoop(self):

        time1 = time.time()

        while self.win.isOpen():
            time2 = time.time()
            self.win.checkMouse()

            # Get new BPM, accept only numbers
            try:
                self.bpm = float(self.form_bpm.getText())
            except ValueError:
                self.form_bpm.setText(self.bpm)
            delay = 60.0/self.bpm

            if (time2 - time1 >= delay):

                self.undrawSevens()

                # Probabilities
                # 7 Chords: Major, Major Norm. 7, Major maj. 7, Minor, Minor 7, Diminished, Half Diminished

                p_minor = 2 / 7.0  # 2 Out of 7 Chords are minor
                p_minor_seven = 0.5  # If it's minor, with 50% it's minor seven
                p_maj_seven = 2 / 5.0  # If it's not minor, 2 out 5 5 chords have a seven
                p_maj_majseven = 0.5  # If it's a major chord with a seven, with 50% it's a maj. seven
                p_dim = 2 / 3.0  # If it's not a seven, with 2/3 it's either diminished or half diminished
                p_hdim = 0.5  # If it's diminished, it's either diminished or half diminished

                # Set root note, intonation and mode randomly from dictionaries
                self.root.setText(rootdict[np.random.randint(7)])
                self.intonation.setText(intonationdict[np.random.randint(3)])
                self.mode.setText(modedict[np.random.choice([0, 1], p=[1-p_minor, p_minor])])

                # Minor
                if (self.mode.getText() == "-"):
                    if np.random.rand() < p_minor_seven:
                        self.seven.draw(self.win)
                        self.sevendrawn = True
                else:
                    # Major
                    if (np.random.rand() < p_maj_seven):
                        self.seven.draw(self.win)
                        self.sevendrawn = True
                        if np.random.rand() < p_maj_majseven:
                            self.maj.draw(self.win)
                            self.majdrawn = True
                    elif (np.random.rand() < p_dim):
                        self.diminished.draw(self.win)
                        self.dimdrawn = True
                        if np.random.rand() < p_hdim:
                            self.halfdim.draw(self.win)
                            self.halfdimdrawn = True
                time1 = time2

if __name__ == "__main__":
    chordpractice = ChordPractice()
    chordpractice.programLoop()