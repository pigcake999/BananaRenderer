from PIL import Image
import sys
import tkinter
im = Image.open(sys.argv[1]) #Can be many different formats.
pix = im.load()
if __name__ == "__main__":
	string = ""
	x,y = 0,0

	while y<360:
		x = 0
		while x<480:
			rgb = str(pix[x,y][0])+","+str(pix[x,y][1])+","+str(pix[x,y][2])
			string += ","+rgb
			x += 1

		y += 1
	string = string[1:]
	alert = tkinter.Tk()
	alertText = tkinter.Text()
	alertText.delete(0.0, tkinter.END)
	alertText.insert(0.0, string, tkinter.END)
	alertText.config(font=("sans-serif", 16))
	alertText.pack(side=tkinter.LEFT)
	alert.title("Banana Renderer 1.0.0 Image Code")
	alert.mainloop()