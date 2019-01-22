#include <iostream>
#include <bitset>
#include <string>

std::string intToBinarystring(int x)
{
    std::string binary_x = std::bitset<8>(x).to_string(); //to binary
    return(binary_x);
}

int binaryCompareBits(std::string x, std::string y)
{
    int total=0;
    
    for(int i=0; i<x.length(); i++)
    {
        std::cout << x[i] << " " << y[i] << "\n";
        if(x[i] == y[i])
        {
            total = total + 0;
        }
        else
        {
            total = total + 1;
        }
    }    
    return(total);
}

int main()
{
    std::string Xs, Ys;
    int total;
    Xs = intToBinarystring(1);
    Ys = intToBinarystring(4);
    total = binaryCompareBits(Xs, Ys);
    std::cout << total << "\n";
}
