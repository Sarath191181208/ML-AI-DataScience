"""
  These are just some utility functions for main.ipynb
"""

import pandas as pd
from IPython.display import display, HTML

ALIGN_LEFT = "style='text-align:left;'"

def opacity_line(opacity: float=0.3)->str:
    """returns a line with opacity"""
    return f"<hr style='opacity: {opacity};'>"

def display_shape(shape: tuple[int, int])->None:
    """displays the shape of a dataframe"""
    rows_shape, cols_shape = shape
    display(HTML(f'''
      <h3>Rows: {rows_shape}, Columns: {cols_shape}</h3>
    '''))

    del rows_shape, cols_shape

def to_table(frame: pd.Series, headers: tuple[str]=None)->str:
    """converts pd.Series to html table"""

    def get_cols(i: list[str])->str:
        arr = i
        arr = [i for i in arr if i not in ["", "\t", "\n"]]
        arr = [f"<td>{i}</td>" for i in arr]
        return "".join(arr)

    x_shape = len(frame)
    frame = frame.head()
    # splitting every new line
    frame = str(frame).split("\n")

    # The last element is the info of the series
    info = frame[-1]
    info += f"<p {ALIGN_LEFT} >Number of Features: <b>{x_shape}</b></p>"
    # converting to html table
    table = [f"<tr>{get_cols(i.split())}</tr>" for i in frame[:-1]]

    # filling the table with empty things
    if (t_len:=len(table)%5) != 0:
        table = table + [f"<tr>{get_cols(['-', '-'])}</tr>"]*(5-t_len)


    # joining into a single table
    table = "".join(table)

    # adding headers
    if headers:
        headers = [f"<td>{i}</td>" for i in headers]
        headers = "".join(headers)
        table = f"<thead>{headers}</thead>{table}"

    # converting to a table
    table = f"<table>{table}</table>"
    # adding info
    table += opacity_line(0.3)
    table += info

    return table

def display_cols(cols: pd.Series, no_cols=5)->None:
    """displays the columns of a dataframe"""

    def _get_cols(i: list[str])->str:
        """converts a list of strings to html table"""
        return "".join([f"<td>{ele}</td>" for ele in i])
    cols = list(cols)
    # filling the non existant columns with empty strings
    if (cols_len:=len(cols)%no_cols) != 0:
        cols = cols + [" "]*(no_cols-cols_len)

    # splitting the columns into groups of 5
    sub_lst = [cols[n:n+no_cols] for n in range(0, len(cols), no_cols)]

    # converting to html table
    table = [f'<tr>  {_get_cols(i)} </tr>' for i in sub_lst]
    table = f"<table>{''.join(table)}</table>"

    display(HTML("<h3>Columns</h3>" + table + "<hr>"))
    del sub_lst, table, _get_cols

def analyze_cols(data: pd.DataFrame, show_feature_info:bool = True, **kwargs)->None:
    """displays the columns & their info of a dataframe
    @params data: pd.DataFrame
    @kwargs:
        no_cols: number of columns to display
        features_no_cols: number of features to display per column in Columns
    """
    def _get_info(label):
        val_cnts = data[label].value_counts()
        return to_table(val_cnts, headers=("Features", "Count"))

    def _display_table(tabels: list[str], labels: list[str]):
        labels = [f'<h3 {ALIGN_LEFT}">{label}</h3>'
          for label in labels]

        # grouping the tables and respective labels together
        cols = [*zip(labels, tabels)]

        # converting to html table
        cols = [f'<div style="margin:10px;" >{label+table}</div>'
          for label, table in cols]

        # if this div isn't supported we can use the tables
        # display(HTML(f'''
        #     <table>
        #       <tr" >
        #         {''.join(cols)}
        #       </tr>
        #     </table>
        # '''))

        display(HTML(f'''
          <div style="display:flex;" >
            {''.join(cols)}
          </div>
        '''))


    cols = data.columns

    display_shape(data.shape)
    display_cols(cols, no_cols=kwargs.get("features_no_cols", 5))

    # Dispalying the info of null values in each column
    display(HTML("<h3> Null Values </h3>"))
    display(data.isna().sum())
    display(HTML("<hr>"))

    # Displaying the some of the data
    display(HTML("<h3> Data </h3>"))
    display(data.head())
    display(HTML("<hr>"))

    # only show features if this is specified
    if not show_feature_info:
        return

    # for every n columns
    # this is just done like this
    # to make them display as grid
    step = kwargs.get("no_cols", 2)
    for i in range(0, len(cols), step):
        labels = cols[i:i+step]
        tables = [_get_info(i) for i in labels]

        _display_table(tables,labels)

    del cols, i, _get_info, _display_table
    del labels, tables, step
