import json
import numpy as np
from scipy.stats import pearsonr, spearmanr, kendalltau

dataset_name = 'domain-specific'
embedding_method = "gte-base-finetuned"
# Paths to the JSON files
json_path_f1 = f'eval_results/{dataset_name}/e-gte-base/semantic_matching_perdoc.jsonl' # Model scores
json_path_scores = f'external_datasets/{dataset_name}/Book1-scores.json' # Human scores

# Read the JSON files
with open(json_path_f1, 'r', encoding='utf-8') as file:
    data_f1 = json.load(file)  # Load semantic_f1 data
semantic_f1_values = np.array(data_f1['semantic_matching']['semantic_f1'])

# Read the JSON file for scores and extract them
with open(json_path_scores, 'r', encoding='utf-8') as file:
    data_scores = json.load(file)
scores = np.array(data_scores)

# Verify the length of both arrays to be equal, or handle cases where they are not
if len(semantic_f1_values) != len(scores):
    raise ValueError("The length of the semantic_f1_values and scores arrays do not match.")

# Compute and print correlations
pearson_corr, _ = pearsonr(semantic_f1_values, scores)
spearman_corr, _ = spearmanr(semantic_f1_values, scores)
kendall_corr, _ = kendalltau(semantic_f1_values, scores)

print(f"Pearson correlation coefficient: {pearson_corr}")
print(f"Spearman's rank correlation coefficient: {spearman_corr}")
print(f"Kendall's tau correlation coefficient: {kendall_corr}")

try:
    # Attempt to read the existing data
    with open('correlations/correlations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    # If the file does not exist, start a new dictionary
    data = {}


if dataset_name not in data:
    data[dataset_name] = {}

if embedding_method not in data[dataset_name]:
    data[dataset_name][embedding_method] = {}

# Append the new results under the dataset name key
data[dataset_name][embedding_method]['pearson'] = pearson_corr
data[dataset_name][embedding_method]['spearman'] = spearman_corr
data[dataset_name][embedding_method]['kendall'] = kendall_corr

# Write the updated dictionary back to the JSON file
with open('correlations/correlations.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)