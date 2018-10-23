method getNextGap(gap: int) returns (newGap: int)
    ensures gap > 1 ==> newGap == (gap*10)/13
    ensures gap <= 1 ==> newGap == 1
    ensures newGap > 0
{
    newGap := (gap * 10)/13;
    if (newGap < 1) {
        newGap := 1;
    }
}

predicate Sorted(a:array<int>, low:int, high:int)
    reads a
    requires 0 <= low < high <= a.Length
{
    forall i, j :: low <= i <= j < high ==> a[i] <= a[j]
}

method combSort(a:array<int>) 
    modifies a
    requires a.Length > 1
    ensures Sorted(a, 0, a.Length)
    ensures multiset(a[..]) == multiset(old(a[..]))
{
    var gap := a.Length;
    var swapped: bool := true;

    while (gap != 1) 
        invariant 1 <= gap <= a.Length
        invariant multiset(a[..]) == multiset(old(a[..]))
        invariant forall k :: 0 <= k < a.Length-gap ==> a[k] <= a[k+gap]
        decreases gap
  {
        gap := getNextGap(gap);
        var i := 0;
        while (i < a.Length-gap) 
            invariant 0 <= i <= a.Length-gap
            invariant forall k :: 0 <= k < i  ==> a[k] <= a[k+gap]
            invariant multiset(a[..]) == multiset(old(a[..]))
            // decreases  n-gap - i
  {
            if (a[i] > a[i+gap]) {
                a[i], a[i+gap] := a[i+gap], a[i];
            }
            i := i + 1;
        }
    }
}