/* Don't give me five!
 In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!
 */

int dontGiveMeFive(int start, int end)
{
	int cont = 0;
	int zero, aux, j;

	for(int i=start; i<=end; i++)
	{
		zero = 1;
		aux = 0;
		if(i<0)
		{
			j = -1 * i;
		}
		else
		{
			j = i;
		}
		while(zero < j)
		{
			if((j%(zero*10) == 5) || (j/(zero*10) == 5))
			{
				aux = 1;
				break;
			}
			zero *= 10;
		}
		if(aux != 1)
		{
			cont++;
		}
	}
	return cont;
}
