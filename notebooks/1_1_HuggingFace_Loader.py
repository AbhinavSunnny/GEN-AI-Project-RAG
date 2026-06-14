from datasets import load_dataset

# Function to load Hugging Face dataset
def load_huggingface_data():
    
    dataset = load_dataset(
        "abisee/cnn_dailymail",
        "3.0.0",
        split="train[:100]"
    )
    
    return dataset


# Load dataset
hf_dataset = load_huggingface_data()

# Display first row
print(hf_dataset[0])