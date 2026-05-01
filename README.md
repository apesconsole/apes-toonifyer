# ⚡ Repo-Squeeze: Ultra-Context Compressor

**Repo-Squeeze** is a high-performance Python utility that transforms bloated code repositories into distilled, LLM-ready Markdown bundles. By applying aggressive logic-stripping and token budgeting, it achieves up to **95%+ compression** compared to raw repo dumps.

## 📊 Performance Benchmark

| Metric           | Before (Raw Bundle) | After (Repo-Squeeze) |
| :--------------- | :------------------ | :------------------- |
| **Total Tokens** | 990,109             | **47,934**           |
| **Context Fit**  | ❌ Overflow         | ✅ Optimized         |
| **Efficiency**   | Baseline            | **95.2% Reduction**  |

## 🚀 Features

- **Intelligent Minification**: Strips Python docstrings, JS/TS comments, and redundant whitespace.
- **Token Budgeting**: Prevents "runaway" files from hijacking your context by truncating files that exceed a specific token threshold.
- **Logic-First Filtering**: Automatically ignores non-essential files (images, binaries, node_modules) and focuses on high-value logic (`.py`, `.ts`, `.js`, etc.).
- **LLM-Native Formatting**: Uses standard Markdown block syntax that models are pre-trained to parse accurately.

## 🛠️ Installation & Usage

1. **Clone the tool** into your workspace.
2. **Install Dependencies**:
   ```bash
   pip install tiktoken
   ```
3. **Run the Compressor**:
   ```bash
   python bundle_repo.py
   ```
4. **Locate Output**: Your distilled context is ready at `/your-context/ultra_bundle.md`.

## 📥 Why it works

Most repositories are 80% "noise" (documentation, styling, and boilerplate). Repo-Squeeze extracts the **"Signal"**—the actual logic flows—ensuring your AI assistant understands the architecture without hitting rate limits or "forgetting" details due to excessive noise.
