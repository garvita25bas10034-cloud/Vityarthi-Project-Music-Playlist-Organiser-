# Problem Statement
The goal of this project is to allow students to apply the subject concepts in a real-world context 
by: 
● Identifying a meaningful problem: The given problem was to create a music playlist organiser.
● Designing a technical solution: Using python I implemented concepts like defining a user function, using data types like dictionaries, lists. 
● Implementing the solution using the tools/methods learned in the course: Fromt the vityarthi module I implemented the basic cincepts of python.
● Demonstrating understanding through documentation and evaluation

# Scope of the Project
The project focues on taking user input to create or edit a pre-existing playlist or delete a pre-exisitng playlist.

# Target Users
The program can be used by anyone who doesn't even have information about Python programming language. The user just has to run the code and then input the values asked for. 
It would be preferrably used by people who want to organise their songs into different playlists.

# High Level Features
1.User Interface and Navigation
Menu-Driven Interaction: The program uses a **Command-Line Interface (CLI)** driven by a main numeric menu. This feature guides the user through all available actions (options 1 through 7).

Continuous Operation: It employs a `while True` loop in the `main` function, allowing the program to **continuously display the menu** and accept user input until the user explicitly chooses to exit.

2.Playlist Management
Creation: Allows the user to create new, named playlists. The program ensures that playlist names are not duplicated.

Deletion: Provides a way to completely remove an existing playlist, including a **confirmation step** to prevent accidental data loss.

Viewing All: Quickly displays a list of all currently stored playlists and the number of songs in each.

3.Song Management
Addition: Enables the user to add a new song title to a specified existing playlist.

Removal: Allows songs to be removed from a playlist. This feature is more robust, supporting removal by both the **song's title** or its **numbered position** in the list.

Viewing Content: Displays the songs contained within a single, specified playlist in a numbered list format.

4.Data Structure and Storage
In-Memory Storage: The program uses a single, global **Python dictionary (`playlists`)** as its data store. This means all data (playlists and songs) is held in the computer's memory and is **not saved permanently** to a file (i.e., the data is lost when the program is closed).

Simple Data Model: It uses the playlist name (string) as the **key** and a Python list of song titles (strings) as the corresponding **value**, providing a clear and efficient structure for lookup. 