## Websight

WebSight is a machine-learning based HTML/website summarizer engine built in Python which makes it possible to feed in a website and create a navigatable format for those who are occularly impaired. 


# How it Works

Websight utilizes [sklearn](http://scikit-learn.org/stable/) to create a machine learning system that takes in a website and identifies all components of the website. After this step it sorts and labels them. Afterwards it reformats the website into a series of arrays based on the header label assigned to the blocks of the website. Once in the array form, the user can navigate through the newly formatted website type.

# Getting Started

At this stage the program to get it to work you must manually enter the htmlsummarizer.py document and manually enter the website url into the code. This location is clearly commented. Once you have entered the desired website url you should just be able to run the htmlsummarizer.py file(currently the newly formatted website is navigable through the requested commands in the console or terminal).

# What Each File Does

# Development pattern for contributors

1. [Create a fork](https://help.github.com/articles/fork-a-repo/) of
   the [main WebSight repository](https://github.com/8NW/AT20PercentProject) on GitHub.
2. Make your changes in a branch named something different from `master`, e.g. create
   a new branch `my-pull-request`.
3. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/).
4. Please follow the [Python style guide for PEP-8](https://www.python.org/dev/peps/pep-0008/).
5. Use the projects [built-in automated testing](http://chatterbot.readthedocs.io/en/latest/testing.html)
   to help make sure that your contribution is free from errors.
