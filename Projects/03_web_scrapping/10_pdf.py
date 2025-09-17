"""
    Debug needed in the get_text method,
"""
import fitz

def read_pdf(file_path):
    doc = fitz.open(file_path)
    print(doc)
    all_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        # all_text += page.get_textbox()

    doc.close()
    return all_text

if __name__ == "__main__":
    file_path = 'time.pdf'
    content = read_pdf(file_path)
    print(content)