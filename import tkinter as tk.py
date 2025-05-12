import tkinter as tk
import random

class BouncingBallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sekip Rengi Değişen Top")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="blue")
        self.dx = 3
        self.dy = 3

        self.update_ball()

    def update_ball(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        pos = self.canvas.coords(self.ball)

        if pos[0] <= 0 or pos[2] >= 600:
            self.dx = -self.dx
            self.change_color()
        if pos[1] <= 0 or pos[3] >= 400:
            self.dy = -self.dy
            self.change_color()

        self.root.after(20, self.update_ball)

    def change_color(self):
        colors = ["red", "green", "blue", "yellow", "purple", "orange"]
        new_color = random.choice(colors)
        self.canvas.itemconfig(self.ball, fill=new_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = BouncingBallApp(root)
    root.mainloop()
