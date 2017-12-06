title: ListViewにContextMenuを表示する
date: 2017-12-06 23:13
category: WPF
slug: listview-contextmenu

WPFでListViewにコンテキストメニューを表示する場合、最も手っ取り早いのはListView.ContextMenuに値を設定する事ですが、この選択はよくありません。<!--
-->ListView.ContextMenuはListView全体に対して表示されるので、ヘッダー部分を右クリックしてもコンテキストメニューが出てしまいます。

きちんとListViewItemにコンテキストメニューを表示するには、ListView.ItemContainerStlyeを用いてListViewItem.ContextMenuに値を設定する必要があります。<!--
-->この場合、ListViewItem.ContextMenuはListViewのDataContextを見てくれないので、ListViewItemにコマンドを設定するには、明示的にDataContextを指定する必要があります。

下記のコードではContextMenuのMenuItemに対象アイテムを引数にするコマンドを表示する例の一部です。<!--
-->サンプルプロジェクトは[GitHub](https://github.com/tepp91/WPFSampleCollection/tree/master/ListViewContextMenu)にアップしています。

ContextMenu.TagはControl的には意味関係ない任意の値を入れられるプロパティです。今回はこれを使ってContextMenuにListViewのDataContextを受け渡しています。

```xaml
<ListView ItemsSource="{Binding DogList}">
	<ListView.ItemContainerStyle>
		<Style TargetType="{x:Type ListViewItem}">
			<Setter
				Property="Tag"
				Value="{Binding DataContext, RelativeSource={RelativeSource AncestorType=ListView}}" />

			<Setter Property="ContextMenu">
				<Setter.Value>
					<ContextMenu DataContext="{Binding PlacementTarget.Tag, RelativeSource={RelativeSource Self}}">
						<MenuItem
							Header="Select"
							Command="{Binding SelectCommand}"
							CommandParameter="{Binding PlacementTarget.Content, RelativeSource={RelativeSource AncestorType=ContextMenu}}" />
					</ContextMenu>
				</Setter.Value>
			</Setter>
		</Style>
	</ListView.ItemContainerStyle>
</ListView>
```
