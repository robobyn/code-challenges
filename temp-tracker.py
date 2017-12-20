# add items in order to make sure max is always highest & min always lowest


class TempTracker(object):

    def __init__(self):
        """Method for instantiating TempTracker object."""

        self.temperatures = []

    def insert(self, temp):
        """Insert a new temperature into TempTracker object."""

        if not self.temperatures:

            self.temperatures.append(temp)
            return "Inserted {}".format(temp)

        for idx, current in enumerate(self.temperatures):

            if temp < self.temperatures[0]:
                self.temperatures.insert(0, temp)
                return "Inserted {} at index 0".format(temp)

            elif temp > self.temperatures[-1]:
                self.temperatures.append(temp)
                return "Inserted {} at index -1".format(temp)

            elif temp >= current and temp <= self.temperatures[idx + 1]:
                self.temperatures.insert(idx + 1, temp)
                return "Inserted {} at index {}".format(temp, idx + 1)

    def get_max(self):
        """Return highest value currently in TempTracker object."""

        return self.temperatures[-1] if self.temperatures else None

    def get_min(self):
        """Return lowest value currently in TempTracker object."""

        return self.temperatures[0] if self.temperatures else None

    def get_mean(self):
        """Return the mean of all values currently in TempTracker."""

        return (float(sum(self.temperatures)) / len(self.temperatures)) \
            if self.temperatures else None

    def get_mode(self):
        """Return the mode of all temps in TempTracker so far."""

        if not self.temperatures:
            return None

        temp_counts = {}

        for value in self.temperatures:

            if value not in temp_counts:
                temp_counts[value] = 1

            else:
                temp_counts[value] += 1

        most = max(temp_counts.values())

        for key in temp_counts:

            if temp_counts[key] == most:
                return key
