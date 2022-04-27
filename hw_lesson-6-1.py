# Task 6-1

# import time
from tkinter import Tk, Canvas, BOTH, TOP, Label, Button


class TrafficLight(Tk):
    __RED_COLOR = 'red'
    __YELLOW_COLOR = 'yellow'
    __GREEN_COLOR = 'green'
    __NO_LIGHT_COLOR = 'gray'

    def __init__(self):
        self.__color = 'red'
        self.__is_running = False  # Else Paused
        super().__init__()

        # In seconds
        self.red_time = 7
        self.yellow_time = 2
        self.green_time = 5
        self.__cur_time = 0

        # self.pack(fill=BOTH, expand=1)
        # Style().configure("Frame", background="#333")
        # Style().configure("TButton", font='serif 20')

        self.title("Application Traffic Lights")
        self.canvas = Canvas(self)
        self.start_button = Button(self, text="Start", font=('Courier', 20), command=self.on_btn_start)
        self.start_button.pack(side=TOP, padx=20, pady=10)
        self.lbl = Label(text="0", font=("Courier", 30), width=10)
        self.lbl.pack(padx=5, pady=5)

        # Овальная форма или круг.
        self.red_light = self.canvas.create_oval(120, 20, 200, 100, outline="black", fill="grey", width=4)
        self.yellow_light = self.canvas.create_oval(120, 120, 200, 200, outline="black", fill="grey", width=4)
        self.green_light = self.canvas.create_oval(120, 220, 200, 300, outline="black", fill="grey", width=4)

        self.canvas.pack(fill=BOTH, expand=1)
        self.update()

    def on_btn_start(self):
        if not self.__is_running:
            self.__is_running = True
            self.start_button.configure(text='Pause')
            self.running()
        else:
            self.start_button.configure(text='Start')
            self.__is_running = False

    def running(self):
        if not self.__is_running:
            return
        if self.__cur_time > 1:
            self.__cur_time -= 1
            self.lbl.configure(text=str(self.__cur_time))
            self.after(1000, self.running)
        else:
            if self.__color == 'red':
                self.__color = 'yellow'
                self.canvas.itemconfigure(self.green_light, fill='grey')
                self.canvas.itemconfigure(self.red_light, fill='red')
                self.__cur_time = self.red_time
                self.lbl.configure(text=str(self.__cur_time))
                self.after(1000, self.running)
            elif self.__color == 'yellow':
                self.__color = 'green'
                self.canvas.itemconfigure(self.red_light, fill='grey')
                self.canvas.itemconfigure(self.yellow_light, fill='yellow')
                self.__cur_time = self.yellow_time
                self.lbl.configure(text=str(self.__cur_time))
                self.after(1000, self.running)
            elif self.__color == 'green':
                self.__color = 'red'
                self.canvas.itemconfigure(self.yellow_light, fill='grey')
                self.canvas.itemconfigure(self.green_light, fill='green')
                self.__cur_time = self.green_time
                self.lbl.configure(text=str(self.__cur_time))
                self.after(1000, self.running)


def main():
    window = TrafficLight()
    window.geometry('320x500')
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    main()
