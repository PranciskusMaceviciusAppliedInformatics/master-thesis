import os

script_directory = os.path.dirname(os.path.realpath(__file__))
checkpoint_folder = os.path.join(script_directory, "baselines/encoder-decoder/checkpoints")

def find_max_checkpoint(checkpoint_dir):
    checkpoint_files = [f for f in os.listdir(checkpoint_dir) if f.startswith("checkpoint") and f.endswith(".pt") and f != "checkpoint_last.pt"]
    if not checkpoint_files:
        return None
    numbers = [int(name.split("checkpoint")[1].split(".")[0]) for name in checkpoint_files]
    return max(numbers)

for folder in os.listdir(checkpoint_folder):
    folder_path = os.path.join(checkpoint_folder, folder)
    print(f"Checking folder: {folder_path}")
    if os.path.isdir(folder_path):
        max_checkpoint = find_max_checkpoint(folder_path)
        print(f"Max checkpoint found: {max_checkpoint}")
        if max_checkpoint is not None:
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                if file.endswith(".pt"):
                    print(f"Found checkpoint file: {file}")
                    if file == f"checkpoint{max_checkpoint}.pt":
                        print(f"Skipping file: {file}")
                        continue
                    elif file == "checkpoint_last.pt":
                        print(f"Removing file: {file}")
                        os.remove(file_path)
                    elif file.startswith("checkpoint") and file.endswith(".pt"):
                        checkpoint_number = int(file.split("checkpoint")[1].split(".")[0])
                        if checkpoint_number < max_checkpoint:
                            print(f"Removing file: {file}")
                            os.remove(file_path)

