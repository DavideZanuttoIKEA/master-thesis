# Keyphrase Generation and Topic Identification Project

## Project Description

This project is composed of two parts. 

The keyphrase generation part utilizes different Large Language Models (Llama3-8B, Gemma-7B, and Mistral-7B) with few-shot learning and fine-tuning to generate keyphrases from a set of reviews. With each keyphrase, its related sentiment will be also generated. Sentiments will be a single word between Positive, Negative and Neutral. An evaluation method called KPEval will be used to evaluate those keyphrases against a manually annotated ground truth. For sentiment evaluation, a classic exact-matching technique has been used (comparing with ground truth).

The topic identification part explores the usage of Llama3-8B to identify the most discussed topics in a group of reviews. The experiments were done using different inputs to the LLM (only the reviews, only the keyphrases obtained by clustering and a combination of them). The clustering methods used to obtained keyphrases are K-means and Hierarchical clustering. Evaluation of topics is done on correctness and diversity. Specific embedding-based metrics have been designed to compute both of them.


## Usage

The execution of these scripts may require csv files or other data stored in my bucket `zanuttod-bucket` on Google Cloud Storage.

### Keyphrase Prediction (Task 1)

#### Generation
- Navigate to `Keyphrase Prediction - Task 1/Keyphrase-generation/`
- Here are available different models with different learning approaches to generate the keyphrases


#### Evaluation
- Navigate to `Keyphrase Prediction - Task 1/Keyphrase-evaluation/`
- Navigate to `run_evaluation.ipynb` and change the `file` variable with the prediction file name
- Execute `run_evaluation.ipynb` to evaluate the generated keyphrases.
- The sentiment score will be showed in the console logs, while the similarity score is saved in `keyphrase-evaluation/eval_results/sample/{model_name}`.


#### Fine-tuning
- Navigate to `Keyphrase Prediction - Task 1/keyphrase-generation-finetuning/`
- Use the notebooks to fine-tune different models (Llama3, Gemma, Mistral) for keyphrase generation


### Topic Identification (Task 2)

#### Clustering
- The `Keyphrase-clustering/` subfolder contains various notebooks for keyphrase clustering and evaluation
- Run `embedKeyphrases.ipynb` to prepare the embeddings of the keyphrases
- Navigate to `hierarchical/` or `k-means/` based on which clustering method you want to use
- Run the files inside the folder following the order, the output will be a csv file with the "core" (clustered) keyphrases


#### Generation
- Navigate to `Topic Identification - Task 2/Topic-generation/`
- Choose between `Llama3_EvaluationTopics-Keyphrases`,  `Llama3_EvaluationTopics-Reviews` and `Llama3_EvaluationTopics-Complete` to generate topics with Llama3, these files include different inputs to the LLM
- (For Demo) Run `HighlightingTopics.ipynb` to generate a csv file with the maximum 4 reviews per article that talk about a specific topic, and the part the mention the topic highlighted


#### Evaluation
- Navigate to `Topic Identification - Task 2/Topic-evaluation/`
- `GroundTruthCreation.ipynb` generates a first draft of ground truth data which has been then manually annotated
- Run `Evaluation.ipynb` for complete evaluation of a file, results are saved in `evaluation_results.json` where topic correctness (exact-matching and embedding based) and topic diversity are listed


### Demo
- Navigate to `project-demo/`
- Run `ReviewsKeyphrasesDemo.py` for a localhost demo of keyphrase prediction
- Run `TopicsDemo.py` for a localhost demo of topic identification
- This require csv files stored in my bucket `zanuttod-bucket` in the folder `project-demo`  

## Author

Davide Zanutto -<br>Data Science & AI Master thesis student at Eindhoven University of Technology and Politecnico di Milano