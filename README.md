# Simple Evaluation Playground

This repository contains a lightweight retrieval-augmented generation (RAG) evaluation workflow centered on the Bridgeport Series 1 milling machine manuals. It couples a FAISS vector store of OCR'd documentation with LangChain, LangGraph, and LangSmith tooling so you can build, run, and grade question‑answering experiments quickly.

## Reading if you want to understand how I did this 
- [Langchain - Eval quick start](https://docs.langchain.com/langsmith/evaluate-rag-tutorial#heres-a-consolidated-script-with-all-the-above-code)


## Repository Structure
- `data/` — Source PDFs and Markdown exports produced by OCR.
- `evalsets/` — CSV datasets of milling machine questions and ground-truth answers.
- `scripts/create_vectostore_md.ipynb` — Notebook that chunks Markdown files and writes the `vstore/` FAISS index.
- `simple_eval.ipynb` — Main notebook that loads the vector store, runs the LangGraph RAG chain, and submits correctness evaluations to LangSmith.
- `vstore/` — Persisted FAISS index (`index.faiss`/`index.pkl`) used at runtime.

## Prerequisites
- If you are interested in langsmith tracing, you might want to setup a project. When you set it up, it will give you a project name and api. Paste that in your .env variables. 
- Python 3.10+ (matching the LangChain/LangGraph requirements).
- An OpenAI API key with access to `gpt-4`, `gpt-4o`, and `text-embedding-3-small`.
- A LangSmith account and API key for dataset management and evaluation runs.

Store your secrets in a `.env` file at the project root (loaded via `dotenv`), for example:

```
OPENAI_API_KEY=sk-...
LANGCHAIN_API_KEY=lsv2-...
LANGCHAIN_PROJECT=simple-eval
LANGCHAIN_TRACING_V2=true
```

## Installation
1. Create and activate a virtual environment.
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```


## Usage
1. **Build the vector store** (if `vstore/` is missing or you want to refresh embeddings):
   - Open `scripts/create_vectostore_md.ipynb`, ensure the configuration block points at your Markdown sources, and execute the notebook.
2. **Upload evaluation data**:
   - `simple_eval.ipynb` reads `evalsets/mill_test.csv`, creates a LangSmith dataset (if needed), and uploads the rows as examples.
3. **Run the RAG evaluation**:
   - Execute the remaining cells in `simple_eval.ipynb` to load the FAISS store, answer each question via the LangGraph pipeline, and score correctness with a structured `gpt-4o` grader.
4. **Inspect results**:
   - Review the generated LangSmith run in the web UI for per-question traces, grading rationales, and aggregate metrics.

## Data Notes
- Markdown files under `data/ocr_md/` are the chunked OCR outputs of the milling manuals and drive the knowledge base.
- CSV files in `evalsets/` must contain `question` and `answer` columns; you can curate additional evaluation sets by following this schema.

## Next Steps with the projects 
- Experiment with alternative embedding models (e.g., `HuggingFaceEmbeddings`) or different chunk sizes when rebuilding the vector store. Latency 
- Add more evaluators (e.g., response latency, groundedness) via LangSmith to broaden coverage.
- Add non-binary likkert style evalutors. 
- Experiment with Anthropic's [Petri Evaluation Agent](https://alignment.anthropic.com/2025/petri/). I was reading the blog post and found a lot of interesting topics and tools that could be used on this project, specifially for safety. Altough the project is geared towards basing frontier models and their interactions with tools, we can craete similar testing methods to see where our RAG lacks. 

## Architecture Overview

The following diagram outlines the document processing and retrieval pipeline used to prepare and evaluate the Bridgeport milling machine manuals.  
It illustrates how PDF manuals are processed through OCR and divided into two data flows — one for image data (dense captions and CSV creation) and another for textual Markdown (chunking and embedding for RAG).

```mermaid
graph TD

    %% --- Input Stage ---
    A[PDF File] --> B[Mistral OCR]

    %% --- Split into two parallel data paths ---
    B --> C1[Extracted Images]
    B --> C2[Extracted Markdown]

    %% --- Image Path ---
    subgraph "Image Processing Path"
        C1 --> D1[Store Images in Folder]
        D1 --> E1[Generate Dense Captions]
        E1 --> F1[Create CSV (Image + Caption Data)]
    end

    %% --- Text Path ---
    subgraph "Text Processing Path"
        C2 --> D2[Chunk Text Data]
        D2 --> E2[Embed Chunks into Vector Store]
        E2 --> F2[Retrieval-Augmented Generation (RAG)]
    end

    %% --- Layout Connections ---
    F1 -.-> F2
    F2 -.-> F1