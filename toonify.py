import os
import sys
import re
import tiktoken

def compress_code(content, ext):
    """Aggressively removes comments and minifies code structure."""
    if ext in ['.py']:
        # Remove docstrings and comments
        content = re.sub(r'(""".*?"""|\'\'\'.*?\'\'\')', '', content, flags=re.DOTALL)
        content = re.sub(r'#.*', '', content)
    elif ext in ['.js', '.ts', '.tsx']:
        # Remove multi-line and single-line comments
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        content = re.sub(r'//.*', '', content)
    
    # Remove excessive whitespace/newlines
    content = re.sub(r'\n\s*\n', '\n', content) 
    return content.strip()

def main():
    repo_path = input("Enter repo path: ").strip()
    limit_per_file = 3000  # Max tokens per file to prevent "runaway" data files
    
    blocklist = {'node_modules', 'venv', '.git', 'your-toon', 'your-context', 'dist', 'build'}
    # Focus only on high-value logic files
    logic_exts = {'.py', '.js', '.ts', '.tsx', '.go', '.rs'}
    
    enc = tiktoken.get_encoding("cl100k_base")
    bundle = []
    final_tokens = 0

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in blocklist and not d.startswith('.')]
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in logic_exts:
                continue # Skip large JSON/CSS/MD files that bloat tokens

            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    raw_content = f.read()
                    
                    # 1. Strip comments and whitespace
                    clean_content = compress_code(raw_content, ext)
                    
                    # 2. Budgeting: Don't let one file eat the whole context
                    tokens = enc.encode(clean_content)
                    if len(tokens) > limit_per_file:
                        clean_content = enc.decode(tokens[:limit_per_file]) + "\n... [TRUNCATED]"
                    
                    formatted = f"FILE: {os.path.relpath(file_path, repo_path)}\n```\n{clean_content}\n```\n"
                    bundle.append(formatted)
                    final_tokens += len(enc.encode(formatted))
            except:
                continue

    # Save output
    output_path = os.path.join(repo_path, "your-context", "ultra_bundle.md")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(bundle)

    print(f"\n⚡ Ultra-Compression Report:")
    print(f"   Final Tokens: {final_tokens}")
    print(f"   Estimated Savings: ~{((990109 - final_tokens) / 990109 * 100):.1f}%")
    sys.exit(0)

if __name__ == "__main__":
    main()
