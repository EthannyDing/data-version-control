from pathlib import Path
import os
import pandas as pd

FOLDERS_TO_LABELS = {"n01440764": "golf ball", "n02102040": "parachute"}


def get_files_and_labels(source_path):
    images = []
    labels = []
    for image_path in source_path.rglob("*/*.JPEG"):
        filename = image_path.absolute()
        folder = image_path.parent.name
        if folder in FOLDERS_TO_LABELS:
            images.append(filename)
            label = FOLDERS_TO_LABELS[folder]
            labels.append(label)
    return images, labels


def save_as_csv(filenames, labels, destination):
    data_dictionary = {"filename": filenames, "label": labels}
    data_frame = pd.DataFrame(data_dictionary)
    data_frame.to_csv(destination)


def main(repo_path):
    data_path = repo_path / "data"
    train_path = data_path / "raw/train"
    test_path = data_path / "raw/val"

    img_path = next(train_path.rglob("*/*.JPEG"))
    print(os.getcwd())  # /Users/ethanding/dvc_tutorial/data-version-control
    print(img_path)  # data/raw/train/n02102040/n02102040_4076.JPEG
    print(img_path.parent)  # data/raw/train/n02102040
    print(img_path.absolute())  # # /Users/ethanding/dvc_tutorial/data-version-control/data/raw/train/n02102040/n02102040_4076.JPEG
    print(img_path.name)  # n02102040_4076.JPEG

    train_files, train_labels = get_files_and_labels(train_path)
    test_files, test_labels = get_files_and_labels(test_path)
    prepared = data_path / "prepared"
    save_as_csv(train_files, train_labels, prepared / "train.csv")
    save_as_csv(test_files, test_labels, prepared / "test.csv")


if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    print(repo_path)
    main(repo_path)
