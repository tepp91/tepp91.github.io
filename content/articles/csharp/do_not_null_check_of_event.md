title: EventのNullチェックを省略する
date: 2019-01-16 23:30
category: C#
slug: do-not-null-check-of-event

イベント作成時に、１つもイベントに登録がないまま呼び出してしまうと例外が発生してしまいます。  
このため、呼び出す前にヌルチェックをしなければいけませんが、それを幾つかの方法でスマートに行う事が出来ます。

Null条件演算子を利用する
------------------------

C# 6.0からNull条件演算子(?)が実装されたことで、nullチェックに関する記述が格段に楽になりました。

?演算子はnullチェックをしてnullならそのままnullを返すという演算子です。
下記の例ではTestEventのnullチェックを行い、nullだったらすぐにnullを返すため、Invokeが実行されることはありません。

```csharp
namespace Hoge
{
	delegate void TestHandler();

	class Hoge
	{
		public event TestHandler TestEvent;

		public void Exec()
		{
			TestEvent?.Invoke();
		}
	}
}
```


空のdelegateを登録する
----------------------

旧式の方法として、空のdelegateを事前に登録しておくという方法もあります。

```csharp
namespace Hoge
{
	delegate void TestHandler();

	class Hoge
	{
		public event TestHandler TestEvent = delegate {};

		public void Exec()
		{
			TestEvent(); // 空のdelegateがあるのでnullチェックしなくていい
		}
	}
}
```
