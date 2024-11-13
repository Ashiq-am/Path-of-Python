# Applying Crop preprocess
X_train = df_train['image_paths'].apply(read_and_crop_image).values
X_val = df_val['image_paths'].apply(read_and_crop_image).values

y_train = df_train['image_labels'].values
y_val = df_val['image_labels'].values

X_train = np.stack(X_train, axis=0)
X_val = np.stack(X_val, axis=0)

# Expand dim to add channel info if image has 1 channel(Colorless)
if not KEEP_COLOR:
    X_train = np.expand_dims(X_train, axis=-1)
    X_val = np.expand_dims(X_val, axis=-1)

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.1, random_state=MAIN_SEED)

print("X_train ->", X_train.shape,
      "\ny_train ->", y_train.shape,
      "\n\nX_test ->", X_test.shape,
      "\ny_test ->", y_test.shape,
      "\n\nX_val ->", X_val.shape,
      "\ny_val ->", y_val.shape
      )
