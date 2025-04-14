# Text Acronymizer Module

A lightweight Python module for converting named entities and capitalized phrases into acronyms using natural language processing and regular expressions.

## 📌 Purpose

This tool helps standardize and compress text by replacing proper names and formal phrases with acronyms. It's useful for:

- Text summarization
- Preprocessing for NLP tasks
- Creating anonymized or encoded corpora

---

## ⚙️ Features

- Named Entity Recognition via [spaCy](https://spacy.io/)
- Regex-based detection of capitalized phrases
- Chainable transformations (NER → Capital Phrases)
- Simple integration with file processing

---

## 🧠 How It Works

1. Detect named entities like **Barack Obama** or **New York**.
2. Convert them into acronyms: `BO`, `NY`.
3. Detect multi-word capitalized phrases: **Artificial Intelligence System** → `AIS`.
4. Output the transformed text.

---

## 🚀 Usage

```bash
python acronymizer.py
