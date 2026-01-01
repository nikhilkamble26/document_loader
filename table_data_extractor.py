import pdfplumber
import pandas as pd

pdf_path = "hdfc_doc.pdf"

# with pdfplumber.open(pdf_path) as pdf:
#     print("Total pages:", len(pdf.pages))
#     page = pdf.pages[6]

#     text = page.extract_text()
#     print(text)


with pdfplumber.open(pdf_path) as pdf:
    print("Total pages:", len(pdf.pages))
    page = pdf.pages[6]

    tables = page.extract_tables()
    print(len(tables))

    table_settings = {
    "vertical_strategy": "lines",
    "horizontal_strategy": "lines"
    }

    tables = page.extract_tables(table_settings)
    print(tables)


all_tables = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            df = pd.DataFrame(table[1:], columns=table[0])
            all_tables.append(df)

final_df = pd.concat(all_tables, ignore_index=True)
