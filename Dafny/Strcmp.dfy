predicate Identical(a:array<char>, b:array<char>, index: int)
	reads a
	reads b
{
	a.Length == b.Length &&
	0 <= index <= a.Length &&
	forall i :: 0 <= i < index ==> a[i] == b[i]
}

method Strcmp(a:array<char>, b:array<char>) returns (identical:bool)
	ensures identical == Identical(a,b, a.Length)
{
	if (a.Length != b.Length){
		identical := false;
		return;
	}

	var index := 0;
	identical := true;
	while (index < a.Length)
		invariant 0 <= index <= a.Length
		invariant identical == Identical(a, b, index)
	{
		if (a[index] != b[index])
		{
			identical := false;
		}
		index := index + 1;
	}
}