from fasthtml.common import *

def render(pairing):
    pairing_number = P(f'Pairing {pairing.id}:')
    show_cheese = P(f'Cheese: {pairing.cheese} - {pairing.cheese_desc}')
    show_wine = P(f'Wine: {pairing.wine} - {pairing.wine_desc}')
    show_book = P(f'Book: {pairing.book} - {pairing.book_desc}')
    return Li(pairing_number, Ul(show_cheese, show_book, show_wine), id=f'pairing-{pairing.id}')
    

app,rt,cheesewine, Pairing = fast_app('data/cheesewine.db', render, id=int, cheese=str, wine=str, book=str, wine_desc=str, cheese_desc=str, book_desc=str, pk='id')

@rt("/")
def get():
    inp_cheese = Input(id="new-cheese", name="cheese", placeholder="New Cheese")
    cheese_description = Input(id="new-cheese-desc", name="cheese_desc", placeholder="Describe your cheese")
    
    inp_wine = Input(id="new-wine", name="wine", placeholder="New Wine")
    wine_description = Input(id="new-wine-desc", name="wine_desc", placeholder="Describe your wine")
    
    inp_book = Input(id="new-book", name="book", placeholder="New Book")
    book_description = Input(id="new-book-desc", name="book_desc", placeholder="Describe your book")
    
    add = Form(inp_cheese, cheese_description, inp_book, book_description, inp_wine, wine_description, Button("Add"), hx_post="/", target_id="pairings-list", hx_swap="beforeend")
    card = Card(Ul(*cheesewine(), id='pairings-list'), header=add, footer=Div(id="current-pairing"))
    return Titled('Pairings', card)

@rt("/")
def post(pairing:Pairing):
    return (
        cheesewine.insert(pairing), 
        Input(id="new-cheese", name="cheese", placeholder="New Cheese", hx_swap_oob='true'),
        Input(id="new-wine", name="wine", placeholder="New Wine", hx_swap_oob='true'),
        Input(id="new-book", name="book", placeholder="New Book", hx_swap_oob='true'),
        Input(id="new-cheese-desc", name="cheese_desc", placeholder="Describe your cheese", hx_swap_oob='true'),
        Input(id="new-wine-desc", name="wine_desc", placeholder="Describe your wine", hx_swap_oob='true'),
        Input(id="new-book-desc", name="book_desc", placeholder="Describe your book", hx_swap_oob='true')
    )
    




if __name__ == "__main__":
    serve()