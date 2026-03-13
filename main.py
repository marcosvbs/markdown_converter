import pymupdf4llm
import os

ROOT_INPUT_PATH = "source_docs"
ROOT_OUTPUT_PATH = "converted_docs"

def clear_markdown(markdown_text):
    # Cleans empty lines and trims whitespace
    clean_markdown = [line.strip() for line in markdown_text.split("\n") if line.strip()]
    return "\n".join(clean_markdown)

def convert_document(doc_name):
    doc_path = f"{ROOT_INPUT_PATH}/{doc_name}"

    if not os.path.exists(doc_path):
        print(f"❌ Error: The file '{doc_path}' was not found.\n")
        return

    print(f"⏳ Processing '{doc_path}'... This may take a few seconds.\n")

    try:
        raw_markdown_content = pymupdf4llm.to_markdown(doc_path)
        final_markdown_content = clear_markdown(raw_markdown_content)

        name_base = os.path.splitext(doc_name)[0]
        output_doc_name = f"converted_{name_base}.md"
        output_path = os.path.join(ROOT_OUTPUT_PATH, output_doc_name)

        with open(output_path, "w", encoding="utf-8") as converted_doc:
            converted_doc.write(final_markdown_content)
        
        print(f"✅ Success! The file '{output_doc_name}' is ready for AI use.\n")

    except Exception as error:
        print(f"⚠️ An error occurred during conversion: {error}\n")


def main():
    doc_name = ''

    while doc_name != '0':
        doc_name = input("Enter a document name (with extension) or 0 to exit: ")

        print("\n")

        if doc_name != '0':
            convert_document(doc_name)

if __name__ == "__main__":
    main()