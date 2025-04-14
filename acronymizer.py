"""
Text Acronymizer Module

This script processes raw text files to identify and convert
named entities and capitalized phrases into acronyms.

Purpose:
- Normalize named entities for compact representation.
- Simplify capitalized phrases to acronyms to improve consistency.

Functionality:
- Uses SpaCy for Named Entity Recognition (NER).
- Applies regex to detect capitalized multi-word phrases.
- Replaces these with their respective acronyms.

Dependencies:
- Requires `spacy` and English model `en_core_web_sm`.
- Utilizes built-in `re` for regex matching.

Limitations:
- May over-acronymize short proper names (e.g., “New”).
- Assumes input text is English and properly capitalized.

Version: 1.0.0  
Created: 2025-04-14  
Last Modified: 2025-04-14 by Marco  
License: MIT  

To cite this code, use:  
Marco. (2025). *Text Acronymizer Module (v1.0.0)*. https://doi.org/10.xxxx/zenodo.xxxxxxx
"""

import spacy  # Natural language processing library
import re     # Regular expressions for pattern matching

def convert_named_entities_to_acronyms(text):
    """
    Converts named entities (people, locations, etc.) in the text
    into acronyms based on their initial letters.

    Parameters:
    - text (str): The input text to process.

    Returns:
    - str: Modified text with named entities replaced by acronyms.

    Notes:
    - Only "PERSON", "GPE", "LOC", and "ORG" entities are included.
    - Acronyms are built from capital initials of each word.
    - Avoids duplicate replacements using a memory dictionary.

    Example:
    "Barack Obama visited New York." → "BO visited NY."
    """
    nlp = spacy.load("en_core_web_sm")  # Load the small English model
    doc = nlp(text)                     # Run NLP pipeline on text
    replaced = text                     # Keep original for progressive replacement
    seen = {}                           # Track already replaced entities

    for ent in doc.ents:
        if ent.label_ in ["PERSON", "GPE", "LOC", "ORG"]:
            if ent.text not in seen:
                # Create acronym from capitalized initials
                acronym = ''.join([
                    word[0].upper() for word in ent.text.split() if word[0].isalpha()
                ])
                seen[ent.text] = acronym  # Store acronym to avoid duplicates
                replaced = replaced.replace(ent.text, acronym)  # Replace in text
    
    return replaced  # Return modified text


def convert_capitalized_phrases_to_acronyms(text):
    """
    Detects capitalized multi-word phrases and converts them to acronyms.

    Parameters:
    - text (str): Text with or without named entity acronyms.

    Returns:
    - str: Text with capitalized phrases replaced by acronyms.

    Notes:
    - Matches two or more consecutive capitalized words.
    - Each acronym is formed from the first letter of each word.

    Example:
    "Artificial Intelligence System" → "AIS"
    """

    # Regex: Matches at least 2 capitalized words
    pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b'

    def acronymize(match):
        phrase = match.group(0)  # Get matched phrase
        acronym = ''.join(word[0].upper() for word in phrase.split())
        return acronym  # Return acronym for substitution

    return re.sub(pattern, acronymize, text)  # Replace all matches


def process_text_file(filename):
    """
    Orchestrates full acronymization process from a text file.

    Parameters:
    - filename (str): Path to the text file to process.

    Returns:
    - str: Fully acronymized text content.

    Notes:
    - Reads the file as UTF-8.
    - Applies named entity and phrase acronymization sequentially.
    """

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()  # Read full text from file

    ner_converted = convert_named_entities_to_acronyms(content)
    fully_converted = convert_capitalized_phrases_to_acronyms(ner_converted)

    return fully_converted  # Final transformed text


# --- Example Usage ---
if __name__ == "__main__":
    file_path = "input.txt"  # Path to input file (change if needed)
    result = process_text_file(file_path)  # Process and transform text
    print(result)  # Output acronymized result
