import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk

root = tk.Tk()

label = tk.Label(text="Number of Integer(N)", bg="light blue")
label.pack(fill=tk.X)
e = tk.Entry()
e.pack(fill=tk.X)
label2 = tk.Label(text="(i)nsertion/(q)uick", bg="red")
label2.pack(fill=tk.X)
e2 = tk.Entry()
e2.pack(fill=tk.X)

canvas1 = tk.Canvas(root, width=100, height=100)
canvas1.pack()


# NOTE: Dibutuhkan Python versi 3.3 dan keatas.

def swap(A, i, j):
    """Function yang membantu swap variabel i dan j"""

    if i != j:
        A[i], A[j] = A[j], A[i]

def insertionsort(A):
    """insertion sort."""

    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            j -= 1
            yield A

def quicksort(A, start, end):
    """quick sort."""

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)


def sort():
    if __name__ == "__main__":
        N = e.get()
        N = int(N)
        method = e2.get()

        A = [x + 1 for x in range(N)]
        random.seed(time.time())
        random.shuffle(A)

        if method == "i":
            title = "Insertion sort"
            generator = insertionsort(A)
        else:
            title = "Quicksort"
            generator = quicksort(A, 0, N - 1)

        fig, ax = plt.subplots()
        ax.set_title(title)

        bar_rects = ax.bar(range(len(A)), A, align="edge")

        ax.set_xlim(0, N)
        ax.set_ylim(0, int(1.07 * N))

        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

        iteration = [0]


        def update_fig(A, rects, iteration):
            for rect, val in zip(rects, A):
                rect.set_height(val)
            iteration[0] += 1
            text.set_text("# of operations: {}".format(iteration[0]))


        anim = animation.FuncAnimation(fig, func=update_fig,
                                       fargs=(bar_rects, iteration), frames=generator, interval=1,
                                       repeat=False)
        plt.show()

button1 = tk.Button(text='Click Me', command=sort, bg='brown', fg='white')
canvas1.create_window(50, 50, window=button1)

root.mainloop()