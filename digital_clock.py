# Code được viết bởi Trần Đức Hiếu, có sự hỗ trợ từ ChatGPT và 1 vài kênh YTB
# Thankiu 

from tkinter import *
from tkinter.ttk import *
from time import strftime

# tính cho các bé yêu sửa ở bên dưới mà sợ sửa sai nên cho lên đây mà setting
setting = {
    'background':'black',
    'color':'red'
}

root = Tk()
root.title("Clock Digital")
root.attributes('-topmost', False) # thay đổi True, False để bật tắt chế độ on top

sample_text = '22:22:22 PM' # cái này là trường hợp mà chiếm độ rộng lớn nhất đó 
estimated_width = len(sample_text) * (100 * 0.5)  # 0.5 là tỷ lệ ước lượng (Hiếu bảo rồi cứ tùy máy thôi)

# Thiết lập kích thước cửa sổ
root.geometry(f"{int(estimated_width)}x140")  # Chiều rộng được ước lượng, chiều cao là 140 pixel tùy thuộc và sở thích =)))
root.configure(background=setting['background'])
def clock():
    time = strftime('%H:%M:%S:%p')
    label.config(text=time)
    label.after(1000, clock)

label = Label(root, font=("Digital-7", 100), background=setting['background'], foreground=setting['color'])
label.pack(anchor='center')

clock()

root.mainloop()
