# CS361-Sprint2
## Song Guesser Microservice for Jonah Sutch's project

This Microservice provides an interactive guessing game that challenges the user to guess missing metadata about a randomly chosen song.

## Communication Contract
Communication Pipe
This Microservice uses ZeroMQ with the REQ/REP socket pattern
Default Port: tcp://localhost:5555

## How to request data from the microservice
Request format
Send a simple string to the Microservice:
to start the game and receive a song prompt:

            "start" or "song_guesser start"
to send a guess (replace your_guess_here):

            Guess: your_guess_here
			
**note the microservice will take "_" over " " for user inputs


Example Code (Requester):
        
        import zmq
        
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555)

        # Start game
        socket.send_string("start")
        response = socket.recv_json()
        print(response["question"])

        # Send guess
        socket.send_string("guess:adele")
        result = socket.recv_string()
        print("Correct!" if result == "true" else "Incorrect!")

## How to receive data from the microservice
Response format
When sending "start":
            
            {
                "question": "Guess the genre!\nSong: hello \nArtist: adele \nGenre: ??? \nMood: emotional",
                "missing": "genre",
                "answer": "soul"
            }
        
When sending a guess:

            "true" or "false"

## Sample songs data  
    
    hello adele soul emotional
    thunder imagine_dragons rock energetic
    stay rhianna pop emotional

## UML Sequence Diagram:
<img width="929" height="856" alt="image" src="https://github.com/user-attachments/assets/4b08c241-502e-4556-838b-4a7f0179ad53" />
