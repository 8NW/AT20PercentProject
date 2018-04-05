# Websight

WebSight is a machine-learning based HTML/website summarizer engine built in Python which makes it possible to feed in a website and create a navigatable format for those who are occularly impaired. 


## How it Works

Websight utilizes [sklearn](http://scikit-learn.org/stable/) to create a machine learning system that takes in a website and identifies all components of the website. After this step it sorts and labels them. Afterwards it reformats the website into a series of arrays based on the header label assigned to the blocks of the website. Once in the array form, the user can navigate through the newly formatted website type.

## Getting Started

At this stage the program to get it to work you must manually enter the htmlsummarizer.py document and manually enter the website url into the code. This location is clearly commented. Once you have entered the desired website url you should just be able to run the htmlsummarizer.py file using terminal with the command "python htmlsummarizer.py"(currently the newly formatted website is navigable through the requested commands in the console or terminal).

## What Each File Does

#### htmlsummarizer.py

The hmlsummarizer.py file is the core of code of the project. This takes the website and parses it using requests. It then passes it through the machine learning file and labels the website into the predifined labels. The website is then sorted into an array using the summarizing functions. Then it becomes navigable for the user. However, currently the list is just printed as it is easier to test.

#### htmlparser.py

The htmlparser.py file takes the website and parses it. The program then takes each of the compnents of the website and asks the user to label it for the machine learning program. This allows the user to also enter new labels for the machine learning labeling. This is so a user can build up the library that the machine learning program references.

#### mlTrainer.py
This is the machine learning program. These should not be deleted or tampered with through direct means. To add more data to the machine learning library the user should use the htmlparser.py file.

#### pkl documents

The pkl documents within the project act as dictionaries for the data that the other files access. These should not be deleted or tampered with as they contain the data that the machine learning uses.

## Development pattern for contributors

1. [Create a fork](https://help.github.com/articles/fork-a-repo/) of
   the [main WebSight repository](https://github.com/8NW/AT20PercentProject) on GitHub.
2. Make your changes in a branch named something different from `master`, e.g. create
   a new branch `my-pull-request`.
3. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/).
4. Please follow the [Python style guide for PEP-8](https://www.python.org/dev/peps/pep-0008/).
5. Make sure that your contribution is free from errors.
