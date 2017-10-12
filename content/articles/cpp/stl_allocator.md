title: STLコンテナで使えるアロケータ
date: 2017-10-13 0:55
category: C++
slug: stl-allocator

std::vectorやstd::list等のSTLコンテナクラスでメモリを確保する際に独自のアロケータを使うためには、
STL用のアロケータを定義する必要があります。

C++11からはstd::allocator_traitsが組み込まれ、
コンテナクラスはこのallocator_traitsを介してallocatorからメモリを確保します。
std::allocator_traitsはアロケータに必要な多くの処理をカバーしてくれるため、
使用者はアロケータを書く際に多くを書く必要がなくなったらしいです。

実装
------------------------------------------------------------------------------

ここでは最小となるアロケータを紹介します。

```c++
//! STLコンテナ用アロケータ
template<class T>
struct StlAllocator{
	using value_type = T;

	//! デフォルトコンストラクタ
	StlAllocator() = default;

	//! コピーコンストラクタ
	StlAllocator( const T& )
	{
	}

	//! コピーコンストラクタ
	template<class U>
	StlAllocator( const U& )
	{
	}

	//! メモリの確保
	T* allocate( std::size_t num )
	{
		std::size_t size = sizeof(T) * num;
		return static_cast<T*>(::malloc( size ));
	}

	//! メモリの解放
	void deallocate( T* p, std::size_t /*num*/ )
	{
		::free( p );
	}
};

//-------------------------------------------------------------------------
template<class T, class U>
inline bool operator==( const StlAllocator<T>& lhs, const StlAllocator<U>& rhs )
{
	return true;
}

//-------------------------------------------------------------------------
template<class T, class U>
inline bool operator!=( const StlAllocator<T>& lhs, const StlAllocator<U>& rhs )
{
	return false;
}
```

使い方
------------------------------------------------------------------------------

```c++
std::vector<int, StlAllocator<int>> v;
std::basic_string<char, std::char_traits<char>, StlAllocator<char>> str;
```

使い方（エイリアステンプレートで使いやすくする）
------------------------------------------------------------------------------

```c++
template<class T>
using vector = std::vector<T, StlAllocator<T>>;

void Test()
{
	vector<int> v;
}
```
