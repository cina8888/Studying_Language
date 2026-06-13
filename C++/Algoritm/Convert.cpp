#include <iostream>
#include <cctype>
#include <string>
using namespace std;

int main()
{
    int count = 0;
    string setence = "heLlo123 45WoRld";
    for (char &word : setence) 
    {
        if (isupper(word))
        {
            word = tolower(word);
        } else if (isdigit(word))
        {
            count += (word - '0');
        } else 
        {
            word = toupper(word);
        }
    }
    
    std::cout << setence << "\n";
    std::cout << count;
    return 0;
}