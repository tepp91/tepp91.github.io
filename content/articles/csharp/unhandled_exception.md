title: キャッチされなかった例外を受け取る
date: 2018-02-01 21:45
category: C#
slug: unhandled-exception

キャッチされなかった例外があると、[System.AppDomain.UnhandledExceptionイベント](https://msdn.microsoft.com/ja-jp/library/system.appdomain.unhandledexception(v=vs.110).aspx)が発生します。

このイベントを受け取ることで、例外がキャッチできずユーザーに残念なダイアログを表示せずに済みます。  
なにより安全に終了し、例外ログを残すような処理をすることが可能になります。

```csharp  
namespace TimeSignal
{
	public class Sample
	{
		/// <summary>
		/// アプリ開始時の処理
		/// </summary>
		public void OnStartUp()
		{
			// イベントを登録
			System.AppDomain.CurrentDomain.UnhandledException += OnUnhandledException;
		}

		/// <summary>
		/// ハンドリングされなかった例外のハンドリング
		/// </summary>
		private void OnUnhandledException(object sender, System.UnhandledExceptionEventArgs e)
		{
			// ここでエラーメッセージとか出す

			System.Environment.Exit( 1 );
		}
	}
}
```
