"""Download the CUAD part of LegalBench-RAG into data/."""

from pathlib import Path

from huggingface_hub import snapshot_download

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Pinned so every run gets the same files the reported numbers came from.
REVISION = "2b9c248bc8179ef0908fd6ba01d50b156facd48b"

if __name__ == "__main__":
    snapshot_download(
        repo_id="awinml/legalbench-rag",
        repo_type="dataset",
        revision=REVISION,
        allow_patterns=["benchmarks/cuad.json", "corpus/cuad/*"],
        local_dir=DATA_DIR,
    )
    n_files = len(list((DATA_DIR / "corpus" / "cuad").glob("*.txt")))
    print(f"Downloaded cuad.json and {n_files} CUAD contracts to {DATA_DIR}")
