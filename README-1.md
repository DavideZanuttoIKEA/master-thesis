# Thesis Project Readme

## Project Overview

The thesis project comprises two main tasks: Keyphrase Generation and Topic Identification. 
Keyphrase generation takes as input a list of reviews and generate keyphrases and sentiments for each of them choosing a model between Llama3, Mistral and Gemma.
Topic identification uses an LLM (Llama3) to generate a list of topics for each article. The input to the LLM can be: reviews, keyphrases obtained by clustering, a combination of reviews and keyphrases. A post-processing step is then applied to merge the results from previous experiments.

All these experiments have been run on Vertex AI with a GPU available, running these experiments with cpu will highly increase the computation time.
---

## How to reproduce

1. Build the Docker image: 
`docker build -t sample-thesis-project .`

2. Run the container: 
`docker run -p 8888:8888 sample-thesis-project`

3. Look for the Jupyter Notebook URL in the console output. It will look something like this: 
http://127.0.0.1:8888/?token='some_token'

4. Open the URL in a browser, here you can run the notebook files

The order to run the notebooks are specified here below for both tasks.

## Keyphrase Generation

### Steps to Generate Keyphrases

1. **Choose a Notebook Based on LLM:**
   - You can generate keyphrases by running one of the three notebooks provided. Select the notebook corresponding to the chosen Language Model (LLM):
     - `gemma-5shot.ipynb`
     - `Llama3-8b-5shot.ipynb`
     - `mistral_5shot.ipynb`

2. **Run the Selected Notebook:**
   - Execute the chosen notebook to generate keyphrases. The results will be saved as CSV files in the `results` subfolder.

### Evaluation Process

1. **Navigate to KPEval:**
   - Go to the `KPEval` directory.

2. **Modify the file name**
   - Navigate to `run_evaluation.ipynb` and change the `file` variable with one between: `gemma-5shot`, `Llama3-8b-5shot`, `mistral_5shot`.

3. **Run run_evaluation.ipynb:**
   - Execute `run_evaluation.ipynb` to evaluate the generated keyphrases.

4. **See the results**
   - The sentiment score will be showed in the console logs, while the similarity score are saved in `keyphrase-generation/KPEval/eval_results/sample/{model_name}`.


---

## Topic Identification

### Steps to Generate Topics

1. **Choose a Notebook:**
   - You can generate topics by running one of the three `TopicIdentification` notebooks. Each notebook uses different inputs:
     - `TopicIdentification-Complete.ipynb`
     - `TopicIdentification-Keyphrases.ipynb`
     - `TopicIdentification-Reviews.ipynb`

2. **Run the Selected Notebook:**
   - Execute the chosen notebook to generate topics.

3. **Postprocessing:**
   - Apply postprocessing by running `postProcessing.ipynb`.

### Evaluation Process

1. **Go to Evaluation.ipynb:**
   - Go to the `Evaluation.ipynb` file in the `topic-identification` folder.

2. **Change the filename**
   - Change the filename in row 10 with one of the csv name in the `results` folder.

3. **Run Evaluation.ipynb:**
   - Execute `evaluation.ipynb` to evaluate the generated topics.

---

## Directory Structure

The project directory structure is as follows:

SAMPLE-THESIS-PROJECT/
├── .conda/
├── keyphrase-generation/
│ ├── KPEval/
│ │ ├── configs/
│ │ ├── embedding/
│ │ ├── eval_results/
│ │ ├── keyphrase-generation/
│ │ ├── metrics/
│ │ ├── model_outputs/
│ │ ├── .gitignore
│ │ ├── 5shot_llama3.csv
│ │ ├── createJson.ipynb
│ │ ├── KeyphrasesGroundTruth.csv
│ │ ├── run_evaluation.ipynb
│ │ ├── run_evaluation.py
│ │ ├── run_evaluation.sh
│ ├── results/
│ ├── gemma-5shot.ipynb
│ ├── Llama3-8b-5shot.ipynb
│ ├── mistral_5shot.ipynb
├── topic-identification/
│ ├── results/
│ ├── 3Shot_Examples.csv
│ ├── 3Shot_Reviews.csv
│ ├── core_keyphrases_hierarchical.csv
│ ├── core_keyphrases_kmeans.csv
│ ├── evaluation_results.json
│ ├── Evaluation.ipynb
│ ├── postProcessing.ipynb
│ ├── TopicGroundTruth.csv
│ ├── TopicIdentification-Complete.ipynb
│ ├── TopicIdentification-Keyphrases.ipynb
│ ├── TopicIdentification-Reviews.ipynb
├── Dockerfile
├── environment.yml
├── requirements.txt
├── Sample-dataset.csv