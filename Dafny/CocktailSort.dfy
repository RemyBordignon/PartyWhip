
predicate Sorted(a:array<int>, low:int, high:int)
	reads a
{
	0 <= low <= high <= a.Length &&
	forall i,j :: low <= i < j < high ==> a[i] <= a[j]
}

method CocktailSort(a:array<int>)
	modifies a
	requires a.Length > 1
	ensures Sorted(a, 0, a.Length)
	ensures multiset(a[..]) == multiset(old(a[..]))
{
    var start := 0;
    var end := a.Length - 1;

	while (start < end)
        invariant start >= 0 && end <= a.Length-1
		invariant forall x :: end < x < a.Length ==> forall y :: 0 <= y < end ==> a[x] >= a[y]
        invariant forall x :: 0 <= x < start ==> forall y :: start <= y < a.Length ==> a[x] <= a[y]
		invariant Sorted(a, 0, start) && Sorted(a, end, a.Length)
		invariant multiset(a[..]) == multiset(old(a[..]))
	{
		var j := start;

		while (j < end)
			invariant start <= j <= end
			invariant forall k :: 0 <= k <= j ==> a[k] <= a[j]
            invariant forall x :: 0 <= x < start ==> forall y :: start <= y < a.Length ==> a[x] <= a[y]
			invariant forall x :: end < x < a.Length ==> forall y :: 0 <= y < end ==> a[x] >= a[y]
			invariant Sorted(a, 0, start) && Sorted(a, end, a.Length)
			invariant multiset(a[..]) == multiset(old(a[..]))
		{
			if (a[j] > a[j+1])
			{
				a[j], a[j+1] := a[j+1], a[j];
			}
			j := j + 1;
		}
        end := end - 1;

        j := end;

        while (j > start)
			invariant start <= j <= end
			invariant forall k :: j <= k <= end ==> a[k] >= a[j]
			invariant forall x :: 0 <= x < start ==> forall y :: start <= y < a.Length ==> a[x] <= a[y]
            invariant forall x :: end < x < a.Length ==> forall y :: 0 <= y < end ==> a[x] >= a[y]
			invariant Sorted(a, 0, start) && Sorted(a, end, a.Length)
			invariant multiset(a[..]) == multiset(old(a[..]))
		{
			if (a[j] < a[j-1])
			{
				a[j], a[j-1] := a[j-1], a[j];
			}
			j := j - 1;
		}
        start := start + 1;
	}
}