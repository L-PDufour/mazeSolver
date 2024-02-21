import tkinter as tk

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, Point1, Point2):
        self.Point1 = Point1
        self.Point2 = Point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.Point1.x, self.Point1.y, self.Point2.x, self.Point2.y, fill=fill_color, width=2)

class CustomWindow:
    def __init__(self, width, height, title="Custom Window"):
        self.root = tk.Tk()
        self.root.title(title)

        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.running = False

        # Bind the close method to the "delete window" action
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        # Redraw the window
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

# Example usage:
width, height = 400, 300
custom_window = CustomWindow(width, height)
custom_window.draw_line(Line(Point(10, 10), Point(100, 100)), "red")
custom_window.wait_for_close()

