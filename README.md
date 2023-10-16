# lab-activity-3-CSBlk3

# Tagalog Porter Stemmer

Tagalog Porter Stemmer is a Python library for stemming Tagalog words. Stemming is the process of reducing inflected (or sometimes derived) words to their word stem, base, or root form. The Tagalog Porter Stemmer library is specifically designed to work with Tagalog, one of the official languages of the Philippines.

## Installation

You can install the Tagalog Porter Stemmer library via pip:

```bash
pip install tagalog-porter-stemmer

from tagalog_porter_stemmer import stem

word = "kumakain"
stemmed_word = stem(word)
print(stemmed_word)  # Output: "kain"

 # How It Works
The Tagalog Porter Stemmer library is an implementation of the Porter stemming algorithm adapted for the Tagalog language. It performs the following steps to stem a Tagalog word:

Removes common prefixes.
Processes verb affixes and tense markers.
Handles common suffixes.
Applies additional rules specific to Tagalog stemming.
The library is designed to be easy to use and effective for Tagalog text analysis, search, and retrieval.


# EXAMPLES

from tagalog_porter_stemmer import stem

words = ["naglalakad", "kinakain", "nagpapalakad", "kumakanta"]
stemmed_words = [stem(word) for word in words]
print(stemmed_words)  
# Output: ['lakad', 'kain', 'lakad', 'kanta']
# License
This project is licensed under the MIT License - see the LICENSE file for details.

 # Acknowledgments
This Tagalog Porter Stemmer library is inspired by the original Porter stemming algorithm, adapted and customized for the Tagalog language. We extend our gratitude to the Porter stemming algorithm authors and contributors.

# Contributing
Contributions to this project are welcome. Please feel free to submit issues, feature requests, or pull requests on our GitHub repository.

If you encounter any issues or have questions, please contact Your Email Address.

Enjoy stemming Tagalog words with the Tagalog Porter Stemmer library!
