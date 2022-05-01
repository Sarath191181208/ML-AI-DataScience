import pandas as pd
from IPython.display import display, HTML

align_left = "style='text-align:left;'"

def opacity_line(opacity: float=0.3)->str:
  """returns a line with opacity"""
  return f"<hr style='opacity: {opacity};'>"

def to_table(x: pd.Series, headers: tuple[str]=None)->str:
  """converts pd.Series to html table"""

  def get_cols(i: list[str])->str:
    arr = i
    arr = [i for i in arr if i not in ["", "\t", "\n"]]
    arr = [f"<td>{i}</td>" for i in arr]
    return "".join(arr)
  
  x_shape = len(x)
  x = x.head()
  # splitting every new line
  x = str(x).split("\n")

  # The last element is the info of the series
  info = x[-1]
  info += f"<p {align_left} >Number of Features: <b>{x_shape}</b></p>"
  # converting to html table
  table = [f"<tr>{get_cols(i.split())}</tr>" for i in x[:-1]]
  
  # filling the table with empty things
  if (a:=len(table)%5) != 0:
    table = table + [f"<tr>{get_cols(['-', '-'])}</tr>"]*(5-a)


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

  # filling the non existant columns with empty strings
  if (a:=len(cols)%no_cols) != 0:
    cols = cols + [" "]*(no_cols-a)
  
  # splitting the columns into groups of 5
  subList = [cols[n:n+no_cols] for n in range(0, len(cols), no_cols)]
  
  # converting to html table
  table = [f'<tr>  {_get_cols(i)} </tr>' for i in subList]
  table = f"<table>{''.join(table)}</table>"

  display(HTML("<h3>Columns</h3>" + table + "<hr>"))
  del subList, table, _get_cols

def analyze_cols(data: pd.DataFrame, **kwargs)->None:
  """displays the columns & their info of a dataframe"""
  def _get_info(label):
      x = data[label].value_counts()
      return to_table(x, headers=("Features", "Count"))

  def _display_table(tabels: list[str], labels: list[str]):
    labels = [f'<h3 {align_left}">{label}</h3>' 
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
  display_cols(cols, no_cols=kwargs.get("features_no_cols", 5))

  display(HTML("<h3> Data </h3>"))
  display(data.head())
  display(HTML("<hr>"))

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