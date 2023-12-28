# Legal Document Precedent Extraction and Classification
This repository contains the code for the extraction and classification of precedents in legal documents. The project involves working with various types of legal cases such as 'Writ Petition,' 'Civil Appeal,' and 'Twenty_six.' The output for each case is available in the respective folders named 'precedents classified output.' Individual case outputs, corresponding to files like filename.xml or filename.txt, can be found in folders named 'filename output.txt.'

## Project Structure:
- Writ Petition
- Civil Appeal
- Twenty_six
- precedents classified output
- filename output.txt
  
## Code Execution:
The main Python code file for preprocessing, extraction, and classification is Data Analysis.ipynb. Each block in the file is thoroughly commented with its functionality at the beginning.

## Project Highlights:
- Extracted and classified precedents and statutes from 150+ legal documents with a high accuracy of 90% using rule-based approaches.
- Conducted sentiment analysis using nltk and spaCy libraries to categorize precedents into Relied, Distinguished, and Overruled.
- Engineered a deep learning model incorporating Bert Tokenizer, bi-Directional LSTM Encoder-Decoder, Attention Pooling, and Conditional Random Field Layer with Adam Optimizer.
- Achieved a test weighted F1 score of 82.61% using the Negative Log-Likelihood loss function on a Gold Dataset containing 2471 RR labeled cases.
