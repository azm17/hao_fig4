Hao et al., PRE(2015)のFig. 4の割引因子（w）ありを作成するプログラムである．

hao_fig4.py
Hao et al., PRE(2015)のFig. 4を作成するためのデータを生成（w=1，epsilon>0，xi>0）

hao_fig4_discount.py
Hao et al., PRE(2015)のFig. 4の割引因子（w<1）ありの図を作成するためのデータを生成
w=1では，分母がゼロになることがあるので，このプログラムでは作成できない．

hao_fig4_noerror.py
Hao et al., PRE(2015)のFig. 4（w=1，epsilon=0，xi=0）の図を作成するためのデータを生成

IchinoseMasudaJTB_Eq67.py
Hao et al., PRE(2015)のFig. 4（w=1，epsilon=0，xi=0）の図を作成するためのデータを生成
Ichinose&Masuda, JTB(2018)により解析的に導出されているので，それを用いてデータを生成

start.sh
hao_fig4_discount.pyを引数を与えて実行する
-Pは同時に実行するプログラム数， start_up.pyによりhao_fig4_discount.pyの引数を生成

start.sh
python3 hao_fig4.pyを引数を与えて実行する
-Pは同時に実行するプログラム数， start_up_hao.pyによりhao_fig4.pyの引数を生成

create_figure_chic.py
縦軸chi_c，横軸エラー率（epsilon+xi）の図を作成

create_figure_deltachi.py
Hao et al., PRE(2015)のFig. 4のような図を作成する
