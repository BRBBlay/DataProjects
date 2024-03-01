from langchain.agents import Tool
from spotify import start_playing_song_by_lyrics,start_playing_song_by_name

def tool_start_playing_song_by_name():
    return Tool(name="Play a song given the name", func=lambda song_name: start_playing_song_by_name(song_name), description="Given a song name, start playing a song. Action Input is a string of song_name", return_direct= True)

def tool_start_playing_song_by_lyrics():
    return Tool(name="Play a song given the lyrics", func= lambda lyrics: start_playing_song_by_lyrics(lyrics), description="Given lyrics, start playing a song. Action Input is a string of lyrics", return_direct= True)

