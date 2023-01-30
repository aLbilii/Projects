import tkinter  as Tk 
from tkinter import *

def delete_determinant_result():
    result_determinant.destroy()
    screen_matrixa.destroy()

def result_determinant():
    global result_determinant

    result_determinant= Tk()
    result_determinant.title("Result")

    a=int(a11_enter.get())
    b=int(a12_enter.get())
    c=int(a13_enter.get())
    d=int(a21_enter.get())
    e=int(a22_enter.get())
    f=int(a23_enter.get())
    g=int(a31_enter.get())
    h=int(a32_enter.get())
    i=int(a33_enter.get())

    t11=Label(result_determinant, text = "RESULT")
    t11.grid(row=0,column=0,padx=15, pady=5)

    t11=Label(result_determinant, text = "Determinant")
    t11.grid(row=1,column=0,padx=15, pady=5)

    m12=a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    t12=Label(result_determinant, text = m12)
    t12.grid(row=1,column=1,padx=15, pady=5)

    exit_determinant=Button(result_determinant, text = "OK", command = delete_determinant_result)
    exit_determinant.grid(row = 4, column = 1)

def matrix_determinant():
    global screen_matrixa
    screen_matrixa= Tk()
    screen_matrixa.title("Matrix A")

    global a11_enter
    global a12_enter
    global a13_enter
    global a21_enter
    global a22_enter
    global a23_enter
    global a31_enter
    global a32_enter
    global a33_enter

    a11_enter=Entry(screen_matrixa)
    a12_enter=Entry(screen_matrixa)
    a13_enter=Entry(screen_matrixa)
    a21_enter=Entry(screen_matrixa)
    a22_enter=Entry(screen_matrixa)
    a23_enter=Entry(screen_matrixa)
    a31_enter=Entry(screen_matrixa)
    a32_enter=Entry(screen_matrixa)
    a33_enter=Entry(screen_matrixa)

    a11_enter.grid(row = 0, column = 0, padx=2, pady= 2)
    a12_enter.grid(row = 0, column = 1, padx=2, pady= 2)
    a13_enter.grid(row = 0, column = 2, padx=2, pady= 2)
    a21_enter.grid(row = 1, column = 0, padx=2, pady= 2)
    a22_enter.grid(row = 1, column = 1, padx=2, pady= 2)
    a23_enter.grid(row = 1, column = 2, padx=2, pady= 2)
    a31_enter.grid(row = 2, column = 0, padx=2, pady= 2)
    a32_enter.grid(row = 2, column = 1, padx=2, pady= 2)
    a33_enter.grid(row = 2, column = 2, padx=2, pady= 2)

    exit_determinant=Button(screen_matrixa, text = "OK", command = result_determinant)
    exit_determinant.grid(row = 4, column = 1)

def delete_multi_result():
    result_multi.destroy()
    screen_matrixa.destroy()
    screen_matrixb.destroy()

def result_multi():
    global result_multi

    result_multi= Tk()
    result_multi.title("Result")

    a11=int(a11_enter.get())
    a12=int(a12_enter.get())
    a13=int(a13_enter.get())
    a21=int(a21_enter.get())
    a22=int(a22_enter.get())
    a23=int(a23_enter.get())
    a31=int(a31_enter.get())
    a32=int(a32_enter.get())
    a33=int(a33_enter.get())

    b11=int(b11_enter.get())
    b12=int(b12_enter.get())
    b13=int(b13_enter.get())
    b21=int(b21_enter.get())
    b22=int(b22_enter.get())
    b23=int(b23_enter.get())
    b31=int(b31_enter.get())
    b32=int(b32_enter.get())
    b33=int(b33_enter.get())

    m11=a11*b11 + a12*b21 + a13*b31
    t11=Label(result_multi, text = m11)
    t11.grid(row=0,column=0,padx=15, pady=5)

    m12=a11*b12 + a21*b22 + a13*b32
    t12=Label(result_multi, text = m12)
    t12.grid(row=0,column=1,padx=15, pady=5)

    m13=a11*b13 + a12*b23 + a13*b33
    t13=Label(result_multi, text = m13)
    t13.grid(row=0,column=2,padx=15, pady=5)

    m21=a21*b11 + a22*b21 + a23*b31
    t11=Label(result_multi, text = m21)
    t11.grid(row=1,column=0,padx=15, pady=5)

    m22=a21*b12 + a22*b22 + a23*b32
    t22=Label(result_multi, text = m22)
    t22.grid(row=1,column=1,padx=15, pady=5)
    
    m23=a21*b13 + a22*b23 + a23*b33
    t23=Label(result_multi, text = m23)
    t23.grid(row=1,column=2,padx=15, pady=5)
    
    m31=a31*b11 + a32*b21 + a33*b31
    t31=Label(result_multi, text = m31)
    t31.grid(row=2,column=0,padx=15, pady=5)
    
    m32=a31*b12 + a32*b22 + a33*b32
    t32=Label(result_multi, text = m32)
    t32.grid(row=2,column=1,padx=15, pady=5)
    
    m33=a31*b13 + a32*b23 + a33*b33
    t33=Label(result_multi, text = m33)
    t33.grid(row=2,column=2,padx=15, pady=5)

    exit_multi=Button(result_multi, text = "OK", command = delete_multi_result)
    exit_multi.grid(row = 4, column = 1)

def matrix_bmulti():
    global screen_matrixb
    screen_matrixb= Tk()
    screen_matrixb.title("Matrix B")

    global b11_enter
    global b12_enter
    global b13_enter
    global b21_enter
    global b22_enter
    global b23_enter
    global b31_enter
    global b32_enter
    global b33_enter

    b11_enter=Entry(screen_matrixb)
    b12_enter=Entry(screen_matrixb)
    b13_enter=Entry(screen_matrixb)
    b21_enter=Entry(screen_matrixb)
    b22_enter=Entry(screen_matrixb)
    b23_enter=Entry(screen_matrixb)
    b31_enter=Entry(screen_matrixb)
    b32_enter=Entry(screen_matrixb)
    b33_enter=Entry(screen_matrixb)

    b11_enter.grid(row = 0, column = 0, padx=2, pady= 2)
    b12_enter.grid(row = 0, column = 1, padx=2, pady= 2)
    b13_enter.grid(row = 0, column = 2, padx=2, pady= 2)
    b21_enter.grid(row = 1, column = 0, padx=2, pady= 2)
    b22_enter.grid(row = 1, column = 1, padx=2, pady= 2)
    b23_enter.grid(row = 1, column = 2, padx=2, pady= 2)
    b31_enter.grid(row = 2, column = 0, padx=2, pady= 2)
    b32_enter.grid(row = 2, column = 1, padx=2, pady= 2)
    b33_enter.grid(row = 2, column = 2, padx=2, pady= 2)

    exit_multi=Button(screen_matrixb, text = "OK", command = result_multi)
    exit_multi.grid(row = 4, column = 1)

def matrix_amulti():
    global screen_matrixa
    screen_matrixa= Tk()
    screen_matrixa.title("Matrix A")

    global a11_enter
    global a12_enter
    global a13_enter
    global a21_enter
    global a22_enter
    global a23_enter
    global a31_enter
    global a32_enter
    global a33_enter

    a11_enter=Entry(screen_matrixa)
    a12_enter=Entry(screen_matrixa)
    a13_enter=Entry(screen_matrixa)
    a21_enter=Entry(screen_matrixa)
    a22_enter=Entry(screen_matrixa)
    a23_enter=Entry(screen_matrixa)
    a31_enter=Entry(screen_matrixa)
    a32_enter=Entry(screen_matrixa)
    a33_enter=Entry(screen_matrixa)

    a11_enter.grid(row = 0, column = 0, padx=2, pady= 2)
    a12_enter.grid(row = 0, column = 1, padx=2, pady= 2)
    a13_enter.grid(row = 0, column = 2, padx=2, pady= 2)
    a21_enter.grid(row = 1, column = 0, padx=2, pady= 2)
    a22_enter.grid(row = 1, column = 1, padx=2, pady= 2)
    a23_enter.grid(row = 1, column = 2, padx=2, pady= 2)
    a31_enter.grid(row = 2, column = 0, padx=2, pady= 2)
    a32_enter.grid(row = 2, column = 1, padx=2, pady= 2)
    a33_enter.grid(row = 2, column = 2, padx=2, pady= 2)

    exit_multi=Button(screen_matrixa, text = "OK", command = matrix_bmulti)
    exit_multi.grid(row = 4, column = 1)

def matrix_multi():
    matrix_amulti()

def delete_add_result():
    result_add.destroy()
    screen_matrixa.destroy()
    screen_matrixb.destroy()

def result_add():
    global result_add

    result_add= Tk()
    result_add.title("Result")

    a11=int(a11_enter.get()) + int(b11_enter.get())
    t11=Label(result_add, text = a11)
    t11.grid(row=0,column=0,padx=15, pady=5)

    a12=int(a12_enter.get()) + int(b12_enter.get())
    t12=Label(result_add, text = a12)
    t12.grid(row=0,column=1,padx=15, pady=5)

    a13=int(a13_enter.get()) + int(b13_enter.get())
    t13=Label(result_add, text = a13)
    t13.grid(row=0,column=2,padx=15, pady=5)

    a21=int(a21_enter.get()) + int(b21_enter.get())
    t11=Label(result_add, text = a21)
    t11.grid(row=1,column=0,padx=15, pady=5)

    a22=int(a22_enter.get()) + int(b22_enter.get())
    t22=Label(result_add, text = a22)
    t22.grid(row=1,column=1,padx=15, pady=5)
    
    a23=int(a23_enter.get()) + int(b23_enter.get())
    t23=Label(result_add, text = a23)
    t23.grid(row=1,column=2,padx=15, pady=5)
    
    a31=int(a31_enter.get()) + int(b31_enter.get())
    t31=Label(result_add, text = a31)
    t31.grid(row=2,column=0,padx=15, pady=5)
    
    a32=int(a32_enter.get()) + int(b32_enter.get())
    t32=Label(result_add, text = a32)
    t32.grid(row=2,column=1,padx=15, pady=5)
    
    a33=int(a33_enter.get()) + int(b33_enter.get())
    t33=Label(result_add, text = a33)
    t33.grid(row=2,column=2,padx=15, pady=5)

    exit_add=Button(result_add, text = "OK", command = delete_add_result)
    exit_add.grid(row = 4, column = 1)

def matrix_badd():
    global screen_matrixb
    screen_matrixb= Tk()
    screen_matrixb.title("Matrix B")

    global b11_enter
    global b12_enter
    global b13_enter
    global b21_enter
    global b22_enter
    global b23_enter
    global b31_enter
    global b32_enter
    global b33_enter

    b11_enter=Entry(screen_matrixb)
    b12_enter=Entry(screen_matrixb)
    b13_enter=Entry(screen_matrixb)
    b21_enter=Entry(screen_matrixb)
    b22_enter=Entry(screen_matrixb)
    b23_enter=Entry(screen_matrixb)
    b31_enter=Entry(screen_matrixb)
    b32_enter=Entry(screen_matrixb)
    b33_enter=Entry(screen_matrixb)

    b11_enter.grid(row = 0, column = 0, padx=2, pady= 2)
    b12_enter.grid(row = 0, column = 1, padx=2, pady= 2)
    b13_enter.grid(row = 0, column = 2, padx=2, pady= 2)
    b21_enter.grid(row = 1, column = 0, padx=2, pady= 2)
    b22_enter.grid(row = 1, column = 1, padx=2, pady= 2)
    b23_enter.grid(row = 1, column = 2, padx=2, pady= 2)
    b31_enter.grid(row = 2, column = 0, padx=2, pady= 2)
    b32_enter.grid(row = 2, column = 1, padx=2, pady= 2)
    b33_enter.grid(row = 2, column = 2, padx=2, pady= 2)

    exit_add=Button(screen_matrixb, text = "OK", command = result_add)
    exit_add.grid(row = 4, column = 1)

def matrix_aadd():
    global screen_matrixa
    screen_matrixa= Tk()
    screen_matrixa.title("Matrix A")

    global a11_enter
    global a12_enter
    global a13_enter
    global a21_enter
    global a22_enter
    global a23_enter
    global a31_enter
    global a32_enter
    global a33_enter

    a11_enter=Entry(screen_matrixa)
    a12_enter=Entry(screen_matrixa)
    a13_enter=Entry(screen_matrixa)
    a21_enter=Entry(screen_matrixa)
    a22_enter=Entry(screen_matrixa)
    a23_enter=Entry(screen_matrixa)
    a31_enter=Entry(screen_matrixa)
    a32_enter=Entry(screen_matrixa)
    a33_enter=Entry(screen_matrixa)

    a11_enter.grid(row = 0, column = 0, padx=2, pady= 2)
    a12_enter.grid(row = 0, column = 1, padx=2, pady= 2)
    a13_enter.grid(row = 0, column = 2, padx=2, pady= 2)
    a21_enter.grid(row = 1, column = 0, padx=2, pady= 2)
    a22_enter.grid(row = 1, column = 1, padx=2, pady= 2)
    a23_enter.grid(row = 1, column = 2, padx=2, pady= 2)
    a31_enter.grid(row = 2, column = 0, padx=2, pady= 2)
    a32_enter.grid(row = 2, column = 1, padx=2, pady= 2)
    a33_enter.grid(row = 2, column = 2, padx=2, pady= 2)

    exit_add=Button(screen_matrixa, text = "OK", command = matrix_badd)
    exit_add.grid(row = 4, column = 1)

def matrix_add():
    matrix_aadd()

def delete_sub_result():
    result_sub.destroy()
    screen_matrixa.destroy()
    screen_matrixb.destroy()

def result_sub():
    global result_sub

    result_sub= Tk()
    result_sub.title("Result")

    a11=int(a11_enter.get()) - int(b11_enter.get())
    t11=Label(result_sub, text = a11)
    t11.grid(row=0,column=0,padx=15, pady=5)

    a12=int(a12_enter.get()) - int(b12_enter.get())
    t12=Label(result_sub, text = a12)
    t12.grid(row=0,column=1,padx=15, pady=5)

    a13=int(a13_enter.get()) - int(b13_enter.get())
    t13=Label(result_sub, text = a13)
    t13.grid(row=0,column=2,padx=15, pady=5)

    a21=int(a21_enter.get()) - int(b21_enter.get())
    t11=Label(result_sub, text = a21)
    t11.grid(row=1,column=0,padx=15, pady=5)

    a22=int(a22_enter.get()) - int(b22_enter.get())
    t22=Label(result_sub, text = a22)
    t22.grid(row=1,column=1,padx=15, pady=5)
    
    a23=int(a23_enter.get()) - int(b23_enter.get())
    t23=Label(result_sub, text = a23)
    t23.grid(row=1,column=2,padx=15, pady=5)
    
    a31=int(a31_enter.get()) - int(b31_enter.get())
    t31=Label(result_sub, text = a31)
    t31.grid(row=2,column=0,padx=15, pady=5)
    
    a32=int(a32_enter.get()) - int(b32_enter.get())
    t32=Label(result_sub, text = a32)
    t32.grid(row=2,column=1,padx=15, pady=5)
    
    a33=int(a33_enter.get()) - int(b33_enter.get())
    t33=Label(result_sub, text = a33)
    t33.grid(row=2,column=2,padx=15, pady=5)

    exit_sub=Button(result_sub, text = "OK", command = delete_sub_result)
    exit_sub.grid(row = 4, column = 1)

def matrix_bsub():
    global screen_matrixb
    screen_matrixb= Tk()
    screen_matrixb.title("Matrix B")

    global b11_enter
    global b12_enter
    global b13_enter
    global b21_enter
    global b22_enter
    global b23_enter
    global b31_enter
    global b32_enter
    global b33_enter

    b11_enter=Entry(screen_matrixb)
    b12_enter=Entry(screen_matrixb)
    b13_enter=Entry(screen_matrixb)
    b21_enter=Entry(screen_matrixb)
    b22_enter=Entry(screen_matrixb)
    b23_enter=Entry(screen_matrixb)
    b31_enter=Entry(screen_matrixb)
    b32_enter=Entry(screen_matrixb)
    b33_enter=Entry(screen_matrixb)

    b11_enter.grid(row = 0, column = 0, padx=2, pady= 2)
    b12_enter.grid(row = 0, column = 1, padx=2, pady= 2)
    b13_enter.grid(row = 0, column = 2, padx=2, pady= 2)
    b21_enter.grid(row = 1, column = 0, padx=2, pady= 2)
    b22_enter.grid(row = 1, column = 1, padx=2, pady= 2)
    b23_enter.grid(row = 1, column = 2, padx=2, pady= 2)
    b31_enter.grid(row = 2, column = 0, padx=2, pady= 2)
    b32_enter.grid(row = 2, column = 1, padx=2, pady= 2)
    b33_enter.grid(row = 2, column = 2, padx=2, pady= 2)

    exit_sub=Button(screen_matrixb, text = "OK", command = result_sub)
    exit_sub.grid(row = 4, column = 1)

def matrix_asub():
    global screen_matrixa
    screen_matrixa= Tk()
    screen_matrixa.title("Matrix A")

    global a11_enter
    global a12_enter
    global a13_enter
    global a21_enter
    global a22_enter
    global a23_enter
    global a31_enter
    global a32_enter
    global a33_enter

    a11_enter=Entry(screen_matrixa)
    a12_enter=Entry(screen_matrixa)
    a13_enter=Entry(screen_matrixa)
    a21_enter=Entry(screen_matrixa)
    a22_enter=Entry(screen_matrixa)
    a23_enter=Entry(screen_matrixa)
    a31_enter=Entry(screen_matrixa)
    a32_enter=Entry(screen_matrixa)
    a33_enter=Entry(screen_matrixa)

    a11_enter.grid(row = 0, column = 0, padx=2, pady= 2)
    a12_enter.grid(row = 0, column = 1, padx=2, pady= 2)
    a13_enter.grid(row = 0, column = 2, padx=2, pady= 2)
    a21_enter.grid(row = 1, column = 0, padx=2, pady= 2)
    a22_enter.grid(row = 1, column = 1, padx=2, pady= 2)
    a23_enter.grid(row = 1, column = 2, padx=2, pady= 2)
    a31_enter.grid(row = 2, column = 0, padx=2, pady= 2)
    a32_enter.grid(row = 2, column = 1, padx=2, pady= 2)
    a33_enter.grid(row = 2, column = 2, padx=2, pady= 2)

    exit_sub=Button(screen_matrixa, text = "OK", command = matrix_bsub)
    exit_sub.grid(row = 4, column = 1)

def matrix_sub():
    matrix_asub()    

def delete_transpose_result():
    trans_result.destroy()
    transpose.destroy()

def result_transpose():
    global trans_result

    trans_result= Tk()
    trans_result.title("Result")

    a11=a11_enter.get()
    t11=Label(trans_result, text = a11)
    t11.grid(row=0,column=0)

    a12=a12_enter.get()
    t12=Label(trans_result, text = a12)
    t12.grid(row=1,column=0)

    a13=a13_enter.get()
    t13=Label(trans_result, text = a13)
    t13.grid(row=2,column=0)

    a21=a21_enter.get()
    t21=Label(trans_result, text = a21)
    t21.grid(row=0,column=1)

    a22=a22_enter.get()    
    t22=Label(trans_result, text = a22)
    t22.grid(row=1,column=1)
        
    a23=a23_enter.get()
    t23=Label(trans_result, text = a23)
    t23.grid(row=2,column=1)
     
    a31=a31_enter.get()
    t31=Label(trans_result, text = a31)
    t31.grid(row=0,column=2)

    a32=a32_enter.get()
    t32=Label(trans_result, text = a32)
    t32.grid(row=1,column=2)
    
    a33=a33_enter.get()
    t33=Label(trans_result, text = a33)
    t33.grid(row=2,column=2)

    exit_sub=Button(trans_result, text = "OK", command = delete_transpose_result)
    exit_sub.grid(row = 4, column = 1)

def transpose():
    global transpose
    transpose= Tk()
    transpose.title("Matrix A")

    global a11_enter
    global a12_enter
    global a13_enter
    global a21_enter
    global a22_enter
    global a23_enter
    global a31_enter
    global a32_enter
    global a33_enter

    a11_enter=Entry(transpose)
    a12_enter=Entry(transpose)
    a13_enter=Entry(transpose)
    a21_enter=Entry(transpose)
    a22_enter=Entry(transpose)
    a23_enter=Entry(transpose)
    a31_enter=Entry(transpose)
    a32_enter=Entry(transpose)
    a33_enter=Entry(transpose)

    a11_enter.grid(row = 0, column = 0, padx=2, pady= 2)
    a12_enter.grid(row = 0, column = 1, padx=2, pady= 2)
    a13_enter.grid(row = 0, column = 2, padx=2, pady= 2)
    a21_enter.grid(row = 1, column = 0, padx=2, pady= 2)
    a22_enter.grid(row = 1, column = 1, padx=2, pady= 2)
    a23_enter.grid(row = 1, column = 2, padx=2, pady= 2)
    a31_enter.grid(row = 2, column = 0, padx=2, pady= 2)
    a32_enter.grid(row = 2, column = 1, padx=2, pady= 2)
    a33_enter.grid(row = 2, column = 2, padx=2, pady= 2)

    exit_add=Button(transpose, text = "OK", command = result_transpose)
    exit_add.grid(row = 4, column = 1)

def delete_main():
    screen.destroy()

def delete_exit():
    screen_exit.destroy()

def matrix_exit():
    global screen_exit
    screen_exit = Toplevel(screen)
    screen_exit.title("")
    screen_exit.geometry("150x100") 
    Label(screen_exit, text = "Do u want to exit?").pack()
    Button(screen_exit, text = "YES", command =delete_main).pack()
    Button(screen_exit, text = "NO ", command =delete_exit).pack()

def main_screen():
    global screen
    screen= Tk()
    screen.title("~~~Calculator~~~")
    screen.geometry("400x400")
    Label(screen, text = "MATRIX CALCULATOR",bg = "Cyan", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(screen, text = "").pack()
    Label(screen, text = "").pack()
    Button(screen, text = "Add Matrix",       height = "1", width = "20", command = matrix_add).pack()
    Button(screen, text = "Subtract Matrix", height = "1", width = "20", command = matrix_sub).pack()
    Button(screen, text = "Multiply Matrix",  height = "1", width = "20", command = matrix_multi).pack()
    Button(screen, text = "Transpose",        height = "1", width = "20", command = transpose).pack()
    Button(screen, text = "Determinant",      height = "1", width = "20", command = matrix_determinant).pack()
    Button(screen, text = "Exit" ,            height = "1", width = "20", command = matrix_exit).pack()
    Label(screen, text = "").pack()
    
    screen.mainloop()

main_screen()


