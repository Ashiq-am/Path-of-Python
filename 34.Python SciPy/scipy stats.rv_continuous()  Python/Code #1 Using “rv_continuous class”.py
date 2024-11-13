def sample(self, size=1, random_state=None):
    """
    Return a sample from PDF - Probability Distribution Function.
    calling - rv_continuous class.

    """

    return self._rv.rvs(size=size, random_state=random_state)
