class Workouts():
    def __init__(self, max):
        self._max = max

    def _get_percentages(self):
        percentages = {}

        i = .65
        while i < 1:
            value = round(i * self._max, 2)
            key = int(i*100)
            percentages[key] = value
            i = i + .05

        d = .40
        while d < .70:
            value = round(d * self._max, 2)
            key = int(d*100)
            percentages[key] = value
            d = d + .10

        return percentages
    
    
    def fivethreeone_program(self):
        percentages = self._get_percentages()
        
        for key, val in percentages.items():
            percentages[key] = val * .9

        workout = {
            "Week 1": [
                [percentages[65], 5],
                [percentages[75], 5],
                [percentages[85], 5]
            ],
            "Week 2": [
                [percentages[70], 3],
                [percentages[80], 3],
                [percentages[90], 3]
            ],
            "Week 3": [
                [percentages[75], 5],
                [percentages[85], 3],
                [percentages[95], 1]
            ],
            "Week 4": [
                [percentages[40], 5],
                [percentages[50], 5],
                [percentages[60], 5]
            ]
        }

        return workout