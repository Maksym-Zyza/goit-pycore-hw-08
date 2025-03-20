from typing import Callable, List, Tuple, Any
from address_book import AddressBook
import pickle


def input_error(func: Callable[..., Any]) -> Callable[..., Any]:
    def inner(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return inner


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    if not user_input.strip():
        return "", []
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    args = [arg.strip() for arg in args]
    return cmd, args


def save_data(book: AddressBook, filename: str = "address_book.pkl") -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename: str = "address_book.pkl") -> AddressBook:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)  
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        return AddressBook()
