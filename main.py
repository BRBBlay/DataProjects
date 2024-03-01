from ai_agents import initialize_agent_zero_shot
from uu_tools import tool_start_playing_song_by_lyrics, tool_start_playing_song_by_name


# Initialize agent
tools = [tool_start_playing_song_by_lyrics,tool_start_playing_song_by_name]
agent = initialize_agent_zero_shot(
    tools=tools)


print("\nHi, Can I play something for you?")

while True:
    request = input(
        "\n\nRequest: ")
    result = agent({"input": request})
    answer = result["output"]
    print(answer)