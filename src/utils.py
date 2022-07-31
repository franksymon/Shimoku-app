from shimoku_components_catalog.html_components import create_h1_title

from app import shimoku
from class_File import OpenFile, ProccesFile

ROOT_DATA = "data/supermarket_sales - Sheet1.csv"
df = OpenFile.open_file_csv(ROOT_DATA)
df_store = ProccesFile.df_store(df)


def create_title(
    title: str,
    sub_title: str,
    menu_path: str,
    order: int,
    rows_size: int = 2,
    cols_size: int = 12,
):
    text_h1_title = create_h1_title(title=f"{title} ", subtitle=f"{sub_title}")
    shimoku.plt.html(
        text_h1_title,
        menu_path=f"{menu_path}",
        order=f"{order}",
        rows_size=f"{rows_size}",
        cols_size=f"{cols_size}",
    )


def deleted_path(menu_path: str):
    shimoku.plt.delete_path(menu_path=f"{menu_path}")
