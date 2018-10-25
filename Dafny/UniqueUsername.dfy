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

method UniqueUsername(usernames:array<array<char>>, newUsername:array<char>) returns (unique: bool)
	ensures unique ==> forall x :: 0 <= x < usernames.Length ==> !Identical(usernames[x], newUsername, newUsername.Length)
{
	var i := 0;
	unique := true;

	while (i < usernames.Length)
		invariant 0 <= i <= usernames.Length
		invariant unique ==> forall x :: 0 <= x < i ==> !Identical(usernames[x], newUsername, newUsername.Length)
	{
		var identical := Strcmp(usernames[i], newUsername);
		
		if (identical)
		{
			unique := false;
		}

		i := i + 1;
	}	
}