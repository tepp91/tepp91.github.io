title: EventのNullチェックを省略する
date: 2017-11-26 23:50
category: C#
slug: do-not-null-check-of-event

イベント作成時に、１つもイベントに登録がないまま呼び出してしまうと例外が発生してしまいます。

このため、呼び出す前にヌルチェッックをしなければいけないのですが、  
初期化時に空のdelegateを登録してあげることで、その手間を回避することが可能です。

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
