/* Also solved this using python*/

int cycle(int n) {
   if (n%2 == 0 || n%5 == 0){
        return -1;     
   }
    int d = 9;
    int count = 1 ;   
    while (d % n != 0){
        d = d%n*10 + 9;
        count += 1;     
    }
    return count;
}
