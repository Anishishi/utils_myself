## 各プログラムの概要と使い方の例

- client.py

  socketクライアントになれる

  ```
  python3 client.py
  ```

- server.py

  socketクライアントになれる

  ```
  python3 server.py
  ```

- divide_into_trainvaltest.py

  データセットをtrain/val/testにランダムにわけることができる．

  - data/*としてファイルが入っている場合→hogefolder内にtrain/val/testのサブフォルダができる

    ```
    python3 divide_into_trainvaltest.py --input_data_folder data --dir_type onlyfiles
    ```

    

  - data/input,data/annoというようにannotationデータに別れている場合→hogefolder/input,hogefolder/annoのそれぞれにtrain/val/testのサブフォルダができる

    ```
    python3 divide_into_trainvaltest.py --input_data_folder original_data --dir_type inputDir_and_annoDir --divide_ratio 1,1,1
    ```

    この場合，train:val:test=1:1:1，とすることができる．

- get_ops_and_process.py

  parserオブジェクトのサンプル．このオブジェクトを使うと様々な入力が受け取れ，受け取ったものをプログラム開始前に出力することができる．

  ```
  python3 get_ops_and_process.py hey --flag --d_value wow --a_req req
  ```

## 以下は作成中

- read_write_recursively.py

  あるフォルダ内のサブディレクトリも含めて，全てのファイルを読んで別のあるフォルダに書くプログラム



