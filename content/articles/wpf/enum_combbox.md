title: 列挙体をコンボボックスにBindingする
date: 2018-04-03 21:00
category: WPF
slug: enum-combobox

マークアップ拡張を利用することで、列挙体をコンボボックスにBindingすることができます。  
また、今回は列挙体に任意の文字列を紐付けて表示するようにします。

ObjectDataProviderを利用する方法もありますが、アプリ内で利用する度にObjectDataProviderを定義する必要があり冗長性があるため、<!--
-->マークアップ拡張のほうが好みです。

サンプルプロジェクトは[GitHub](https://github.com/tepp91/WPFSampleCollection/tree/master/EnumComboBox)にアップしています。

列挙体
----------------

列挙体を定義する際に、Description属性を使用して列挙体の各値に文字列を紐付けておきます。<!--
-->今回はDisplay属性を使用していますが、Description属性等でも問題ありません（コンバーター要調整）

```csharp
using System.ComponentModel.DataAnnotations;

namespace EnumComboBox
{
	enum Dogs
	{
		[Display(Name = "Golden Retriver")]
		GoldenRetriver,

		[Display(Name = "Miniture Dachshund")]
		MinitureDachshund,

		[Display(Name = "Border Collie")]
		BorderCollie,
	}
}
```

コンバーター
-----------------

列挙体からDisplay属性に設定した文字列に変換するためのコンバートを用意します。

```csharp
using System;
using System.Globalization;
using System.Windows.Data;
using System.Reflection;
using System.ComponentModel.DataAnnotations;

namespace EnumComboBox
{
	class EnumDisplayConverter : IValueConverter
	{
		public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
		{
			FieldInfo field = value.GetType().GetField(value.ToString());
			DisplayAttribute attr = field.GetCustomAttribute<DisplayAttribute>();
			if (attr != null) {
				return attr.Name;
			}
			return value.ToString();
		}

		public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
		{
			throw new NotImplementedException();
		}
	}
}
```

マークアップ拡張
-----------------

列挙体の型からリストを作成するマークアップ拡張です。

```csharp
using System;
using System.Windows.Markup;

namespace EnumComboBox
{
	public class EnumListExtension : MarkupExtension
	{
		private Type enumType_;

		public EnumListExtension(Type type)
		{
			enumType_ = type;
		}

		public override object ProvideValue(IServiceProvider serviceProvider)
		{
			return Enum.GetValues(enumType_);
		}
	}
}
```

Xaml
------

上記の3つを利用したXamlは以下のように書きます。

```xaml
<ComboBox ItemsSource="{Binding Source={local:EnumList {x:Type local:Dogs}}}">
	<ComboBox.Resources>
		<local:EnumDisplayConverter x:Key="EnumDisplayConv"/>
	</ComboBox.Resources>

	<ComboBox.ItemTemplate>
		<DataTemplate>
			<TextBlock Text="{Binding Converter={StaticResource EnumDisplayConv}}" />
		</DataTemplate>
	</ComboBox.ItemTemplate>
</ComboBox>
```
