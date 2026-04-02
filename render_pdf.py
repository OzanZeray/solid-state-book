"""Render the complete book Markdown to PDF using fpdf2."""
import re
from fpdf import FPDF


class BookPDF(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.set_auto_page_break(auto=True, margin=25)
        self.add_font('DejaVu', '', 'C:/Windows/Fonts/times.ttf')
        self.add_font('DejaVu', 'B', 'C:/Windows/Fonts/timesbd.ttf')
        self.add_font('DejaVu', 'I', 'C:/Windows/Fonts/timesi.ttf')
        self.add_font('DejaVu', 'BI', 'C:/Windows/Fonts/timesbi.ttf')
        self.add_font('Mono', '', 'C:/Windows/Fonts/consola.ttf')

    def header(self):
        if self.page_no() > 1:
            self.set_font('DejaVu', 'I', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 5, 'Experimental Data for Introductory Solid State Physics', align='C')
            self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', '', 9)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, str(self.page_no()), align='C')

    def chapter_title(self, title):
        self.add_page()
        self.set_font('DejaVu', 'B', 20)
        self.set_text_color(44, 62, 80)
        self.multi_cell(0, 10, title)
        self.set_draw_color(44, 62, 80)
        self.line(10, self.get_y() + 2, 200, self.get_y() + 2)
        self.ln(8)

    def section_title(self, title):
        self.ln(4)
        self.set_font('DejaVu', 'B', 14)
        self.set_text_color(52, 73, 94)
        self.multi_cell(0, 8, title)
        self.set_draw_color(189, 195, 199)
        self.line(10, self.get_y() + 1, 200, self.get_y() + 1)
        self.ln(4)

    def subsection_title(self, title):
        self.ln(3)
        self.set_font('DejaVu', 'B', 12)
        self.set_text_color(44, 62, 80)
        self.multi_cell(0, 7, title)
        self.ln(2)

    def body_text(self, text):
        self.set_font('DejaVu', '', 10)
        self.set_text_color(26, 26, 26)
        self.set_x(10)
        try:
            self.multi_cell(190, 5.5, text)
        except Exception:
            pass
        self.ln(2)

    def bold_text(self, text):
        self.set_font('DejaVu', 'B', 10)
        self.set_text_color(26, 26, 26)
        self.set_x(10)
        try:
            self.multi_cell(190, 5.5, text)
        except Exception:
            pass
        self.ln(2)

    def italic_text(self, text):
        self.set_font('DejaVu', 'I', 10)
        self.set_text_color(44, 62, 80)
        self.set_x(10)
        try:
            self.multi_cell(190, 5.5, text)
        except Exception:
            pass
        self.ln(2)

    def quote_block(self, text):
        self.set_fill_color(240, 247, 253)
        self.set_font('DejaVu', 'I', 9.5)
        self.set_text_color(44, 62, 80)
        self.set_x(18)
        self.multi_cell(172, 5.5, text, fill=True)
        self.ln(3)

    def table_row(self, cells, header=False):
        col_width = 180 / len(cells) if cells else 180
        self.set_font('DejaVu', 'B' if header else '', 8.5)
        if header:
            self.set_fill_color(236, 240, 241)
            self.set_text_color(44, 62, 80)
        else:
            self.set_fill_color(255, 255, 255)
            self.set_text_color(26, 26, 26)
        for cell in cells:
            self.cell(col_width, 6, str(cell).strip(), border=1, fill=True, align='C')
        self.ln()

    def separator(self):
        self.ln(3)
        self.set_draw_color(200, 200, 200)
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(5)


def parse_and_render(md_text, pdf):
    lines = md_text.split('\n')
    i = 0
    in_table = False
    table_header_done = False

    while i < len(lines):
        line = lines[i].rstrip()

        # Skip YAML front matter
        if line == '---' and i < 5:
            i += 1
            while i < len(lines) and lines[i].rstrip() != '---':
                i += 1
            i += 1
            continue

        # Empty line
        if not line:
            if in_table:
                in_table = False
                table_header_done = False
                pdf.ln(3)
            i += 1
            continue

        # Horizontal rule
        if line.startswith('---') and len(line.strip()) <= 5:
            pdf.separator()
            i += 1
            continue

        # Part headers (# Part ...)
        if line.startswith('# Part ') or line.startswith('# Experimental Data'):
            pdf.chapter_title(clean(line.lstrip('#').strip()))
            i += 1
            continue

        # Chapter header (# Chapter N:)
        if re.match(r'^# Chapter \d', line):
            pdf.chapter_title(clean(line.lstrip('#').strip()))
            i += 1
            continue

        # H1
        if line.startswith('# '):
            pdf.chapter_title(clean(line[2:].strip()))
            i += 1
            continue

        # H2
        if line.startswith('## '):
            pdf.section_title(clean(line[3:].strip()))
            i += 1
            continue

        # H3
        if line.startswith('### '):
            pdf.subsection_title(clean(line[4:].strip()))
            i += 1
            continue

        # H4
        if line.startswith('#### '):
            pdf.bold_text(clean(line[5:].strip()))
            i += 1
            continue

        # Table row
        if '|' in line and line.strip().startswith('|'):
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            # Skip separator rows (|---|---|)
            if all(set(c.strip()) <= {'-', ':', ' '} for c in cells):
                i += 1
                continue
            if not in_table:
                in_table = True
                table_header_done = False
                pdf.table_row([clean(c) for c in cells], header=True)
                table_header_done = True
            else:
                pdf.table_row([clean(c) for c in cells], header=False)
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            quote_lines = [line[2:]]
            while i + 1 < len(lines) and lines[i+1].startswith('> '):
                i += 1
                quote_lines.append(lines[i][2:])
            pdf.quote_block(clean(' '.join(quote_lines)))
            i += 1
            continue

        # Bullet list
        if line.startswith('- ') or line.startswith('* '):
            pdf.set_font('DejaVu', '', 10)
            pdf.set_text_color(26, 26, 26)
            pdf.set_x(15)
            pdf.multi_cell(180, 5.5, '  * ' + clean(line[2:]))
            i += 1
            continue

        # Numbered list
        m = re.match(r'^(\d+)\.\s+(.+)', line)
        if m:
            pdf.set_font('DejaVu', '', 10)
            pdf.set_text_color(26, 26, 26)
            pdf.set_x(15)
            pdf.multi_cell(180, 5.5, f'  {m.group(1)}. ' + clean(m.group(2)))
            i += 1
            continue

        # Regular paragraph — collect consecutive lines
        para_lines = [line]
        while i + 1 < len(lines) and lines[i+1].strip() and not lines[i+1].startswith('#') and not lines[i+1].startswith('|') and not lines[i+1].startswith('>') and not lines[i+1].startswith('- ') and not lines[i+1].startswith('---'):
            i += 1
            para_lines.append(lines[i])
        text = ' '.join(para_lines)
        text = clean(text)
        if text.startswith('**') and text.endswith('**'):
            pdf.bold_text(text.strip('*'))
        else:
            pdf.body_text(text)
        i += 1


def clean(text):
    """Remove markdown formatting for PDF text."""
    text = re.sub(r'\$\$.*?\$\$', '[equation]', text, flags=re.DOTALL)
    text = re.sub(r'\$([^$]+)\$', r'\1', text)
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'\1', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # [text](url) -> text
    text = text.replace('$$', '')
    text = text.replace('\\', '')
    # Replace special characters that might cause encoding issues
    text = text.replace('→', '->')
    text = text.replace('≈', '~')
    text = text.replace('≥', '>=')
    text = text.replace('≤', '<=')
    text = text.replace('×', 'x')
    text = text.replace('±', '+/-')
    text = text.replace('−', '-')
    text = text.replace('∞', 'infinity')
    text = text.replace('\u200b', '')
    text = text.replace('α', 'alpha')
    text = text.replace('β', 'beta')
    text = text.replace('γ', 'gamma')
    text = text.replace('δ', 'delta')
    text = text.replace('ε', 'epsilon')
    text = text.replace('θ', 'theta')
    text = text.replace('λ', 'lambda')
    text = text.replace('μ', 'mu')
    text = text.replace('ν', 'nu')
    text = text.replace('π', 'pi')
    text = text.replace('ρ', 'rho')
    text = text.replace('σ', 'sigma')
    text = text.replace('τ', 'tau')
    text = text.replace('φ', 'phi')
    text = text.replace('χ', 'chi')
    text = text.replace('ψ', 'psi')
    text = text.replace('ω', 'omega')
    text = text.replace('Ω', 'Ohm')
    text = text.replace('Θ', 'Theta')
    text = text.replace('Δ', 'Delta')
    text = text.replace('κ', 'kappa')
    text = text.replace('ℏ', 'hbar')
    text = text.replace('⟨', '<')
    text = text.replace('⟩', '>')
    text = text.replace('—', '--')
    text = text.replace('–', '-')
    text = text.replace('"', '"')
    text = text.replace('"', '"')
    text = text.replace(''', "'")
    text = text.replace(''', "'")
    text = text.replace('²', '^2')
    text = text.replace('³', '^3')
    text = text.replace('⁴', '^4')
    text = text.replace('⁻', '-')
    text = text.replace('¹', '1')
    # Remove any remaining non-latin1 chars
    text = text.encode('latin-1', errors='replace').decode('latin-1')
    return text.strip()


if __name__ == '__main__':
    print("Reading book...")
    with open('book/COMPLETE_BOOK.md', 'r', encoding='utf-8') as f:
        md_text = f.read()

    print("Generating PDF...")
    pdf = BookPDF()

    # Title page
    pdf.add_page()
    pdf.ln(50)
    pdf.set_font('DejaVu', 'B', 28)
    pdf.set_text_color(44, 62, 80)
    pdf.multi_cell(0, 14, 'Experimental Data for\nIntroductory Solid State\nPhysics', align='C')
    pdf.ln(20)
    pdf.set_font('DejaVu', '', 16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, 'Ozan Zeray', align='C')
    pdf.ln(30)
    pdf.set_font('DejaVu', 'I', 11)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 6, 'A companion to the topics of introductory solid state physics,\npresenting the real experimental data behind the theory.', align='C')

    # Render content
    parse_and_render(md_text, pdf)

    # Save
    output = 'book/COMPLETE_BOOK.pdf'
    pdf.output(output)
    import os
    size_mb = os.path.getsize(output) / (1024 * 1024)
    print(f"SUCCESS: {output} ({size_mb:.1f} MB)")
