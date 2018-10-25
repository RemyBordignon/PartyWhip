predicate Sorted(a:array<int>, low:int, high:int)
	reads a
{
	0 <= low <= high <= a.Length &&
	forall i,j :: low <= i < j < high ==> a[i] <= a[j]
}

predicate MinElementIndex(a:array<int>, low:int, high:int, index:int)
	reads a
{
	low >= 0 && high < a.Length &&
	low <= index < a.Length &&
	forall i :: low <= i <= high ==> a[i] >= a[index]
}

method SelectionSort(a:array<int>)
	modifies a
	requires a.Length > 1
	ensures Sorted(a, 0, a.Length)
	ensures multiset(a[..]) == multiset(old(a[..]))
{
	var i := 0;

	while (i < a.Length)
		invariant 0 <= i <= a.Length
		invariant Sorted(a, 0, i)
		invariant forall x :: 0 <= x < i ==> forall y :: i <= y < a.Length ==> a[x] <= a[y]
		invariant multiset(a[..]) == multiset(old(a[..]))
	{
		var min_element_index := i;

		var j := i;
		while (j < a.Length)
			invariant i <= j <= a.Length
			invariant forall x :: 0 <= x < i ==> forall y :: i <= y < a.Length ==> a[x] <= a[y]
			invariant MinElementIndex(a, i, j-1, min_element_index)
			invariant multiset(a[..]) == multiset(old(a[..]))
		{
			if (a[j] < a[min_element_index])
			{
				min_element_index := j;
			}

			j := j + 1;
		}

		a[i], a[min_element_index] := a[min_element_index], a[i];
		i := i + 1;
	}
}