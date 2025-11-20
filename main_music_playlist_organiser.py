import time # Used for a small delay to make the output clearer

# The main data structure to hold all playlists.
playlists = {}

def show_menu():
    """Displays the main menu options."""
    print("\n" + "="*40)
    print("      🎵 Music Playlist Organizer 🎵")
    print("="*40)
    print("1. Create New Playlist")
    print("2. View All Playlists")
    print("3. View Songs in a Playlist")
    print("4. Add Song to Playlist")
    print("5. Remove Song from Playlist")
    print("6. Delete Playlist")
    print("7. Exit")
    print("="*40)

def create_playlist():
    """Allows the user to create a new, empty playlist."""
    name = input("Enter the name for the new playlist: ").strip()
    if not name:
        print("Playlist name cannot be empty.")
        return
    if name in playlists:
        print(f"Error: Playlist '{name}' already exists.")
    else:
        playlists[name] = []
        print(f"✅ Playlist '{name}' created successfully!")

def view_all_playlists():
    """Displays all existing playlists."""
    if not playlists:
        print("\nNo playlists found. Create one first!")
        return

    print("\n--- All Playlists ---")
    for name in playlists:
        print(f"- {name} (Songs: {len(playlists[name])})")
    print("---------------------")

def get_playlist_name(prompt):
    """Helper function to get a playlist name from the user."""
    name = input(prompt).strip()
    if name not in playlists:
        print(f"Error: Playlist '{name}' not found.")
        return None
    return name

def view_songs_in_playlist():
    """Displays all songs in a specific playlist."""
    view_all_playlists()
    if not playlists:
        return

    name = get_playlist_name("Enter the name of the playlist to view songs: ")
    if name:
        songs = playlists[name]
        print(f"\n--- Songs in '{name}' (Total: {len(songs)}) ---")
        if not songs:
            print("This playlist is currently empty.")
        else:
            for i, song in enumerate(songs, 1):
                print(f"{i}. {song}")
        print("------------------------------------------")

def add_song_to_playlist():
    """Adds a song to an existing playlist."""
    view_all_playlists()
    if not playlists:
        return

    name = get_playlist_name("Enter the name of the playlist to add a song to: ")
    if name:
        song = input("Enter the title of the song to add: ").strip()
        if not song:
            print("Song title cannot be empty.")
            return

        if song in playlists[name]:
             print(f"Warning: Song '{song}' is already in '{name}'.")
        else:
             playlists[name].append(song)
             print(f"🎶 Song '{song}' added to '{name}'.")

def remove_song_from_playlist():
    """Removes a song from an existing playlist by title or number."""
    view_all_playlists()
    if not playlists:
        return

    name = get_playlist_name("Enter the name of the playlist to remove a song from: ")
    if name:
        songs = playlists[name]
        if not songs:
            print(f"The playlist '{name}' is empty. Nothing to remove.")
            return

        print(f"\n--- Songs in '{name}' ---")
        for i, song in enumerate(songs, 1):
            print(f"{i}. {song}")
        print("--------------------------")

        try:
            song_input = input("Enter the song title or its number (e.g., '1', 'My Song Title'): ").strip()
            
            # Try to interpret as a song number
            if song_input.isdigit():
                index = int(song_input) - 1
                if 0 <= index < len(songs):
                    removed_song = songs.pop(index)
                    print(f"🗑️ Song '{removed_song}' removed from '{name}' by number.")
                else:
                    print("Invalid song number.")
            # Interpret as a song title
            else:
                if song_input in songs:
                    songs.remove(song_input)
                    print(f"🗑️ Song '{song_input}' removed from '{name}' by title.")
                else:
                    print(f"Error: Song '{song_input}' not found in '{name}'.")

        except ValueError:
            print("Invalid input.")

def delete_playlist():
    """Deletes an entire playlist."""
    view_all_playlists()
    if not playlists:
        return

    name = get_playlist_name("Enter the name of the playlist to DELETE: ")
    if name:
        confirm = input(f"Are you sure you want to delete playlist '{name}'? (yes/no): ").lower()
        if confirm == 'yes':
            del playlists[name]
            print(f"💥 Playlist '{name}' has been deleted.")
        else:
            print("Playlist deletion cancelled.")


# --- Main Loop ---
def main():
    """The main function to run the interactive program."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            create_playlist()
        elif choice == '2':
            view_all_playlists()
        elif choice == '3':
            view_songs_in_playlist()
        elif choice == '4':
            add_song_to_playlist()
        elif choice == '5':
            remove_song_from_playlist()
        elif choice == '6':
            delete_playlist()
        elif choice == '7':
            print("\nExiting the Playlist Organizer. Goodbye! 👋")
            time.sleep(1)
            break
        else:
            print("🚫 Invalid choice. Please enter a number between 1 and 7.")

        time.sleep(1.5) # Pause briefly before showing the menu again

if __name__ == "__main__":
    main()