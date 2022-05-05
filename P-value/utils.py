from IPython.display import display, HTML


def to_single_space(x: str) -> str:
    """converts multiple spaces to single space"""
    return ' '.join(x.split())


def to_cols(x: str) -> str:
    """converts a string seperated by spaces to a html table column"""
    return "".join(
    [f'<td>{wrd}</td>' for wrd in str(x).split(' ')])


def to_rows(x: str) -> str:
    """converts a string seperated by lines to a html table row"""
    return "".join(
    [f'<tr>{to_cols(to_single_space(wrd))}</tr>' for wrd in str(x).split('\n')])


def display_in_grid(data: list[str], no_of_cols: int=2) -> None:
    """
    displays data in a grid format 
    @param data: str -> list of strings of single html objects
    @param no_of_cols:int -> number of columns
    """

    for i in range(0, len(data), no_of_cols):
        display(HTML(f'''
        <table>
            {"".join([
                to_cols(row) for row in data[i:i+no_of_cols]
            ])}
        </table>'''))
