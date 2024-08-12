"""Here's a simple script using the examples above to create a command-line Wikipedia search tool:"""
import wikipedia

from wikipedia.exceptions import DisambiguationError, PageError

def search_wikipedia(term):
    """Search Wikipedia and return a summary."""
    try:
        summary = wikipedia.summary(term)
        print(f"Summary for {term}:")
        print(summary)
    except DisambiguationError as e:
        print("DisambiguationError: The term is ambiguous. Here are some options:")
        for option in e.options:
            print(option)
    except PageError as e:
        print(f"PageError: {e}")
    except wikipedia.exceptions.HTTPTimeoutError:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the Wikipedia search tool."""
    print("Welcome to the Wikipedia search tool!")
    while True:
        search_term = input("Enter a search term (or 'quit' to exit): ")
        if search_term.lower() == 'quit':
            break
        search_wikipedia(search_term)

if __name__ == "__main__":
    main()


"""to install wikipedia"""
pip install wikipedia-api

"""add this code then to wiki.py"""
import wikipedia


def get_wikipedia_page():
    while True:
        # Prompt the user for a page title or search phrase
        search_term = input("Enter a page title or search phrase (or leave blank to exit): ").strip()
        if not search_term:
            break

        try:
            # Search for the page using the search term
            page = wikipedia.page(search_term, autosuggest=True)
            # Print the title, summary, and URL of the page
            print("\nTitle:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)
        except wikipedia.DisambiguationError as e:
            print("There are multiple options for that search term. Please be more specific.")
            print("Options include:", e.options)
        except wikipedia.PageError:
            print("The page could not be found. Please try another search term.")
        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    get_wikipedia_page()
