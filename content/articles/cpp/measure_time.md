title: 時間を取得、計測する
date: 2017-09-29 0:9
category: C++
slug: measure-time-by-chrono


C++11から時間Utilのchronoライブラリが追加されました。
ここではchronoの機能を使って時間を取得、計算する方法を説明します。

現在の時間を取得する
------------------------------------------------------------------------------

現在の日時は、std::chrono::system_clock::nowを使うことで取得出来ます。

```c++
#include <chrono>

int main()
{
	std::chrono::system_clock::time_point now = std::chrono::system_clock::now();
	return 0;
}
```

経過時間を計測する
------------------------------------------------------------------------------

time_pointクラスは演算子がオーバーライドされているので単純に引き算するだけで
time_pointの時間差を求めることが出来ます。  
ただし、戻り値はstd::chrono::durationになります。

```c++
#include <chrono>
#include <iostream>

int main()
{
	std::chrono::system_clock::time_point t1 = std::chrono::system_clock::now();

	// 計測したい処理

	std::chrono::system_clock::time_point t2 = std::chrono::system_clock::now();

	std::chrono::duration<float> elapsed = t2 - t1; // floatで秒を取得
	std::chrono::nanoseconds nanoElapsed = t2 - t1; // ナノ秒で取得

	// ナノ秒をミリ秒に変換。切り捨て発生時はduration_castを利用する。
	std::chrono::milliseconds milliSeconds = std::chrono::duration_cast<std::chrono::milliseconds>(nanoElapsed);

	std::cout << elapsed.count() << std::endl;
}
```

std::chrono::nanosecondsというクラスが出てきましたが、中身はstd::chrono::duration<long long, nano>の別名になります。
また単位を変換する場合「秒→ミリ秒」なのどの切り捨てが発生しない場合は代入するだけで良いですが、
「ミリ秒→秒」などの切り捨てが発生する場合は、std::chrono::duration_castを利用します。

関連C++リファレンス
------------------------------------------------------------------------------

[C++日本語リファレンス std::chrono::system_clock::now](https://cpprefjp.github.io/reference/chrono/system_clock/now.html)  
[C++日本語リファレンス std::chrono::duration](https://cpprefjp.github.io/reference/chrono/duration.html)  

