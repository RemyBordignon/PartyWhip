
predicate ReverseSorted(a:array<int>, low:int, high:int)
	reads a
{
	0 <= low <= high <= a.Length &&
	forall i,j :: low <= i < j < high ==> a[i] >= a[j]
}

method BubbleSort(a:array<int>)
	modifies a
	requires a.Length > 1
	ensures ReverseSorted(a, 0, a.Length)
	ensures multiset(a[..]) == multiset(old(a[..]))
{
	var i := 0;

	while (i < a.Length)
		invariant 0 <= i <= a.Length
		invariant forall x :: a.Length-i <= x < a.Length ==> forall y :: 0 <= y < a.Length-i ==> a[x] <= a[y]
		invariant ReverseSorted(a, a.Length - i, a.Length)
		invariant multiset(a[..]) == multiset(old(a[..]))
	{
		var j := 0;

		while (j < a.Length-i-1)
			invariant 0 <= j <= a.Length-i-1
			invariant forall k :: 0 <= k <= j ==> a[k] >= a[j]
			invariant forall x :: a.Length-i <= x < a.Length ==> forall y :: 0 <= y < a.Length-i ==> a[x] <= a[y]
			invariant ReverseSorted(a, a.Length-i-1, a.Length)
			invariant multiset(a[..]) == multiset(old(a[..]))
		{
			if (a[j] < a[j+1])
			{
				a[j], a[j+1] := a[j+1], a[j];
			}
			j := j + 1;
		}
		i := i + 1;
	}
}