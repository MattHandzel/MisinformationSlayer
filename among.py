import os
import sys


class DuplicateOutput(object):
    def __init__(self, *streams):
        self.streams = streams

    def write(self, message):
        for stream in self.streams:
            stream.write(message)
            stream.flush()  # Ensure message is immediately written to the stream

    def flush(self):
        for stream in self.streams:
            stream.flush()


# Example usage
if __name__ == "__main__":
    # Open a file for writing
    file = open("output.txt", "a")

    # Save the original stdout so we can restore it later
    original_stdout = sys.stdout

    # Redirect stdout to our custom class that writes to both console and file
    sys.stdout = DuplicateOutput(sys.stdout, file)

    # Now, every print statement will go to both the console and the file
    print("This message will be printed to the console and saved to 'output.txt'")

    # Restore the original stdout when done
    sys.stdout = original_stdout
    try:
        os.system("chatgpt > output_iii11.txt")
    except Exception as e:
        pass

    # Close the file
    file.close()
