"""Class to store a message (operator overload, union types, default parameters.)"""

class Message:

    to: str | int
    content: str
    important: bool

    def __init__(self, recipient: str | int, message_content: str = "", importance_flag: bool = False):
        """Construct a message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f'"{self.content}"'
        return output
    

    def __mul__(self, factor: int):
        """Multiplication operator overload"""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + copy_val


msg_to_myslef: Message = Message("me", "Great job!", True)
print(msg_to_myslef)
msg_to_sam: Message = Message(1, "You are awesome!")
print(msg_to_sam)
