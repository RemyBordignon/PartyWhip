predicate Sorted(a:array<int>, low:int, high:int)
	reads a
{
	0 <= low <= high <= a.Length &&
	forall i,j :: low <= i < j < high ==> a[i] <= a[j]
}

method InsertionSortShuffle(a:array<int>)
	modifies a
	requires a.Length>1
	ensures Sorted(a, 0, a.Length)
	ensures multiset(a[..]) == multiset(old(a[..]))
{
	var curr := 1;
	while (curr < a.Length)
		invariant 1 <= curr <= a.Length
		invariant Sorted(a, 0, curr);
		invariant multiset(a[..]) == multiset(old(a[..]))
	{
		var num := a[curr];
		var prev := curr - 1;
		a[curr] := a[prev];

		while (prev >= 0 && a[prev] > num)
			invariant -1 <= prev < curr
			invariant forall i :: prev < i < curr ==> a[i] >= num
			invariant Sorted(a, 0, curr + 1)
			invariant multiset(a[..]) + multiset([num]) - multiset([a[prev + 1]]) == multiset(old(a[..]))
		{
			a[prev + 1] := a[prev];
			prev := prev - 1;
		}

		a[prev + 1] := num;
		curr := curr + 1;
	}
}