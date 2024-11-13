fig.for_each_trace(lambda trace: trace.update(name=trace.name.replace("Sales_A", "Product A Sales").replace("Sales_B", "Product B Sales")))
