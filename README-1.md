# Keyphrase and Topic Identification Project

## Project Description

This project focuses on advanced natural language processing tasks, specifically keyphrase prediction and topic identification. It leverages state-of-the-art language models and machine learning techniques to extract meaningful information from text data.

### Key Features:
1. **Keyphrase Prediction (Task 1)**: 
   - Utilizes fine-tuned versions of cutting-edge language models like Llama3, LoRA, and Mistral.
   - Implements both few-shot learning and full fine-tuning approaches.
   - Includes comprehensive evaluation metrics and tools for assessing keyphrase quality.

2. **Topic Identification (Task 2)**:
   - Employs clustering and classification techniques to identify main topics in text corpora.
   - Features tools for visualizing topic distributions and highlighting key themes.

3. **Evaluation and Benchmarking**:
   - Robust evaluation frameworks for both keyphrase prediction and topic identification tasks.
   - Includes scripts for creating ground truth datasets and conducting meta-evaluations.

4. **Demonstration Tools**:
   - User-friendly demo applications to showcase the capabilities of both keyphrase extraction and topic identification on real-world text data.

This project aims to provide researchers and practitioners with powerful tools for extracting structured information from unstructured text, facilitating applications in areas such as content analysis, information retrieval, and document summarization.

## Overview

This project focuses on two main tasks:
1. Keyphrase Prediction (Task 1)
2. Topic Identification (Task 2)

The project uses various machine learning models, including fine-tuned versions of Llama3, LoRA, and Mistral, to perform keyphrase extraction and topic identification on text data.

## Project Structure
.
├── Keyphrase Prediction - Task 1
│   ├── Keyphrase-evaluation
│   │   ├── configs
│   │   ├── correlations
│   │   ├── embeddings
│   │   ├── eval_results
│   │   ├── external_datasets
│   │   ├── metrics
│   │   ├── model_outputs
│   │   ├── run_evaluation.ipynb
│   │   └── run_evaluation.py
│   ├── Keyphrase-generation
│   │   ├── FineTuned-Mistral7b.ipynb
│   │   └── gemma-5shot.ipynb
│   └── keyphrase-generation-finetuning
│       ├── FineTuning-llama3.ipynb
│       ├── FineTuning-LoRA-gemma.ipynb
│       ├── FineTuning-LoRA-mistral.ipynb
│       ├── Llama3-8b-1shot.ipynb
│       ├── Llama3-8b-5shot.ipynb
│       ├── llama3-finetuned.ipynb
│       └── mistral_5shot.ipynb
├── Topic Identification - Task 2
│   ├── Topic-evaluation
│   │   ├── Evaluation.ipynb
│   │   ├── EvaluationForMetaEvaluation.ipynb
│   │   ├── GroundTruthCreation.ipynb
│   │   └── mean&std.ipynb
│   └── Topic-generation
│       ├── Appearances&Sentiment.ipynb
│       ├── evaluation_results.json
│       ├── fewShotExamples.ipynb
│       ├── HighlightingTopics.ipynb
│       ├── Keyphrase-clustering
│       │   ├── Llama3_EvaluationTopics-Complete.ipynb
│       │   ├── Llama3_EvaluationTopics-Keyphrases.ipynb
│       │   ├── Llama3_EvaluationTopics-Reviews.ipynb
│       │   ├── Mistral7B_EvaluationTopics.ipynb
│       │   ├── NumberOfAppearances.ipynb
│       │   └── postProcessing.ipynb
├── project-demo
│   ├── pycache
│   ├── duplicates.py
│   ├── ikea_logo.svg.png
│   ├── ReviewsKeyphrasesDemo.py
│   └── TopicsDemo.py
├── README-1.md
├── README.md
└── requirements.txt

## Setup

1. Clone the repository:
git clone [repository-url]

2. Install the required dependencies:
pip install -r requirements.txt

3. Set up the necessary environment variables (if any).

## Usage

### Keyphrase Prediction (Task 1)

#### Evaluation
- Navigate to `Keyphrase Prediction - Task 1/Keyphrase-evaluation/`
- Run `run_evaluation.ipynb` or `run_evaluation.py` to evaluate keyphrase prediction models

#### Generation
- Navigate to `Keyphrase Prediction - Task 1/Keyphrase-generation/`
- Use `FineTuned-Mistral7b.ipynb` or `gemma-5shot.ipynb` for keyphrase generation

#### Fine-tuning
- Navigate to `Keyphrase Prediction - Task 1/keyphrase-generation-finetuning/`
- Use the various notebooks to fine-tune different models (Llama3, LoRA, Mistral) for keyphrase generation

### Topic Identification (Task 2)

#### Evaluation
- Navigate to `Topic Identification - Task 2/Topic-evaluation/`
- Use `Evaluation.ipynb` for general evaluation
- `GroundTruthCreation.ipynb` for creating ground truth data
- `mean&std.ipynb` for statistical analysis

#### Generation
- Navigate to `Topic Identification - Task 2/Topic-generation/`
- Use `Appearances&Sentiment.ipynb` for analyzing topic appearances and sentiment
- `HighlightingTopics.ipynb` for topic highlighting
- The `Keyphrase-clustering/` subfolder contains various notebooks for keyphrase clustering and evaluation

### Demo
- Navigate to `project-demo/`
- Run `ReviewsKeyphrasesDemo.py` for a demo of the keyphrase prediction
- Run `TopicsDemo.py` for a demo of the topic identification

## Contributing

[Include guidelines for contributing to the project]

## License

[Specify the license under which this project is released]

## Contact

[Provide contact information or links for further inquiries]