# Experimental Data for Introductory Solid State Physics — Book Project

## Project Context
This is a LaTeX book project presenting real experimental data and studies for every topic in introductory solid state physics (following Kittel's chapter structure, Ch 1-22). The book supplements theory with actual experimental evidence.

## Tech Stack
- **LaTeX** (`book` class, dark mode, A4)
- **Source files:** `tex/main.tex` (and future chapter files)
- **Reference PDFs:** `alakali kitaplar/` directory
- **arXiv papers:** `arxiv-papers/` directory (MCP server storage)

## MCP Servers Available
- **arxiv-mcp-server** — Search arXiv, fetch paper content, store locally
- **arxiv-latex-mcp** — Fetch arXiv LaTeX sources for precise math interpretation

## Writing Guidelines
- Each chapter focuses on EXPERIMENTAL DATA, not theory derivation
- Minimal theoretical framing (just enough context for the data)
- Always cite original experimental sources
- Use `pgfplots` for data visualization where possible
- Use `siunitx` for all physical quantities and units
- Dark mode: black background, white text (already configured)

## Skills to Use
When working on this project, leverage these skills as needed:

### /pdf
Use for reading and extracting content from the reference PDFs in `alakali kitaplar/`:
- `exp techniques in cond mat at low temp.pdf`
- `correlated electron exp methods.pdf`
- `field guide solid state physics.pdf`
- `fundamentals of semicon Contents.pdf`

### /canvas-design
Use for generating scientific diagrams and figures (crystal structures, experimental setups, schematic illustrations) as PNG/PDF for inclusion in LaTeX chapters.

### /search-first
Use BEFORE writing any chapter to research and find:
- Original experimental papers on arXiv
- Existing open datasets
- Historical landmark experiments for each topic

### /article-writing
Use for drafting long-form chapter content with proper scientific writing style.

## File Structure
```
tex/
  main.tex          — Main LaTeX document
  chapters/         — Individual chapter .tex files (to be created)
  figures/          — Plots and diagrams (to be created)
  data/             — Raw experimental data CSV files (to be created)
alakali kitaplar/   — Reference books (PDFs)
arxiv-papers/       — Downloaded arXiv papers (MCP server storage)
PLAN.md             — Full chapter structure and data strategy
```

## LaTeX Conventions
- Book class with `\chapter`, `\section`, `\subsection` hierarchy
- Packages to use: `graphicx`, `booktabs`, `siunitx`, `hyperref`, `amsmath`, `pgfplots`, `biblatex`
- All experimental data tables should use `booktabs` formatting
- All plots from data should use `pgfplots` with data files in `data/`
- Bibliography managed via `biblatex` with a central `.bib` file
