folder = '..../C-NMC_Leukemia'
print(os.listdir(folder))
train = os.path.join(folder,'training_data')

fold_0 =os.path.join(train,os.listdir(train)[0])

all_img_path = os.path.join(fold_0, os.listdir(fold_0)[-1])
img_path = os.path.join(all_img_path,os.listdir(all_img_path)[0])
img_path


img = Image.open(img_path)
