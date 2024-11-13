# Example 3: Formula-based conditional formatting (highlight even numbers in blue)
blue_fill = PatternFill(start_color="FF0000FF",
                        end_color="FF0000FF", fill_type="solid")
ws.conditional_formatting.add('A1:D4', FormulaRule(
    formula=['MOD(A1,2)=0'], fill=blue_fill))
