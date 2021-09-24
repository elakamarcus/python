import math
import tkinter as tk

SIZE = 600

top = (200,50)
botleft = (50,200)
botright = (200,200)

def calc_magnitude(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    

def triangle_area(p1, p2, p3):
    a = calc_magnitude(p1, p2)
    b = calc_magnitude(p1, p3)
    c = calc_magnitude(p2, p3)
    s = (1/2) * (a + b + c)

    return math.sqrt(s * (s-a) * (s-b) * (s-c))

def rektangel(img):
    for y in range(SIZE // 2):
        for x in range(SIZE):
            img.put("blue", (x,y))

def triangle(top, botleft, botright, img):
    for y in range(top[1], botright[1]):
        for x in range(botleft[0], botright[0]):
            area = triangle_area((top, botright), (top, botleft), (botleft, botright))
            if triangle_area((x,y), top, botleft) + triangle_area((x,y), botleft, botright) + triangle_area((x,y),botright, top) < area:
                img.put("#ffffff", (x,y))
    

def main():
    window = tk.Tk()
    canvas = tk.Canvas(window, width=SIZE, height=SIZE, bg="#000000")
    canvas.pack()
    img = tk.PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE/2, SIZE/2), image=img, state="norma")
    #rektangel(img)
    #triangle((200,50),(50,200),(400,200),img)
    triangle(top, botleft, botright, img)
    window.mainloop()

if __name__ == "__main__":
    main()
