/*
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
*/
#include <string>
#include <vector>
#include<iostream>

using namespace std;

vector<std::string> solution(const std::string &s)
{
  
  string  str=s;
  int StrSize=str.size();
  vector<string> NewString;

  if (StrSize%2!=0){
    str.push_back('_');
  }
  
  StrSize=str.size();
  
  for(int i=0;i<StrSize/2;i++){
    string sub=str.substr(0,2);
    NewString.push_back(sub);
    str.erase(0,2);
  }
    
    return NewString;
}
