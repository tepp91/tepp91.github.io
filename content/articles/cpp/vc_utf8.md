title: Visual Studioで.cppをデフォルトでUTF-8にする
date: 2017-09-29 0:9
category: C++
slug: visual-studio-cpp-utf-8

テンプレートファイルをいじる方法
------------------------------------------------------------------------------

Visual Studioで新規作成でソースファイル(.cpp, .h)を作成する場合に使用されるテンプレートとなるファイルが  
Visual Studioのインストールフォルダの中にあります。  

このテンプレートファイルをUTF-8 BOMにしておくと、新規作成してもUtf-8になっているので誤ってShift JISが紛れ込むことはありません。
  
ファイルは

* Visual Studio 2015の場合
    * C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcprojectitems
* Visual Studio 2017(Community)の場合
    * C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\VC\vcprojectitems


にあるnewc++file.cppとhfile.hがそのテンプレートにあたります。

拡張機能を利用する方法
------------------------------------------------------------------------------

[FourceUTF8](https://marketplace.visualstudio.com/items?itemName=jz5.ForceUTF8withBOM-18593)というのがあります。  
こちらは保存する際にShift JISの際にUTF-8(BOMあり・なし)に自動変換して保存してくれる拡張機能です。  
