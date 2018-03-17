title: Scancode Mapによるキー割り当ての変更
date: 2018-03-17 1:12
category: Misc
slug: remap-keyboard-with-scancode-map

Scancode Map
----------------

キーボードのキー割り当ての変更をレジストリのScancode Mapを変更することで可能になります。

Scancodeは、キーボードでキーが入力された際にキーボードからCPUに送られてるコードの事です。  
Scancode MapはScancodeの変換テーブルのことで、これを設定することでキー割り当ての変更をすることが可能です。

Scacode Mapはレジストリの  
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout  
の下に「Scancode Map」というバイナリ値で作成します。


フォーマット
-------------

Scancode Mapはヘッダーの後ろにキー割り当ての情報を入れ、最後にキー割り当て終端を意味するヌル値(0のこと)を入れます。

ヘッダーに記入するキーの割り当て数（マッピング数）ですが、これは最後に入れるヌル値を含める事と、<!--
-->Windowsはリトルエンディアンのため、値が前詰めになることに注意してください。

<table>
<tr><td>ヘッダー：バージョン（すべて0）</td><td>4 byte</td></tr>
<tr><td>ヘッダー：フラグ（すべて0）</td><td>4 byte</td></tr>
<tr><td>ヘッダー：マッピング数</td><td>4 byte</td></tr>
<tr><td>キー割り当て</td><td>--</td></tr>
<tr><td>Null</td><td>4 byte</td></tr>
</table>

キー割り当ては、4byte値で表現し、前2byteが変換前のキー、後2byteで変換後のキーを表します。

例えば、Caps Lock(0x3A)を左Ctrl(0x1D)に変換する場合、0x003A001Dとなりますが、<!--
-->これもリトルエンディアンを意識する必要があるので、書く時は「1D 00 3A 00」になります。


例：「左Ctrl <-> Caps lock」「無変換 -> Enter」「変換 -> Back Space」
----------------------------------------------------------------

### Scancode Map

```
00 00 00 00 00 00 00 00
05 00 00 00 1D 00 3A 00
3A 00 1D 00 1C 00 7B 00
0E 00 79 00 00 00 00 00
```

### 解説

<table>
<tr><th>バイナリ</th><th>値</th><th>説明</th></tr>
<tr><td>00 00 00 00</td><td>0x00000000</td><td>バージョン</td></tr>
<tr><td>00 00 00 00</td><td>0x00000000</td><td>フラグ</td></tr>
<tr><td>05 00 00 00</td><td>0x00000005</td><td>マッピング数</td></tr>
<tr><td>1D 00 3A 00</td><td>0x003A001D</td><td>Caps Lock(0x1D) -> Enter(0x1D)</td></tr>
<tr><td>3A 00 1D 00</td><td>0x001D003A</td><td>Enter(0x1D) -> Caps Lock(0x1D)</td></tr>
<tr><td>1C 00 7B 00</td><td>0x007B001C</td><td>無変換(0x7B) -> Enter(0x1C)</td></tr>
<tr><td>0E 00 79 00</td><td>0x0079000E</td><td>変換(0x79) -> Back Space(0x0E)</td></tr>
<tr><td>00 00 00 00</td><td>0x00000000</td><td>終端ヌル値</td></tr>
</table>

### Scancode

<table>
<tr><td>左Ctrl</td><td>0x1D</td></tr>
<tr><td>Caps  Lock</td><td>0x3A</td></tr>
<tr><td>Enter</td><td>0x1C</td></tr>
<tr><td>無変換</td><td>7B</td></tr>
<tr><td>Back Space</td><td>0x0E</td></tr>
<tr><td>変換</td><td>0x79</td></tr>
</table>

参考
-----

[MSDN Keyboard and mouse class drivers - Scan code mapper for keyboards](https://docs.microsoft.com/en-us/windows-hardware/drivers/hid/keyboard-and-mouse-class-drivers#scan-code-mapper-for-keyboards)
