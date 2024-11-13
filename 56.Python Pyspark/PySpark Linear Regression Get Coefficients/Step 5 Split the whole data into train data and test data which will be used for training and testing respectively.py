final_data = output.select("features",'Yearly Amount Spent')
train_data,test_data = final_data.randomSplit([0.7,0.3])
