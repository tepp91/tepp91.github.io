title: ビットカウント
date: 2018-10-04 0:19
category: C++
slug: bit-count

SIMD(\_mm_popcnt_u32)を利用する
------------------------------------------------------------------------------

SSE 4.2からPOPCNT命令が追加されました。<!--
-->後者のビット演算に比べて非常に早く処理が出来ます。  
関数はnmmintrin.hに定義されています。

```c++
__mm_popcnt_u32(value);
```

ビット演算による計算
------------------------------------------------------------------------------

ビットの隣通りを合計していき、最終的なビット数を取得します。

```c++
uint32_t bitCount( uint32_t value )
{
	value = (value & 0x55555555) + (value >> 1  & 0x55555555);
	value = (value & 0x33333333) + (value >> 2  & 0x33333333);
	value = (value & 0x0F0F0F0F) + (value >> 4  & 0x0F0F0F0F);
	value = (value & 0x00FF00FF) + (value >> 8  & 0x00FF00FF);
	return  (value & 0x0000FFFF) + (value >> 16);
}
```
