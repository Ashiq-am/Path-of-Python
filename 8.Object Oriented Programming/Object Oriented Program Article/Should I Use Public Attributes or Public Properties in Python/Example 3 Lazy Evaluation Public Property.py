class Data:
    def __init__(self, data):
        self._data = data
        self._processed_data = None

    @property
    def processed_data(self):
        if self._processed_data is None:
            self._processed_data = self._process_data()
        return self._processed_data

    def _process_data(self):
        # Simulate a heavy processing task
        return [x * 2 for x in self._data]


data = Data([1, 2, 3])
print(data.processed_data)  # Output: [2, 4, 6]
