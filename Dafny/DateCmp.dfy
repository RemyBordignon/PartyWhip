predicate DateGreaterThan(date1:Date, date2:Date)
	reads date1
	reads date2
{
	date1.Year > date2.Year ||
	(date1.Year == date2.Year && date1.Month > date2.Month) ||
	(date1.Year == date2.Year && date1.Month == date2.Month && date1.Day > date2.Day)
}

class {:autocontracts} Date
{
	var Day: int;
	var Month: int;
	var Year: int;

	predicate Valid()
	{
		1 <= Month <= 12 &&
		Month in [1,3,5,7,8,10,12] ==> 1 <= Day <= 31 &&
		Month in [4,5,9,11] ==> 1 <= Day <= 30 &&
		Month == 2 ==> 1 <= Day <= 28
	}

	constructor(day:int, month:int, year:int)
		ensures Day == day && Month == month && Year == year
	{
		Day := day;
		Month := month;
		Year := year;
	}

	method GreaterThan(date:Date) returns (greaterThan:bool)
		 ensures greaterThan == DateGreaterThan(this, date)
	{
		greaterThan := false;

		if (this.Year > date.Year ||
		   (this.Year == date.Year && this.Month > date.Month) ||
		   (this.Year == date.Year && this.Month == date.Month && this.Day > date.Day))
		{
			greaterThan := true;
		}
	}
}