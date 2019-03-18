//Accumulate use example

#include <iostream>
#include <numeric>

using namespace std;

int myfun(int x, int y){
    return x * y;
}

int main(){
    int sum = 1;
    int a[] = {5 , 10 , 15} ;

    cout << "Result using accumulate" << endl;
    cout << accumulate(a, a+3, sum) << endl;

    cout << "Result using myfun" << endl;
    cout << accumulate(a, a+3, sum, myfun) << endl;

    cout << "Result using pre-defined func" << endl;
    cout << accumulate(a, a+3, sum, std::minus<int>()) << endl;

    return 0;
}