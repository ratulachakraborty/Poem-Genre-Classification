# Poem-Genre-Classification
Developed a machine learning algorithm which classifies the genre of the poem using a labelled data-set and natural language processing packages of python
Used two different classification models: Support Vector machine(SVM) and Random Forest Classifier and accuracies have been found.

Features:

1) Tokenise - Broke the paragraph using nltk sent_tokeniser and converted into a file having end of line replaced with "\n"
Then, further broke them into tokens and a simple linguistic change is done.

2) Length of Tokens: Length of tokens

3)Average Token Count: average token count

4) Largest Token: Largest token

5)Empath values : Used an inbuilt text sentiment analyser name as "Empath". It calculates normalised values of different abstract
nouns ,present in the given string.

6) Text Blob: used another inbuilt sentiment analyser which classifies between positive,negative and neutral emotion types.

