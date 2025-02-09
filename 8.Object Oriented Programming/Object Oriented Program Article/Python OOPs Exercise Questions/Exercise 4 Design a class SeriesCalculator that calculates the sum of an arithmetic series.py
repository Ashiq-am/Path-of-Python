class SeriesCalculator:
    def calculate_sum(self, n, a=1, d=2):
        # Sum of the first n terms of an arithmetic series
        return n * (2 * a + (n - 1) * d) // 2

# Test the calculator
sc = SeriesCalculator()
print("Sum of series:", sc.calculate_sum(5))
