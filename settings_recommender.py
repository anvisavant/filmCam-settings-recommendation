from exposureData import film_exposure_data

def autocomplete(user_input):
    """
    Returns a list of film types that start with the given user input.
    """
    return [film for film in film_exposure_data.keys() if film.lower().startswith(user_input.lower())]

def display_film_data(selected_film):
    """
    Displays all the data related to the selected film type.
    """
    if selected_film in film_exposure_data:
        data = film_exposure_data[selected_film]
        print(f"\nFilm Type: {selected_film}")
        print("Lighting Conditions:", ', '.join(data['lighting_conditions']))
        print("\nRecommended Settings:")
        for i, setting in enumerate(data['recommended_settings'], 1):
            print(f"  Setting {i}:")
            print(f"    Lighting: {data['lighting_conditions'][i-1]}")
            print(f"    Shutter Speed: {setting['shutter_speed']}")
            print(f"    Aperture: {setting['aperture']}")
            print(f"    ISO: {setting['ISO']}")
        print("\nDescription:", data['description'])
    else:
        print("Film type not found.")

def main():
    print("Hi!! Welcome to the Film Photography Exposure Recommender!")
    
    while True:
        user_input = input("\nEnter the beginning of a film type (or 'quit' to exit): ").strip()
        
        if user_input.lower() == 'quit':
            print("Thank you for using the Film Photography Exposure Recommender!")
            break
        
        suggestions = autocomplete(user_input)
        
        if not suggestions:
            print("No matching film types found.")
        else:
            print("\nSuggested film types:")
            for i, film in enumerate(suggestions, 1):
                print(f"{i}. {film}")
            
            choice = input("\nEnter the number of your chosen film type (or press Enter to search again): ").strip()
            
            if choice.isdigit() and 1 <= int(choice) <= len(suggestions):
                selected_film = suggestions[int(choice) - 1]
                display_film_data(selected_film)
            elif choice == "":
                continue
            else:
                print("Hmm, I dont seem to have data on that. Please try again.")

if __name__ == "__main__":
    main()
