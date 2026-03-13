import pymupdf4llm
import os

ROOT_INPUT_PATH = "source_docs"
ROOT_OUTPUT_PATH = "converted_docs"

def clear_markdown(markdown_text):
    clean_markdown = [line.strip() for line in markdown_text.split("\n") if line.strip()]

    return "\n".join(clean_markdown)

def converter_documento(doc_name):
    doc_path = f"{ROOT_INPUT_PATH}/{doc_name}"

    if not os.path.exists(doc_path):
        print(f"❌ Erro: O arquivo '{doc_path}' não foi encontrado.")
        return

    print(f"⏳ Processando '{doc_path}'... Isso pode levar alguns segundos.")

    try:
        raw_markdown_content = pymupdf4llm.to_markdown(doc_path)
        final_markdown_content = clear_markdown(raw_markdown_content)

        name_base = os.path.splitext(doc_name)[0]
        output_doc_name = f"converted_{name_base}.md"
        output_path = os.path.join(ROOT_OUTPUT_PATH, output_doc_name)

        with open(output_path, "w", encoding="utf-8") as converted_doc:
            converted_doc.write(final_markdown_content)
        
        print(f"✅ Concluído! O arquivo '{output_doc_name}' está pronto para ser usado na IA.")

    except Exception as erro:
        print(f"⚠️ Houve um erro na conversão: {erro}")


def main():
    doc_name = ''

    while doc_name != '0':
        doc_name = input("Enter a document name and format or 0 to stop the program: ")

        if doc_name != '0':
            converter_documento(doc_name)

main()
    
