import os
import shutil
import random


def split_dataset(dataset_path, train_ratio=0.7):
    images_path = os.path.join(dataset_path, "images")
    labels_path = os.path.join(dataset_path, "labels")
    train_images_path = os.path.join(images_path, "train")
    val_images_path = os.path.join(images_path, "val")
    train_labels_path = os.path.join(labels_path, "train")
    val_labels_path = os.path.join(labels_path, "val")

    os.makedirs(train_images_path, exist_ok=True)
    os.makedirs(val_images_path, exist_ok=True)
    os.makedirs(train_labels_path, exist_ok=True)
    os.makedirs(val_labels_path, exist_ok=True)

    image_files = [f for f in os.listdir(images_path) if f.endswith(".jpg")]

    random.shuffle(image_files)
    train_size = int(len(image_files) * train_ratio)
    train_files = image_files[:train_size]
    val_files = image_files[train_size:]

    for file in train_files:
        shutil.move(
            os.path.join(images_path, file), os.path.join(train_images_path, file)
        )
        label_file = file.replace(".jpg", ".txt")
        shutil.move(
            os.path.join(labels_path, label_file),
            os.path.join(train_labels_path, label_file),
        )

    for file in val_files:
        shutil.move(
            os.path.join(images_path, file), os.path.join(val_images_path, file)
        )
        label_file = file.replace(".jpg", ".txt")
        shutil.move(
            os.path.join(labels_path, label_file),
            os.path.join(val_labels_path, label_file),
        )

    print(
        f"Dataset split completed: {len(train_files)} train files, {len(val_files)} val files"
    )


dataset_path = "datasets/project-3-at-2025-01-16-07-57-578a93f1"
split_dataset(dataset_path)
