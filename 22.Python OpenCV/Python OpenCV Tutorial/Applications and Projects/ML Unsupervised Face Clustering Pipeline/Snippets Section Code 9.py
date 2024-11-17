# Inherit class tqdm for visualization of progress
class TqdmUpdate(tqdm):

    # This function will be passed as progress
    # callback function. Setting the predefined
    # variables for auto-updates in visualization
    def update(self, done, total_size=None):
        if total_size is not None:
            self.total = total_size

        self.n = done
        super().refresh()
