from tkinter import *
from tkinter import ttk
from functools import cmp_to_key

# effective pulls 計算用
def calc_eff_pull(aqua,x,pulls):
    return int((10+(20*(aqua-x))+pulls)*(1+2+4*x))

# リストを作成
def make_list(aqua,pulls):
  # コンパレータを定義
  def cmp(a, b):
      if calc_eff_pull(aqua,a,pulls) < calc_eff_pull(aqua,b,pulls):
          return 1
      elif calc_eff_pull(aqua,a,pulls) > calc_eff_pull(aqua,b,pulls):
          return -1
      else:
          return 0
  pullList=list(range(aqua+1))
  pullList.sort(key=cmp_to_key(cmp))
  return pullList

# 状態を入れるグローバル変数
state = 0

# Effective pullsを表示するラベルのリスト
label_list = []

root = Tk()
root.title("Effective Pulls Maximizer")

#ラベル
discription_label = ttk.Label(root,text ='一番pull数が多くなるアクアの取り方を計算します')
aqua_label = ttk.Label(root,text ='アクアビーコンの残り数')
pulls_label = ttk.Label(root,text ='Dark Greyを除いたpull数')

#入力用
aqua =  IntVar()
pulls =  IntVar()

aqua_entry = ttk.Entry(root,textvariable=aqua)
pulls_entry = ttk.Entry(root,textvariable=pulls)

#ボタンが行う操作を定義
def show_result():
    clear_label_list()
    global state,label_list,aqua,pulls
    state = 1
    label_list = []
    l = make_list(aqua.get(),pulls.get())
    for i in range(len(l)):
       label_list.append(ttk.Label(root,text =f'{l[i]} Aqua for Grey, {aqua.get()-l[i]} Aqua for Dark Grey, {calc_eff_pull(aqua.get(),l[i],pulls.get())} Effective Pulls'))
    set_layout()
    return

def clear():
    clear_label_list()
    global state
    state = 0
    aqua.set(0)
    pulls.set(0)
    set_layout()
    return

#計算ボタン
run_button = ttk.Button(root,text = 'Run',command=lambda:show_result())
clear_button = ttk.Button(root,text = 'Clear',command=lambda:clear())

#レイアウト指定用関数
def set_layout():
  global state,root
  if state == 0:
    aqua_label.grid(row=1,column=0,padx=(20, 5), pady=(5, 5))
    aqua_entry.grid(row=1,column=1,padx=(5, 20), pady=(5, 5))
    pulls_label.grid(row=2,column=0,padx=(20, 5), pady=(5, 5))
    pulls_entry.grid(row=2,column=1,padx=(5, 20), pady=(5, 5))
    run_button.grid(row=3,column=0,padx=(20, 5), pady=(5, 5))
    clear_button.grid(row=3,column=1,padx=(5, 20), pady=(5, 5))
  else:
    aqua_label.grid(row=1,column=0,padx=(20, 5), pady=(5, 5))
    aqua_entry.grid(row=1,column=1,padx=(5, 20), pady=(5, 5))
    pulls_label.grid(row=2,column=0,padx=(20, 5), pady=(5, 5))
    pulls_entry.grid(row=2,column=1,padx=(5, 20), pady=(5, 5))
    i = 2
    for l in label_list:
      i+=1
      l.grid(row=i,columnspan = 2,padx=(5, 5), pady=(5, 5))
    run_button.grid(row=i+1,column=0,padx=(20, 5), pady=(5, 5))
    clear_button.grid(row=i+1,column=1,padx=(5, 20), pady=(5, 5))

def clear_label_list():
   for l in label_list:
      l.destroy()

set_layout()


##ウィンドウの表示
root.mainloop()