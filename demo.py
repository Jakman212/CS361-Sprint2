import time
import subprocess
import zmq

SONG_FILE = "songs.txt"

# Sample song data
sample_songs = [
    "numb linkin_park alternative dark",
    "halo beyonce pop uplifting",
    "thunder imagine_dragons rock energetic",
    "rolling_in_the_deep adele soul emotional"
]

# Write sample songs to file
def write_sample_songs():
    with open(SONG_FILE, "w") as f:
        for song in sample_songs:
            f.write(song + "\n")

# Start microservice subprocess
def start_microservice():
    print("Starting Song Guesser Microservice...")
    return subprocess.Popen(["python", "song_guesser.py"])

# Main test client
def run_test():
    print("=== Song Guesser Test ===")

    while True:
        command = input("Type 'song_guesser start' to begin, or 'exit' to quit: ").strip().lower()

        if command == "exit":
            print("Exiting.")
            return

        elif command == "song_guesser start":
            # Write songs and start microservice
            write_sample_songs()
            process = start_microservice()
            time.sleep(1.5)

            # Connect to ZeroMQ
            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://localhost:5555")

            # Request game round
            socket.send_string("start")
            response = socket.recv_json()

            print(f"\n{response['question']}")

            # Loop for guesses
            while True:
                user_guess = input("Your guess: ")
                socket.send_string(f"guess:{user_guess}")
                result = socket.recv_string()

                if result.lower() == "true":
                    print("✅ Correct guess!")
                    break
                else:
                    print("❌ Try again.")

            process.terminate()
            break

        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    run_test()
