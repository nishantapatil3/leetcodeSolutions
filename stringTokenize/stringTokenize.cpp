/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    std::string txt = "The Brown Fox Jumped over to catch the Salmon";
    std::string delimiter = " ";
    
    size_t pos = 0;
    std::string token;
    while ((pos = txt.find(delimiter)) != std::string::npos){
        token = txt.substr(0, pos);
        cout << token << endl;
        txt.erase(0, pos + delimiter.length());
    }
    cout << txt << endl;
    return 0;
}
