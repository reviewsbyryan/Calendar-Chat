import tkinter as tk
import chat
import speech_tool

def hear_message():
    print("You clicked the hear button!")

    message = speech_tool.recognize_speech()
    response = chat.chat(message)

    text_display.config(state=tk.NORMAL)

    text_display.insert(tk.END,"\nYou: ")
    text_display.insert(tk.END,message)

    text_display.insert(tk.END,"\nAI: ")
    text_display.insert(tk.END,response)

    text_display.config(state=tk.DISABLED)

def send_message():
    print("You clicked the send button!")

    message = entry.get()
    response = chat.chat(message)

    text_display.config(state=tk.NORMAL)

    text_display.insert(tk.END,"\nYou: ")
    text_display.insert(tk.END,message)

    text_display.insert(tk.END,"\nAI: ")
    text_display.insert(tk.END, response, "message")
    
    text_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Chat Window")

# Create a text display area with vertical scrollbar
text_display = tk.Text(root, wrap=tk.WORD)
text_display.pack(fill=tk.BOTH, expand=True)

# Create an input field and send button
entry = tk.Entry(root)
entry.pack(fill=tk.BOTH, expand=True)

# Create a button to hear the message
hear_button = tk.Button(root, text="Hear", command=hear_message)
hear_button.pack(fill=tk.BOTH, expand=True)


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(fill=tk.BOTH, expand=True)

root.mainloop()