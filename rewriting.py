import fileinput

# JavaScriptファイルを読み込む
with fileinput.FileInput('jasmine-html.js', inplace=True, backup='.bak') as file:
    # 行数をカウントするための変数を初期化する
    line_count = 0
    
    # ファイルを一行ずつ読み込む
    for line in file:
        # 行数をインクリメントする
        line_count += 1
        
        if line_count == 252:
            line = 'if (true) statusBarMessage += my_ticket();'
        
        # 書き換えた行をファイルに出力する
        print(line, end='')
