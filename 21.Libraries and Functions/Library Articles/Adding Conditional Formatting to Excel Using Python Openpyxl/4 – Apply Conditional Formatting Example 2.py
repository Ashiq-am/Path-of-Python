# ...

# Example 2: Apply a 2-color scale between 10 and 80
ws.conditional_formatting.add('A1:D4', ColorScaleRule(start_type='num', start_value=10, start_color='FFFFEDA0',
                                                      end_type='num', end_value=80, end_color='FF00BFFF'))
