"""Streamlit demo: ask a question, see the clauses that answer it.

    streamlit run app.py
"""

from pathlib import Path

import streamlit as st

from clausesearch.retrieve import load_pipeline

CONFIG_DIR = Path(__file__).resolve().parent / "configs"
CONTEXT_CHARS = 300  # text shown on each side of a passage when expanded


@st.cache_resource
def get_pipeline(config_path: str):
    # Built once per config and reused across reruns, since indexing reads every contract.
    return load_pipeline(config_path)


st.set_page_config(page_title="Contract Clause Search", layout="wide")
st.title("Contract Clause Search")
st.caption("Finds the passages in the indexed contracts that answer a question, or says none does.")

with st.sidebar:
    configs = sorted(CONFIG_DIR.glob("*.yaml"))
    config_path = st.selectbox("Pipeline config", configs, format_func=lambda p: p.stem)
    top_n = st.slider("Passages to show", 1, 20, 5)

pipeline = get_pipeline(str(config_path))
st.sidebar.write(f"{len(pipeline.corpus)} contracts, {len(pipeline.chunks):,} passages indexed")

question = st.text_input(
    "Question",
    placeholder="Consider the Sponsorship Agreement between ...; What is the governing law for this contract?",
)

if question:
    result = pipeline(question)
    if result["abstain"]:
        st.warning("No relevant clause found in the indexed contracts.")
    else:
        for rank, p in enumerate(result["passages"][:top_n], 1):
            start, end = p["span"]
            text = pipeline.corpus[p["file_path"]]
            with st.container(border=True):
                st.markdown(f"**#{rank}** · `{p['file_path']}` · characters {start}–{end} · score {p['score']:.2f}")
                if p.get("section"):
                    st.caption(f"Section: {p['section']}")
                st.write(text[start:end])
                with st.expander("Show surrounding text"):
                    st.text(text[max(0, start - CONTEXT_CHARS) : end + CONTEXT_CHARS])
