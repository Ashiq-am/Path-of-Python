# ...

# Example 1: Highlight cells greater than 40 in red
red_fill = PatternFill(start_color="FFEE1111",
                       end_color="FFEE1111", fill_type="solid")
ws.conditional_formatting.add('A1:D4', CellIsRule(
    operator='greaterThan', formula=['40'], stopIfTrue=True, fill=red_fill))
