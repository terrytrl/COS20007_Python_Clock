import Counter
from Counter import Counter


class Clock(object):
    
    _counterHours = Counter("Hours")
    _counterMins = Counter("Mins")
    _counterSeconds = Counter("Seconds")

    def __init__(self):
        self

    def CountMe():

        _counterSeconds.Increment

        if(_counterSeconds.count == 60):
            _counterMins.Increment
            _counterSeconds.Reset
        if(_counterMins.count == 60):
            _counterHours.Increment
            _counterMins.Reset
        if(_counterHours.count == 24) & (_counterMins.count == 60) & (_counterSeconds.count == 60):
            _counterHours.Reset
            _counterMins.Reset

    def PrintClock():
        print(_counterSeconds.value)
    
        
